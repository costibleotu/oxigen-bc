from django.db.models import Sum
from django.utils.html import strip_tags
from rest_framework import serializers
from oxigen_api.donors import models
import html.parser


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
        return models.Donor.objects.filter(
            is_company=True).aggregate(Sum('amount'))['amount__sum']

    def get_donors_sum(self, obj):
        return models.Donor.objects.filter(
            is_company=False).aggregate(Sum('amount'))['amount__sum']

    def get_donors_count(self, obj):
        return models.Donor.objects.exclude(is_company=True).count()


class DonorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Donor
        exclude = ['display', 'name', 'date_added']


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Story
        exclude = ['display']


class FullNameDonorSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Donor
        exclude = ['display', 'name', 'date_added']

    def get_display_name(self, obj):
        if obj.is_company:
            return obj.display_name
        return obj.name

    def to_representation(self, instance):
        html_parser = html.parser.HTMLParser()
        data = super().to_representation(instance)
        if instance.comment:
            data['comment'] = strip_tags(
                html_parser.unescape(instance.comment))

        return data


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

    def to_representation(self, instance):
        html_parser = html.parser.HTMLParser()
        data = super().to_representation(instance)
        if instance.comment:
            data['comment'] = strip_tags(
                html_parser.unescape(instance.comment))

        return data


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
        fields = [
            "hospitals_ocupation_rate", "new_cases", "infection_rate", "date"]
