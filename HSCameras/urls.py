"""
URL configuration for HSCameras project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from Add_Products import views
from Customer import views as viewss


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('camera/',views.Camera,name='camerapage'),
    path('Audio/',views.Audio,name='audio'),

    path('Lights/',views.Lights,name='lights'),
    path('Lensesandgrid/',views.Lensesgrid,name="lensesgrid"),
    path('ringsandgrips/',views.ringsandgrips,name="ringsandgrips"),
    path('filter/',views.filter,name="filter"),

    # path('Accessories/',views.Accessories,name="accessories"),
    path('videoproduction/',views.videoproduction,name="videoproduction"),
    path('livestream/',views.livestream,name="livestream"),
    path('product/<int:productid>',views.singleproduct,name="product"),
    
    path('delete/<int:cart_item_id>',views.remove_from_cart,name="deleteitem"),
    path('addcart/<int:product_id>',views.add_cart,name="addcart"),
    path('cart/',views.wishlist,name="wishlist"),
    path('about/',views.about,name="about"),

    path('questions/',views.questions,name="questions"),
    path('contact/',viewss.contact,name="contact"),
    path('enquire/',views.sending_mail,name="sending_mail"),
    path('tinymce/', include('tinymce.urls')),
    path('email/',viewss.email,name="email")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "HS Cameras Admin Portal"
admin.site.site_title = "HS Cameras Admin Portal"
admin.site.index_title = "Welcome to HS Cameras Admin Portal"