from rest_framework import serializers
from oxigen_api.donors import models


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Campaign
        exclude = ['display']


class DonorSerializer(serializers.ModelSerializer):
    campaign = serializers.SerializerMethodField()

    class Meta:
        model = models.Donor
        exclude = ['display', 'name', 'date_added']

    def get_campaign(self, obj):
        return obj.campaign.name


class ExpenseSerializer(serializers.ModelSerializer):
    campaign = serializers.SerializerMethodField()

    class Meta:
        model = models.Expense
        exclude = ['display']

    def get_campaign(self, obj):
        return obj.campaign.name


class PartnerSerializer(serializers.ModelSerializer):
    campaign = serializers.SerializerMethodField()

    class Meta:
        model = models.Partner
        exclude = ['display']

    def get_campaign(self, obj):
        return obj.campaign.name


class QuoteSerializer(serializers.ModelSerializer):
    campaign = serializers.SerializerMethodField()

    class Meta:
        model = models.Quote
        exclude = ['display']

    def get_campaign(self, obj):
        return obj.campaign.name


class NeedSerializer(serializers.ModelSerializer):
    campaign = serializers.SerializerMethodField()

    class Meta:
        model = models.Need
        exclude = ['display']

    def get_campaign(self, obj):
        return obj.campaign.name
