from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
# from phonenumber_field.modelfields import PhoneNumberField
from .managers import OrganizationHeadManager


class OrganizationHead(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(verbose_name="Email",
                              unique=True, null=False, blank=False)
    title = models.CharField(
        verbose_name="Organization Name", max_length=40, unique=True, null=False, blank=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=13, validators=[
                             phone_regex], blank=True)

    # phone = PhoneNumberField(verbose_name="Phone", blank=True)
    description = models.TextField(verbose_name="Describe your Organization")
    url = models.URLField(verbose_name="Organization URL",
                          null=True, blank=True, default=None)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = OrganizationHeadManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['title', ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True
