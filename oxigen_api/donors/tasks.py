from django.db import transaction
from oxigen_api.donors import models
from config import celery_app
from bs4 import BeautifulSoup
import requests
import gspread
from pprint import pprint
from datetime import datetime


@celery_app.task()
def sync_spreadsheet():
    client = gspread.service_account(filename='secrets/oxigen-gsheet.json')
    campaign, _ = models.Campaign.objects.get_or_create(name='Oxigen pentru Timisoara')
    sheet = client.open("Date centralizate").worksheet('buget + nevoi identificate').get_all_records()
    with transaction.atomic():
        models.Need.objects.update(display=False)
        for row in sheet:
            if row['denumire'] and row['denumire'] != 'Total':
                # pprint(row)
                need, _ = models.Need.objects.get_or_create(
                    name=row['denumire'], campaign=campaign)

                need.quantity = row['cantitate'] if row['cantitate'] else 0
                need.stock = row['achiziționat'] if row['achiziționat'] else 0
                need.price = row['total lei'].replace("RON",'').replace('.', '').replace(',', '.') if row['total lei'] else 0
                need.recipient = row['beneficiari']
                need.comment = row['observații']
                need.display = True
                need.save()
                print(need, need.display)

    sheet = client.open("Date centralizate").worksheet('Cheltuieli realizate').get_all_records()
    with transaction.atomic():
        models.Expense.objects.update(display=False)
        for row in sheet:
            if row['item']:
                # pprint(row)
                expense, _ = models.Expense.objects.get_or_create(
                    name=row['item'], campaign=campaign)
                expense.supplier = row['furnizor']
                expense.document = row['document']
                expense.status = row['status']
                expense.quantity = row['cantitate']
                expense.in_use = row['utilizat']
                expense.available = row['disponibil']
                expense.price = str(row['suma']).replace(',', '.')
                expense.comment = row['observatii']
                expense.display = True
                expense.save()
    return 'OK'


@celery_app.task()
def get_campaign_stats():
    campaign, _ = models.Campaign.objects.get_or_create(name='Oxigen pentru Timisoara')
    r = requests.get('https://www.timotion.ro/proiecte-2020/solidari-in-fata-covid-19/')
    soup = BeautifulSoup(r.text, 'html.parser')

    # Campaign stats
    campaign_stats = soup.find_all(attrs={"class": "fundraiser-numbers"})

    campaign.amount_collected = float(campaign_stats[0].find_all('span')[1].text.replace(',', ''))
    campaign.target = float(campaign_stats[1].find_all('span')[1].text.replace(',', ''))
    campaign.donations = float(campaign_stats[3].find_all('span')[1].text.replace(',', ''))
    campaign.save()

    # Donors
    donors_table = soup.find('table', attrs={"class": "donations"})
    trs = donors_table.find_all('tr')
    trs.reverse()
    i = 0
    with transaction.atomic():
        models.Donor.objects.update(display=False)
        for tr in trs:
            i += 1
            # pprint(tr)
            donor_name = tr.find_all('td')[0].text
            donor_amount = float(tr.find_all('td')[1].text.replace(' RON', '').replace(',', ''))
            donor_comment = tr.find_all('td')[2].text

            # donor, created = models.Donor.objects.get_or_create(
            #     # name=donor_name.strip(),
            #     campaign=campaign,
            #     order=i,
            #     )
            donor_filter = models.Donor.objects.filter(campaign=campaign, name=donor_name.strip(), amount=donor_amount, display=False)
            if donor_filter:
                donor = donor_filter[0]
            else:
                donor, _ = models.Donor.objects.create(campaign=campaign, name=donor_name.strip(), amount=donor_amount)

            donor.order = i
            donor.comment = donor_comment
            donor.display = True
            if not donor.display_name:
                donor.display_name = donor.name.split(' ')[0]
            donor.save()
        # print(donor)

    # # Expenses
    # expenses_table = soup.find(attrs={'class': 'entry combo'}).find('table')
    # for tr in expenses_table.find_all('tr')[2:]:
    #     tds = tr.find_all('td')
    #     print(tds)
    #     expense = models.Expense.objects.get_or_create(
    #         campaign=campaign,
    #         document=tds[0].text,
    #         amount=tds[1].text.replace(',', '.'),
    #         supplier=tds[2].text,
    #         name=tds[3].text,
    #         comment=tds[4].text,
    #         )
        # print(expense)
    return len(trs)


@celery_app.task()
def sync_covid19_pmt():
    r = requests.get('https://covid19.primariatm.ro/')
    soup = BeautifulSoup(r.text, 'html.parser')

    stats = soup.find_all(attrs={'class': 'tracking-tighter'})
    hospitals_ocupation_rate = soup.find_all('span', attrs={'class': 'text-red-600'})[0].text.replace('%', '')
    today = datetime.today()

    covid_stats, _ = models.CovidStats.objects.get_or_create(date=today)
    covid_stats.hospitals_ocupation_rate = hospitals_ocupation_rate
    covid_stats.new_cases = stats[1].text
    covid_stats.infection_rate = stats[0].text.replace(',', '.')
    covid_stats.save()
    # campaign.amount_collected = float(campaign_stats[0].find_all('span')[1].text.replace(',', ''))
    # campaign.target = float(campaign_stats[1].find_all('span')[1].text.replace(',', ''))
    # campaign.donations = float(campaign_stats[3].find_all('span')[1].text.replace(',', ''))
    # campaign.save()

    return 'OK'
