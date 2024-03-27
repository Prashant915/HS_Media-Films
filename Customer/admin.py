from django.contrib import admin
from .models import *
from django.utils.html import mark_safe

class All_Email(admin.ModelAdmin):
      list_display=('id','Email')

class Customer_Info(admin.ModelAdmin):
      list_display=('Name','Email','Phone_Number','subject','Message')
      
admin.site.register(Subscribed_Customer_email,All_Email)
admin.site.register(Customer_Enqirie,Customer_Info)