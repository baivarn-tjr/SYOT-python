from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password as check_hashed_password

class Applicant(models.Model):
    prefix = models.CharField(      max_length = 15)
    username = models.CharField(    max_length=50,
                                    unique=True)

    tel = models.CharField(         max_length = 15)
    email = models.EmailField()
    hashed_password = models.CharField(    max_length = 130,
                                            blank=True)
    def __str__(self):
        return "%s %s %s (%s)" % (   self.prefix,
                                    self.username,
                                    self.tel,
                                    self.email)

    @staticmethod
    def find_by_username(username):
        try:
            applicant = Applicant.objects.get(username=username)
            return applicant
        except Applicant.DoesNotExist:
            return None

    def set_password(self, password):
        self.hashed_password = make_password(password)

    def check_password(self, password):
        return check_hashed_password(password, self.hashed_password)
