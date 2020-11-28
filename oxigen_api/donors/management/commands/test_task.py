# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core import exceptions
from django.utils.text import slugify
from oxigen_api.donors import tasks


class Command(BaseCommand):
    help = "Will try to import json file"

    def handle(self, *args, **options):
        self.do_bulk_import()

    def do_bulk_import(self):
        print('heello')
        t = tasks.sync_spreadsheet()
        print(t)
