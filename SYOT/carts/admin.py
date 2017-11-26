from django.contrib import admin
from .models import Basket,  CompanyMoney ,PaymentHistory

admin.site.register(Basket)
admin.site.register(CompanyMoney)
admin.site.register(PaymentHistory)
