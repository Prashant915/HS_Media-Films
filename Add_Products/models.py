from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html
from django.core.exceptions import ValidationError

Catagory=(
    ('Camera','Camera'),
    ('Lenses','Lenses'),
    ('Rings & Grips','Rings & Grips'),
    ('Audio','Audio'),
    ('Lights','Lights'),
    ('Filter','Filter'),
    
)

Destination=(
    ('Home Page - Shutter','Home Page - Shutter'),
    ('Home Page - Experience','Home Page - Experience'),
    ('Home Page - Vision','Home Page - Vision'),
    ('Video Production - Shutter','Video Production - Shutter'),
    ('Video Production - Experience','Video Production - Experience'),
    ('Video Production - Vision','Video Production - Vision'),
    ('About','About'),
    ('Frequently Questions','Frequently Questions'),
    ('Contact','Contact')

)
def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
        
class Show_Products(models.Model):
    Image=models.ImageField(blank=False,null=False,default=None,validators=[validate_image],help_text='Maximum file size allowed is 1Mb')
    Product_Name=models.CharField(max_length=50)
    Sub_description=HTMLField(max_length=2000)
    Catagory=models.CharField(max_length=30,choices=Catagory)
    Description=HTMLField(max_length=2000)
    Youtube_Link=models.URLField()
    Sale=models.BooleanField(default=False)
    Best_seller= models.BooleanField(default=False)
    Top_rate=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Product_Name

class Product_images(models.Model):
    post=models.ForeignKey(Show_Products,default=None,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to="Products",validators=[validate_image],help_text='Maximum file size allowed is 1Mb')

class DemoModel(models.Model):
    @property
    def semantic_autocomplete(self):
        html = self.get_img()
        return format_html(html)

class Cart(models.Model):
    items = models.ManyToManyField(Show_Products, through='CartItem')
    
class CartItem(models.Model):
    product = models.ForeignKey(Show_Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

        
class Banner(models.Model):
    Choose_Banner_For=models.CharField(max_length=40,choices=Destination,unique=True)
    Image=models.ImageField(upload_to="Banners",validators=[validate_image],help_text='Maximum file size allowed is 1Mb')
    Title=models.CharField(max_length=30)
    Sub_title=models.CharField(max_length=50)
    link=models.URLField()

    

