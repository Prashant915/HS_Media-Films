from django.contrib import admin
from .models import *
from django.utils.html import mark_safe

class Products(admin.ModelAdmin):
      list_display=('Product_image','id',"Product_Name","Catagory","Youtube_Link","Best_seller")
      def Product_image(self,obj):
            return mark_safe(f'<img src="/media/{obj.Image}" width="150" height="120"/>')

admin.site.register(Show_Products,Products)

class PosetImageAdmin(admin.ModelAdmin):
      list_display=('post','Product_image')

      def Product_image(self,obj):
            return mark_safe(f'<img src="/media/{obj.Image}" width="150" height="120"/>')

admin.site.register(Product_images,PosetImageAdmin)

class Banner_Image(admin.ModelAdmin):
      list_display=('Choose_Banner_For','Banner_image')

      def Banner_image(self,obj):
            return mark_safe(f'<img src="/media/{obj.Image}" width="200" height="120"/>')
admin.site.register(Banner,Banner_Image)
