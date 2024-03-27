from django.shortcuts import render,redirect
from .models import *
from Add_Products.models import *
# Create your views here.
def contact(request):
    allmsg=None
    cart_items=None
    if 'cart_id' in request.session:
        cart_items = Cart.objects.get(pk=request.session['cart_id']).cartitem_set.all()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=Customer_Enqirie(Name=name,Email=email,Phone_Number=phone,subject=subject,Message=message)
        data.save()
        allmsg={
            "Thankyou":"Thankyou! We will Reach You Soon..."
        }
        return render(request,'contact.html',{'cart_items': cart_items,'msg':allmsg})
    banner=Banner.objects.get(Choose_Banner_For='Contact')
    return render(request,'contact.html',{'banner':banner,'cart_items': cart_items})

def email(request):
    if request.method=="POST":
        email=request.POST.get("digemail")
        result=Subscribed_Customer_email(Email=email)
        result.save()
        return redirect('/')
    return render(request,'footer.html')