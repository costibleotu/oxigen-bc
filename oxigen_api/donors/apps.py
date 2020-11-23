from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DonorsConfig(AppConfig):
    name = "oxigen_api.donors"
    verbose_name = _("Donors")

    # def ready(self):
    #     try:
    #         import oxigen_api.users.signals  # noqa F401
    #     except ImportError:
    #         pass
