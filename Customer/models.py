from django.db import models
from django.utils.html import format_html
# Create your models here.
class Subscribed_Customer_email(models.Model):
    Email=models.EmailField()

class Customer_Enqirie(models.Model):
    Name=models.CharField(max_length=20,blank=False)
    Email=models.EmailField()
    Phone_Number=models.CharField(max_length=12,null=False,blank=False)
    subject=models.CharField(max_length=50)
    Message=models.TextField(max_length=150)

class DemoModel(models.Model):
    @property
    def semantic_autocomplete(self):
        html = self.get_img()
        return format_html(html)