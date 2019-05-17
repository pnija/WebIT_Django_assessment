from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    """ a model for adding client details """
    client_name = models.CharField("Full name", max_length=1024, unique=True)
    street_name = models.CharField("Street name", max_length=1024)
    suburb = models.CharField("Suburb", max_length=1024)
    postcode = models.CharField("Postcode", max_length=6)
    state = models.CharField("State", max_length=1024)
    client_contact_name = models.CharField(unique=True, max_length=1024)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)

    def __str__(self):
        return self.client_name
