# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core import exceptions
from django.utils.text import slugify
from home import models
import json
from glob import glob
import os
import json
from datetime import datetime
import locale
import re
import csv
from unidecode import unidecode
from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
from taggit.models import Tag


class Command(BaseCommand):
    help = "Will try to import json file"

    def handle(self, *args, **options):
        self.do_bulk_import()

    def do_bulk_import(self):
        i = 0
        client = gspread.service_account(filename='../secrets/gsheet.json')

        collections_index = models.CollectionsIndexPage.objects.last()
        authors_index = models.AuthorsPage.objects.last()
        works_index = models.WorksPage.objects.last()

        # for author in models.AuthorPage.objects.all():
        #     print('delete author ', author)
        #     author.delete()
        # for work in models.WorkPage.objects.all():
        #     print('delete work', work)
        #     work.delete()
        # for collection in models.CollectionPage.objects.all():
        #     print('delete collection ', collection)
        #     collection.delete()

        collections_index = models.CollectionsIndexPage.objects.last()
        authors_index = models.AuthorsPage.objects.last()
        works_index = models.WorksPage.objects.last()

        sheet = client.open("DB__FLO_2020").worksheet('COLLECTIONS').get_all_records()
        for row in sheet:
            collection_group = models.CollectionsGroupPage.objects.filter(title=row['title'])
            if not collection_group.exists():
                collection_group = models.CollectionsGroupPage()
                collection_group.title = row['title']
                collections_index.add_child(instance=collection_group)

            collection_group = models.CollectionsGroupPage.objects.get(title=row['title'])
            collection = models.CollectionPage.objects.filter(title=row['subcollection'])
            if not collection.exists():
                collection = models.CollectionPage()
                collection.title = row['subcollection']
                collection.short_title = row['subcollection-short']
                collection_group.add_child(instance=collection)
            else:
                collection = collection[0]
            collection.works.set([])
            collection.save()
            # print('Collection group:', collection_group)
            # print('Collection:', collection)

        sheet = client.open("DB__FLO_2020").worksheet('AUTHORS').get_all_records()
        for row in sheet:
            row_first_name = row['first_name'].strip()
            row_last_name = row['last_name'].strip()
            row_author_type = row['author_type'].strip()
            row_country_of_birth = row['country_of_birth'].strip()
            row_date_of_birth = row['date_of_birth']
            row_date_of_death = row['date_of_death']
            row_website = row['website'].strip()
            row_email = row['email'].strip()
            row_bio = row['bio'].strip()
            row_aditional_info = row['aditional_info'].strip()

            row_collective = row['collective'].strip()


            title = '{} {}'.format(row_first_name, row_last_name).strip()

            author = models.AuthorPage.objects.filter(title=title)
            if not author.exists():
                author = models.AuthorPage()
                author.title = title
                authors_index.add_child(instance=author)
            else:
                author = author[0]
            print('author:', author)
            author.first_name = row_first_name
            author.last_name = row_last_name
            author.author_type, _ = models.AuthorType.objects.get_or_create(name=row_author_type)
            author.country_of_birth, _ = models.Country.objects.get_or_create(name=row_country_of_birth)

            if row_date_of_birth:
                author.date_of_birth = datetime.strptime(str(row_date_of_birth), '%Y')

            if row_date_of_death:
                author.date_of_death = datetime.strptime(str(row_date_of_death), '%Y')

            author.website = []
            for website in row_website.split(','):
                if website:
                    if website.startswith('http://') or website.startswith('https://'):
                        website_url = website
                    else:
                        website_url = 'http://' + website

                    author.website.append(website_url)

            author.email = row_email.split(',')[0]
            try:
                author.save()
            except:
                author.email = None
            author.bio = row_bio
            author.aditional_info = row_aditional_info


            if row_collective:
                collective = models.AuthorPage.objects.filter(
                    title=row_collective
                )

                if not collective.exists():
                    collective = models.AuthorPage()
                    collective.title = row_collective
                    authors_index.add_child(instance=collective)
                else:
                    collective = collective[0]
                collective.author_type, _ = models.AuthorType.objects.get_or_create(name='Collective')
                if not author.pk in collective.collective.values_list('author__pk', flat=True):
                    collective_member = models.CollectiveAuthors()
                    collective_member.author = author
                    collective.collective.add(collective_member)
                    collective.save()

            author.save()

        sheet = client.open("DB__FLO_2020").worksheet('WORKS').get_all_records()
        for row in sheet:
            row_title = str(row['title']).strip()
            row_subtitle = row['subtitle'].strip()
            row_original_title = row['original_title'].strip()
            row_original_subtitle = row['original_subtitle'].strip()
            row_music_title = row['music_title'].strip()
            row_website = row['website'].strip()
            row_keywords = row['keywords'].strip()
            row_year_of_production = row['year_of_production']

            row_categories = row['categories'].strip()
            row_contribution_type = row['contribution_type'].strip()
            row_work_type = row['work_type'].strip()
            row_countries = str(row['countries']).strip()
            row_rights = row['rights'].strip()
            row_original_title_language = row['original_title_language'].strip()
            row_language = row['language'].strip()
            row_event_location = row['event_location'].strip()
            row_date_start = row['date_start'].strip()
            row_date_end = row['date_end'].strip()

            row_authors = row['authors'].strip()
            row_collections = str(row['collections']).strip()

            row_synopsis = str(row['synopsis']).strip()
            row_aditional_info = row['aditional_info'].strip()
            print('work:', row_title)
            work = models.WorkPage.objects.filter(title=row_title)
            if not work.exists():
                work = models.WorkPage()
                work.title = row_title
                if work.title == '####':
                    work.slug = 'dddd'
                else:
                    work._generate_slug()
                works_index.add_child(instance=work)
            else:
                work = work[0]

            work.title = row_title
            work.subtitle = row_subtitle
            work.original_title = row_original_title if row_original_title else None
            work.original_subtitle = row_original_subtitle
            work.music_title = row_music_title

            work.website = []
            for website in row_website.split(','):
                if website:
                    if website.startswith('http://') or website.startswith('https://'):
                        website_url = website
                    else:
                        website_url = 'http://' + website
                    work.website.append(website_url)

            work.year_of_production = row_year_of_production if row_year_of_production else None

            try:

                work.work_type, _ = models.WorkType.objects.get_or_create(name=row_work_type)
                work.rights, _ = models.Licence.objects.get_or_create(name=row_rights)
                work.original_title_language = models.Language.objects.get_or_create(name=row_original_title_language)[0] if row_original_title_language else None
                work.language, _ = models.Language.objects.get_or_create(name=row_language) if row_language else None, None
                work.event_location, _ = models.EventLocation.objects.get_or_create(name=row_event_location) if row_event_location else None, None
                work.date_start  = datetime.strptime(row_date_start, '%d.%m.%Y') if row_date_start else None
                work.date_end  = datetime.strptime(row_date_end, '%d.%m.%Y') if row_date_end else None

                author_index = -1
                work.authors.set([])
                for author in row_authors.strip().replace('   ', ' ').replace('  ',' ').split("|"):
                    author = author.strip()
                    author_index += 1
                    if author:
                        try:
                            author_page = models.AuthorPage.objects.filter(title=author)[0]
                            # if not author_page.exists():
                            #     author_page = models.AuthorPage()
                            #     author_page.title = author
                            #     authors_page.add_child(instance=author_page)
                            # else:
                            #     author_page = author_page[0]

                            if not author in work.authors.values_list(
                                "author__title", flat=True
                            ):
                                work_author = models.WorkAuthors()
                                work_author.author = author_page
                                work_author.contribution_type, _ = models.ContributionType.objects.get_or_create(name=row_contribution_type.split("|")[author_index].strip())
                                work.authors.add(work_author)
                                work.save()
                        except:
                            pass
                            print('---------Did not find  author {} in work {}'.format(author, work))
                for collection_str in row_collections.split('|'):
                    collection = models.CollectionPage.objects.get(short_title=collection_str)
                    if work.pk not in collection.works.values_list('work__pk', flat=True):
                        work_collection = models.WorkCollections()
                        work_collection.work = work
                        collection.works.add(work_collection)
                        collection.save()

                for category in row_categories.split("|"):
                    category = category.strip()
                    category_page = models.Category.objects.filter(
                        name=category
                    )
                    if not category_page.exists():
                        category_page = models.Category()
                        category_page.name = category
                        category_page.save()
                    else:
                        category_page = category_page[0]

                    if not category in work.categories.values_list(
                        "category__name", flat=True
                    ):
                        work_category = models.WorkCategories()
                        work_category.category = category_page
                        work.categories.add(work_category)
                work.countries.set([])
                work_countries = work.countries.values_list("country__name", flat=True)
                for c in row_countries.split("|"):
                    c = c.strip()
                    country_page, _ = models.Country.objects.get_or_create(name=c)

                    if not c in work_countries:
                        work_country = models.WorkCountries()
                        work_country.country = country_page
                        work.countries.add(work_country)
                # models.WorkPage.objects.live().exclude(tags=None).values("tags__name", "tags__pk")
                work.tags.set()
                for keyword in row_keywords.split(','):
                    keyword = keyword.strip()[:100]
                    tag, _ = Tag.objects.get_or_create(name=keyword)
                    work.tags.add(tag)
                work.synopsis = row_synopsis
                # try:
                #     if not work.synopsis:
                #         work.synopsis.stream_data.append(
                #             {
                #                 "type": "paragraph_block",
                #                 "value": row["Description"],
                #             }
                #         )
                # except:
                #     pass
                # work.full_clean()
                work.save()
            except Exception as e:
                print(work, '-------------', e)

        sheet = client.open("DB__FLO_2020").worksheet('VIDEOS').get_all_records()
        for row in sheet:
            row_title = str(row['title']).strip()
            row_duration = row['duration']
            row_screen_format = row['screen_format']
            row_sound = row['sound (YES/NO)']
            try:
                video_page = models.WorkPage.objects.get(title=row_title)
                video_page.video_format = row_screen_format
                video_page.video_sound = True if row_sound == 'Sound' else False
                print('Video: ', video_page)
                video_page.save()
            except Exception as e:
                print('Video: {} ------ {}'.format(row_title, e))
