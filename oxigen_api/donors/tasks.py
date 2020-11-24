from oxigen_api.donors import models
from config import celery_app
from bs4 import BeautifulSoup
import requests


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
    for tr in trs:
        i += 1
        donor_name = tr.find_all('td')[0].text
        donor_amount = float(tr.find_all('td')[1].text.replace(' RON', '').replace(',', ''))
        donor_comment = tr.find_all('td')[2].text
        donor, created = models.Donor.objects.get_or_create(
            name=donor_name.strip(),
            campaign=campaign,
            amount=donor_amount,
            comment=donor_comment
            )
        if created:
            donor.display_name = donor.name.split(' ')[0]
            donor.save()
        # print(donor)

    # Expenses
    expenses_table = soup.find(attrs={'class': 'entry combo'}).find('table')
    for tr in expenses_table.find_all('tr')[2:]:
        tds = tr.find_all('td')
        expense = models.Expense.objects.get_or_create(
            campaign=campaign,
            document=tds[0].text,
            amount=tds[1].text.replace(',', '.'),
            supplier=tds[2].text,
            name=tds[3].text,
            status=tds[4].text,
            comment=tds[5].text,
            )
        # print(expense)
    return len(trs)

