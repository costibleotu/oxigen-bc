from django.db.models import (
    Model,
    CharField,
    TextField,
    IntegerField,
    FloatField,
    BooleanField,
    ForeignKey,
    ImageField,
    DateTimeField,
    CASCADE
)
from django.utils.translation import gettext_lazy as _


class Campaign(Model):
    name = CharField(max_length=255)
    target = FloatField(default=0)
    amount_collected = FloatField(default=0)
    donations = IntegerField(default=0)
    display = BooleanField(default=True)

    def percent(self):
        if self.amount_collected:
            return self.amount_collected / self.target
        return '-'

    def __str__(self):
        return self.name


class Donor(Model):
    name = CharField(_("Name of Donor"), blank=True, max_length=255)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    display_name = CharField(_("Display Name"), blank=True, max_length=255)
    amount = IntegerField()
    comment = TextField(null=True, blank=True)
    is_company = BooleanField(default=False)
    display = BooleanField(default=True)
    date_added = DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.name


class Expense(Model):
    name = CharField(max_length=255, null=True)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    supplier = CharField(max_length=255, null=True)
    document = CharField(max_length=255, null=True)
    status = CharField(max_length=255, null=True)
    amount = FloatField(default=0)
    comment = TextField(null=True, blank=True)
    display = BooleanField(default=True)

    def __str__(self):
        return self.name


class Need(Model):
    name = CharField(max_length=255, null=True)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    quantity = FloatField(default=0)
    stock = FloatField(default=0)
    supplier = CharField(max_length=255, null=True)
    comment = TextField(null=True, blank=True)
    display = BooleanField(default=True)

    def __str__(self):
        return self.name


class Partner(Model):
    name = CharField(max_length=255, null=True)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    logo = ImageField(upload_to="logos", null=True)
    comment = TextField(null=True, blank=True)
    display = BooleanField(default=True)

    def __str__(self):
        return self.name


class Quote(Model):
    name = CharField(max_length=255, null=True)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    comment = TextField(null=True, blank=True)
    display = BooleanField(default=True)

    def __str__(self):
        return self.name
