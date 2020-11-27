from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from oxigen_api.donors.api import views

# if settings.DEBUG:
#     router = DefaultRouter()
# else:
router = DefaultRouter()

router.register("dashboard", views.DashboardViewSet, basename='dash')
router.register("campaigns", views.CampaignViewSet)
router.register("donors", views.DonorViewSet, 'donor')
router.register("named-donors", views.NamedDonorViewSet, 'named-donor')
router.register("expenses", views.ExpenseViewSet)
router.register("partners", views.PartnerViewSet)
router.register("quotes", views.QuoteViewSet)
router.register("needs", views.NeedViewSet)


app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]
