from django.db.models import (
    Model,
    CharField,
    TextField,
    IntegerField,
    FloatField,
    BooleanField,
    ForeignKey,
    FileField,
    DateTimeField,
    DateField,
    CASCADE,
    URLField
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
    name = CharField(_("Name of Donor"), null=True, blank=True, max_length=255)
    order = IntegerField(default=0)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    display_name = CharField(_("Display Name"), blank=True, max_length=255)
    amount = IntegerField(default=0)
    comment = TextField(null=True, blank=True)
    is_company = BooleanField(default=False)
    logo = FileField(upload_to="logos", null=True, blank=True)
    display = BooleanField(default=True)
    date_added = DateTimeField(null=True, blank=True, auto_now_add=True)
    link = URLField(max_length=200, null=True, blank=True)
    is_anonym = BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.name == "Anonim":
            self.is_anonym = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Expense(Model):
    name = CharField(max_length=255, null=True)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    supplier = CharField(max_length=255, null=True)
    document = CharField(max_length=255, null=True)
    status = CharField(max_length=255, null=True)
    quantity = FloatField(default=0)
    in_use = FloatField(default=0)
    available = FloatField(default=0)
    price = FloatField(default=0)
    comment = TextField(null=True, blank=True)
    display = BooleanField(default=True)

    def __str__(self):
        return self.name


class Need(Model):
    name = CharField(max_length=255, null=True)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    quantity = FloatField(default=0)
    stock = FloatField(default=0)
    price = FloatField(default=0)
    recipient = CharField(max_length=255, null=True, blank=True)
    comment = TextField(null=True, blank=True)
    display = BooleanField(default=True)

    def __str__(self):
        return self.name


class Partner(Model):
    name = CharField(max_length=255, null=True)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    logo = FileField(upload_to="logos", null=True)
    comment = TextField(null=True, blank=True)
    display = BooleanField(default=True)
    link = URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Quote(Model):
    name = CharField(max_length=255, null=True)
    comment = TextField(null=True, blank=True)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    display = BooleanField(default=True)

    def __str__(self):
        return self.name


class FAQ(Model):
    question = TextField()
    answer = TextField()
    order = IntegerField(default=1)
    campaign = ForeignKey(Campaign, on_delete=CASCADE)
    display = BooleanField(default=True)

    def __str__(self):
        return self.question


class CovidStats(Model):
    hospitals_ocupation_rate = IntegerField(default=0)
    new_cases = IntegerField(default=0)
    infection_rate = FloatField(default=0)
    date = DateField(null=True)

    def __str__(self):
        return self.date
