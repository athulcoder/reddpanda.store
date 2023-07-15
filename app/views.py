from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from . models import Customer, Product, Cart, OrderPlaced
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from  django.contrib import messages

class ProductView(View):
 def get(self, request):
  topwear = Product.objects.filter(category='TW')
  bottomwear = Product.objects.filter(category='BW')
  footwear = Product.objects.filter(category='FW')
  digital = Product.objects.filter(category='D')
  home = Product.objects.filter(category='H')
  new = Product.objects.filter(category='N')
  

  return render(request, 'app/index.html',{'topwear':topwear, 'bottomwear':bottomwear, 'footwear':footwear, 'digital':digital,'home':home,'new':new})


# def home(request):
#  return render(request, 'app/index.html')


class SingleProductDetailView(View):
  def get(self, request, pk):
   product = Product.objects.get(pk=pk)
   return render(request, 'app/sproduct.html', {'product':product})

# def product_detail(request):
#  return render(request, 'app/sproduct.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def logout_(request):
 logout(request)
 return redirect('home')


def logout_view(request):
 return render(request, 'app/logout.html' )


def account_info(request):
 return render(request, 'app/account_info.html')


def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')



def address(request):
  if request.method=="POST":
    user = request.user
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    city = request.POST.get('city')
    pincode = request.POST.get('pincode')
    state = request.POST.get('state')
    locality = request.POST.get('locality')
    address = request.POST.get('address')
    landmark = request.POST.get('landmark')
    alt_phone = request.POST.get('alt_phone')
    
    costumer = Customer(locality=locality,name=name, user=user,mobile_number=phone,city=city,pincode=pincode,state=state,address=address,landmark=landmark,other_mobile_number=alt_phone)
    costumer.save()

    return redirect('address')
  return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login_(request):
    if request.method=='POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request,username=username, password=password)
      if user is not None:
       login(request, user)
       return redirect('home')

    return render(request, 'app/login.html')

def customerregistration(request):
 if request.method=='POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email  = request.POST.get('email')
    password1  = request.POST.get('password1')
    password2  = request.POST.get('password2')

    if password1==password2:
      messages.success(request, "Congratulations!! Account created successfully")
      my_user = User.objects.create_user(email,email, password1)
      my_user.first_name = first_name
      my_user.last_name = last_name
      my_user.save()
      login(request, my_user)

      return redirect('home')
  
 return render(request, 'app/customerregistration.html')


def checkout(request):
 return render(request, 'app/checkout.html')

def shop(request):
 return render(request, 'app/shop.html')

def category(request):
 return render(request, 'app/category.html')