# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core import exceptions
from django.utils.text import slugify
from oxigen_api.donors import models
import json
from glob import glob
import os
import json
from datetime import datetime
import locale
import re
import csv
from pprint import pprint
import gspread


class Command(BaseCommand):
    help = "Will try to import json file"

    def handle(self, *args, **options):
        self.do_bulk_import()

    def do_bulk_import(self):
        i = 0
        client = gspread.service_account(filename='secrets/oxigen-gsheet.json')
        campaign, _ = models.Campaign.objects.get_or_create(name='Oxigen pentru Timisoara')
        sheet = client.open("Date centralizate").worksheet('buget + nevoi identificate').get_all_records()
        for row in sheet:
            if row['denumire'] and row['denumire'] != 'Total':
                pprint(row)
                need, _ = models.Need.objects.get_or_create(
                    name=row['denumire'], campaign=campaign)

                need.quantity = row['cantitate']
                need.stock = row['achiziționat'] if row['achiziționat'] else 0
                need.price = row['total lei'].replace("RON",'').replace('.', '').replace(',', '.')
                need.recipient = row['beneficiari']
                need.comment = row['observații']
                need.save()


        # sheet = client.open("Date centralizate").worksheet('Cheltuieli realizate').get_all_records()
        # for row in sheet:
        #     print(row)
