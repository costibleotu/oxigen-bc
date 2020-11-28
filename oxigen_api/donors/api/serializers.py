from django.db.models import Sum
from rest_framework import serializers
from oxigen_api.donors import models


class CampaignSerializer(serializers.ModelSerializer):
    companies_count = serializers.SerializerMethodField()
    companies_sum = serializers.SerializerMethodField()
    donors_count = serializers.SerializerMethodField()
    donors_sum = serializers.SerializerMethodField()

    class Meta:
        model = models.Campaign
        exclude = ['display', ]

    def get_companies_count(self, obj):
        return models.Donor.objects.filter(is_company=True).count()

    def get_companies_sum(self, obj):
        return models.Donor.objects.filter(is_company=True).aggregate(Sum('amount'))['amount__sum']

    def get_donors_sum(self, obj):
        return models.Donor.objects.filter(is_company=False).aggregate(Sum('amount'))['amount__sum']

    def get_donors_count(self, obj):
        return models.Donor.objects.exclude(is_company=True).count()


class DonorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Donor
        exclude = ['display', 'name', 'date_added']


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Expense
        exclude = ['display', 'campaign']


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Partner
        exclude = ['display', 'campaign']


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quote
        exclude = ['display', 'campaign']


class NeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Need
        exclude = ['display', 'campaign']


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FAQ
        exclude = ['display', 'campaign']


class CovidStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CovidStats
        fields = ["hospitals_ocupation_rate", "new_cases", "infection_rate", "date"]
