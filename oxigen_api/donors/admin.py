from django.contrib import admin
from django.db.models import Sum, Count
from . import models


@admin.register(models.Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Donor._meta.get_fields()]
    search_fields = ["name"]
    list_filter = ["campaign"]
    list_filter = ["is_company", "is_anonym", "display"]

    def save_model(self, request, obj, form, change):
       super().save_model(request, obj, form, change)
       campaign = models.Campaign.objects.last()
       stats = models.Donor.objects.aggregate(amount=Sum('amount'), count=Count('id'))
       print(stats)
       campaign.amount_collected = stats['amount']
       campaign.donations = stats['count']
       campaign.save()

@admin.register(models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = [
        "name", "target", "amount_collected", "donations", "display"]
    search_fields = ["name"]
    list_filter = ["display"]


@admin.register(models.Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Expense._meta.get_fields()]
    search_fields = ["name"]
    list_filter = ["display"]


@admin.register(models.Need)
class NeedAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Need._meta.get_fields()]
    search_fields = ["name"]
    list_filter = ["display"]


@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Partner._meta.get_fields()]
    # list_display = ["name", "campaign", "logo", "comment"]
    list_filter = ["partner_type", "display"]
    search_fields = ["name"]


@admin.register(models.Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Quote._meta.get_fields()]
    search_fields = ["name"]
    list_filter = ["display"]


@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.FAQ._meta.get_fields()]
    list_filter = ["display"]


@admin.register(models.CovidStats)
class CovidStatsAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.CovidStats._meta.get_fields()]


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Document._meta.get_fields()]
