from django.db import models
from django.utils.translation import gettext_lazy as _
from  django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), blank=False,unique=True)
    
    REQUIRED_FIELDS = ["email","first_name","last_name"]

