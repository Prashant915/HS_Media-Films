from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from .models import *
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from email.mime.image import MIMEImage

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        return (a_set & b_set)
    
def common(request,Product):
    p_id=None
    remove=False
    cart_items=None
    
    if 'cart_id' in request.session:
        cart_items = Cart.objects.get(pk=request.session['cart_id']).cartitem_set.all()
    st=request.GET.get("search")
    if st!=None:
        Product=Show_Products.objects.filter(Product_Name__icontains=st)
    if 'cart_id' in request.session:
        cart = Cart.objects.get(pk=request.session['cart_id'])
        cart_items = cart.cartitem_set.all()
    if cart_items:
        p_id=[i.product.id for i in cart_items]
    product_ids = [product.id for product in Product]
    if p_id and product_ids and common_member(p_id,product_ids):
        remove=list(common_member(p_id,product_ids))
    return(Product,cart_items,remove)

def homepage(request):
    cart_items=None
    new_arrival=Show_Products.objects.order_by('id').reverse()[:10]
    Best_seller=Show_Products.objects.order_by('?')
    top_rate=Show_Products.objects.order_by('?')
    banner1=Banner.objects.get(Choose_Banner_For='Home Page - Shutter')
    banner2=Banner.objects.get(Choose_Banner_For='Home Page - Experience')
    banner3=Banner.objects.get(Choose_Banner_For='Home Page - Vision')
    newarrived,cart_items,remove=common(request,new_arrival)
    result={
        "Product":newarrived,
        "Product2":Best_seller,
        "Product3":top_rate,
        'cart_items': cart_items,
        'banner1':banner1,
        'banner2':banner2,
        'banner3':banner3,
        'remove':remove
    }
    return render(request,'index.html',result)


def Camera(request):
    Product=Show_Products.objects.filter(Catagory="Camera").order_by('?')
    Product,cart_items,remove=common(request,Product)
    return render(request,'Camera.html',{"Product":Product,'cart_items': cart_items,'remove':remove})

def filter(request):
    Product=Show_Products.objects.filter(Catagory="Filter").order_by('?')
    Product,cart_items,remove=common(request,Product)
    return render(request,'Filter.html',{"Product":Product,'cart_items': cart_items,"remove":remove})

def Audio(request):
    Product=Show_Products.objects.filter(Catagory="Audio").order_by('?')
    Product,cart_items,remove=common(request,Product)
    return render(request,'Audio.html',{"Product":Product,'cart_items': cart_items,'remove':remove})

def Lensesgrid(request):
    Product=Show_Products.objects.filter(Catagory="Lenses").order_by('?')
    Product,cart_items,remove=common(request,Product)
    return render(request,'Lensesandgrid.html',{"Product":Product,'cart_items': cart_items,'remove':remove})

def ringsandgrips(request):
    Product=Show_Products.objects.filter(Catagory="Rings & Grips").order_by('?')
    Product,cart_items,remove=common(request,Product)
    return render(request,'ringsandgrips.html',{"Product":Product,'cart_items': cart_items,'remove':remove})

def Lights(request):
    Product=Show_Products.objects.filter(Catagory="Lights").order_by('?')
    Product,cart_items,remove=common(request,Product)
    return render(request,'Lights.html',{"Product":Product,'cart_items': cart_items,'remove':remove})

def videoproduction(request):
    new_arrival=Show_Products.objects.order_by('id').reverse()[:10]
    banner1=Banner.objects.get(Choose_Banner_For="Video Production - Shutter")
    banner2=Banner.objects.get(Choose_Banner_For="Video Production - Experience")
    banner3=Banner.objects.get(Choose_Banner_For="Video Production - Vision")
    newarrived,cart_items,remove=common(request,new_arrival)
    result={
        "banner1":banner1,
        "banner2":banner2,
        "banner3":banner3,
        "newarrival":newarrived,
        'cart_items': cart_items,
        'remove':remove
    }
    return render(request,'videoproduction.html',result)

def livestream(request):
    cart_items=None
    Camera=Show_Products.objects.filter(Catagory="Camera").order_by('?')
    Filter=Show_Products.objects.filter(Catagory="Filter").order_by('?')
    Lenses=Show_Products.objects.filter(Catagory="Lenses").order_by('?')
    if 'cart_id' in request.session:
        cart_items = Cart.objects.get(pk=request.session['cart_id']).cartitem_set.all()
    result={
        'cart_items': cart_items,
        'camera':Camera,
        'filter':Filter,
        'lenses':Lenses
    }
    return render(request,'livestream.html',result)

def about(request):
    cart_items=None
    if 'cart_id' in request.session:
        cart_items = Cart.objects.get(pk=request.session['cart_id']).cartitem_set.all()
    banner=Banner.objects.get(Choose_Banner_For='About')
    return render(request,'about.html',{'cart_items': cart_items,'banner':banner})

def questions(request):
    cart_items=None
    if 'cart_id' in request.session:
        cart_items = Cart.objects.get(pk=request.session['cart_id']).cartitem_set.all()
    question=Frequently_Question.objects.all()
    banner=Banner.objects.get(Choose_Banner_For='Frequently Questions')
    return render(request,'question.html',{'question':question,'cart_items': cart_items,'banner':banner})


def singleproduct(request,productid):
    cart_items=None
    remove=False
    if 'cart_id' in request.session:
        cart_items = Cart.objects.get(pk=request.session['cart_id']).cartitem_set.all()
    result=Show_Products.objects.get(pk=productid)
    img=Product_images.objects.filter(post=productid)
    random=Show_Products.objects.all().order_by('?')
    random2=Show_Products.objects.all().order_by('?')
    if 'cart_id' in request.session:
        cart = Cart.objects.get(pk=request.session['cart_id'])
        cart_items = cart.cartitem_set.all()
        p_id=[i.product.id for i in cart_items]
        if productid in p_id:
            remove=True
    data={
        'result':result,
        'img':img,
        'random':random,
        'random2':random2,
        'cart_items': cart_items,
        'remove':remove
    }
    return render(request,'product.html',data)


def add_cart(request,product_id):
    product = get_object_or_404(Show_Products, pk=product_id)
    
    if 'cart_id' not in request.session:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.get(pk=request.session['cart_id'])
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('wishlist')

def  sending_mail(request):
    cart_items=None
    if 'cart_id' in request.session:
        cart_items = Cart.objects.get(pk=request.session['cart_id']).cartitem_set.all()
    if request.method == "POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        emailid=request.POST.get('email')
        
        if 'cart_id' in request.session:
            cart = Cart.objects.get(pk=request.session['cart_id'])
            cart_items = cart.cartitem_set.all()
            # p_name=[i.product.Product_Name for i in cart_items]
            # p_id=[i.product.id for i in cart_items]
        context={
        'name':name,
        'mobile':mobile,
        'emailid':emailid,
        'data':cart_items
        } 
        subject=f'New Enquiry: from {name}'
        html_message=render_to_string("email.html",context)
        plain_message=strip_tags(html_message)
        # message=f'Thankyou {name} for Enquiry in our site we will connect you soon at {mobile} this number'
        # email_from=settings.EMAIL_HOST
        message=EmailMultiAlternatives(
            subject= subject,
            body=plain_message,
            from_email=None,
            to=['prashantrandiwe@gmail.com']
        )
        message.mixed_subtype = 'related'
        message.attach_alternative(html_message,"text/html")
        message.send()
        # message=f'Customer Email: {emailid} Mobile Number: {mobile} Name: {name} Product Enquired regarding {p_name} having product id {p_id}'
        # email_from=settings.EMAIL_HOST
        # send_mail(subject,message,email_from,['prashantrandiwe@gmail.com'],fail_silently=False)

        subject=f'Thankyou {name} for Reaching Us'
        html_message=render_to_string("customeremail.html",context)
        plain_message=strip_tags(html_message)
        # message=f'Thankyou {name} for Enquiry in our site we will connect you soon at {mobile} this number'
        # email_from=settings.EMAIL_HOST
        message=EmailMultiAlternatives(
            subject= subject,
            body=plain_message,
            from_email=None,
            to=[emailid]
        )
        message.attach_alternative(html_message,"text/html")
        message.send()
        # send_mail(subject,message,email_from,[emailid],fail_silently=False)
        return redirect('/cart/')
    else:
        return render(request,'cart.html',{'cart_items': cart_items})
    
def remove_from_cart(request,cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    if cart_item:
        print(cart_item.id)
    cart_item.delete()
    return redirect('wishlist')

def wishlist(request):
    cart_items=None
    if 'cart_id' in request.session:
        cart = Cart.objects.get(pk=request.session['cart_id'])
        cart_items = cart.cartitem_set.all()
    else:
        cart_items = []
    p_name=[i.product.Product_Name for i in cart_items]
    p_id=[i.product.id for i in cart_items]
    
    return render(request,'cart.html',{'cart_items': cart_items})


# def Accessories(request):
#     cart_items=None
#     Product=Show_Products.objects.filter(Catagory="Studio & Accessories").order_by('?')
#     if 'cart_id' in request.session:
#         cart_items = Cart.objects.get(pk=request.session['cart_id']).cartitem_set.all()
#     st=request.GET.get("search")
#     if st!=None:
#         Product=Show_Products.objects.filter(Product_Name__icontains=st)
#     return render(request,'Accessories.html',{"Product":Product,'cart_items': cart_items})