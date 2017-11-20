from django.db import models
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password as check_hashed_password

class Applicant(models.Model):
    ACTIVE_TYPE = (
        ('AC', 'Active'),
        ('CL', 'Closed'),
        ('WT', 'Waiting'),
    )
    RESET_TYPE = (
        ('RS', 'Reset'),
        ('CL', 'Closed'),
    )
    # username = models.CharField(    max_length=50,
    #                                 unique=True)
    #
    # tel = models.CharField(         max_length = 15)
    # email = models.EmailField()
    # hashed_password = models.CharField(    max_length = 130,
    #                                         blank=True)
    is_activated = models.CharField(
        max_length=2,
        choices=ACTIVE_TYPE,
        default='WT'
    )
    reset_password = models.CharField(
        max_length=2,
        choices=RESET_TYPE,
        default='CL'
    )
    username = models.CharField(default=None,max_length=50,unique=True)
    email = models.EmailField(default=None, max_length=128,unique=True)
    firstname = models.CharField(default=None, max_length=128)
    lastname = models.CharField(default=None, max_length=128)
    hashed_password = models.CharField(default=None,max_length=128)
    mobile = models.CharField(default=None,max_length=10)
    address = models.CharField(max_length=512, default=None)
    city = models.CharField(max_length=128, default=None)
    state = models.CharField(max_length=128, default=None)
    zipcode = models.CharField(max_length=5, default=None)

    # def __str__(self):
    #     return "%s %s (%s)" % (    self.username,
    #                                 self.tel,
    #                                 self.email)

    @staticmethod
    def find_by_username(username):
        try:
            applicant = Applicant.objects.get(username=username)
            return applicant
        except Applicant.DoesNotExist:
            return None

    def find_by_email(email):
        try:
            applicant = Applicant.objects.get(email=email)
            return applicant
        except Applicant.DoesNotExist:
            return None

    def set_password(self, password):
        self.hashed_password = make_password(password)

    def check_password(self, password):
        return check_hashed_password(password, self.hashed_password)
