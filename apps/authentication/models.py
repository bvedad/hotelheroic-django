# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELD = AbstractUser.EMAIL_FIELD
    email = EmailField(_('email address'), unique=True)  # changes email to unique and blank to false
    REQUIRED_FIELDS = ["username"]  # removes email from REQUIRED_FIELDS
