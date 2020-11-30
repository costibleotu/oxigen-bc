from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.utils.html import strip_tags
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from .serializers import (
    CampaignSerializer,
    DonorSerializer,
    FullNameDonorSerializer,
    ExpenseSerializer,
    PartnerSerializer,
    QuoteSerializer,
    NeedSerializer,
    FAQSerializer,
    CovidStatSerializer,
    StorySerializer
)

from oxigen_api.donors import models


class DashboardViewSet(ViewSet):
    """
    Dashboard with all data
    """

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def list(self, request):
        campaign = CampaignSerializer(
            models.Campaign.objects.last())

        needs = NeedSerializer(
            models.Need.objects.filter(display=True),
            many=True)

        expenses = ExpenseSerializer(
            models.Expense.objects.filter(display=True),
            many=True)

        companies = DonorSerializer(
            models.Donor.objects.filter(
                display=True, is_company=True).order_by('-order')[:5],
            many=True)

        quotes = QuoteSerializer(
            models.Quote.objects.filter(
                display=True).order_by('order'),
            many=True)

        faqs = FAQSerializer(
            models.FAQ.objects.filter(
                display=True).order_by('order'),
            many=True)

        partners = PartnerSerializer(
            models.Partner.objects.filter(
                display=True, partner_type='project').order_by('order'),
            many=True)

        media_partners = PartnerSerializer(
            models.Partner.objects.filter(
                display=True, partner_type='media').order_by('order'),
            many=True)

        covid_stats = CovidStatSerializer(
            models.CovidStats.objects.last())

        result = {
            'campaign': campaign.data,
            'companies': companies.data,
            'needs': needs.data,
            'expenses': expenses.data,
            'quotes': quotes.data,
            'faqs': faqs.data,
            'covid_stats': covid_stats.data,
            'partners': partners.data,
            'media_partners': media_partners.data,
        }
        return Response(result)


class CampaignViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = CampaignSerializer
    queryset = models.Campaign.objects.all()

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DonorViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = FullNameDonorSerializer
    queryset = models.Donor.objects.filter(
        display=True).prefetch_related('campaign').order_by('-order')

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class StoryViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = StorySerializer
    queryset = models.Story.objects.filter(
        display=True).prefetch_related('campaign').order_by('-order')

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class NamedDonorViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = DonorSerializer
    queryset = models.Donor.objects.exclude(
        name="Anonim").filter(display=True).prefetch_related('campaign').order_by('-order')

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ExpenseViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = ExpenseSerializer
    queryset = models.Expense.objects.filter(
        display=True).prefetch_related('campaign')

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PartnerViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = PartnerSerializer
    queryset = models.Partner.objects.filter(
        display=True).prefetch_related('campaign').order_by('order')

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class QuoteViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = QuoteSerializer
    queryset = models.Quote.objects.filter(
        display=True).prefetch_related('campaign')

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class NeedViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = NeedSerializer
    queryset = models.Need.objects.filter(
        display=True).prefetch_related('campaign')

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class FAQViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = FAQSerializer
    queryset = models.FAQ.objects.filter(
        display=True).prefetch_related('campaign').order_by('order')

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
