from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from oxigen_api.donors.api.views import (
    CampaignViewSet,
    NamedDonorViewSet,
    DonorViewSet,
    ExpenseViewSet,
    PartnerViewSet,
    QuoteViewSet,
    NeedViewSet,
    )

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("campains", CampaignViewSet)
router.register("donors", DonorViewSet)
router.register("named-donors", NamedDonorViewSet)
router.register("expenses", ExpenseViewSet)
router.register("partners", PartnerViewSet)
router.register("quotes", QuoteViewSet)
router.register("needs", NeedViewSet)


app_name = "api"
urlpatterns = router.urls
