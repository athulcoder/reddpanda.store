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
   all_products =  Product.objects.filter(category=product.category)
  

   return render(request, 'app/sproduct.html', {'product':product,'all_products':all_products})

# def product_detail(request):
#  return render(request, 'app/sproduct.html')

def show_my_cart(request):
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

  address_added = Customer.objects.filter(user=request.user)

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
  return render(request, 'app/address.html',{'address_added':address_added})

def edit_address(request,ck):
  address = Customer.objects.get(id=ck)

  if request.method=="POST":
    address.name = request.POST.get('name')
    address.phone = request.POST.get('phone')
    address.city = request.POST.get('city')
    address.pincode = request.POST.get('pincode')
    address.address = request.POST.get('address')
    address.state = request.POST.get('state')
    address.landmark = request.POST.get('landmark')
    address.locality = request.POST.get('locality')
    address.alt_phone = request.POST.get('alt_phone')
    address.save()
    return redirect('address')
  return render(request, 'app/address_edit.html',{'address':address})

def delete_address(request,ck):
  address = Customer.objects.get(id=ck)
  address.delete()
  return redirect('address')
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
  else:
    
    return render(request, 'app/login.html')

def customerregistration(request):
  if request.method=='POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email  = request.POST.get('email')
    password1  = request.POST.get('password1')
    password2  = request.POST.get('password2')

    if password1==password2 and '@' in email and '.' in email:
      messages.success(request, "Congratulations!! Account created successfully")
      my_user = User.objects.create_user(email,email, password1)
      my_user.first_name = first_name
      my_user.last_name = last_name
      my_user.save()
      login(request, my_user)

      return redirect('home')
    elif '@' not in email or '.' not in email:
      messages.error(request, 'Invalid Email Entered')
    else:
      messages.error(request, "Passwords doesn't match !")
  
  return render(request, 'app/customerregistration.html')


def checkout(request):
  return render(request, 'app/checkout.html')

def shop(request):
  topwear = Product.objects.filter(category='TW')
  bottomwear = Product.objects.filter(category='BW')
  footwear = Product.objects.filter(category='FW')
  digital = Product.objects.filter(category='D')
  home = Product.objects.filter(category='H')
  new = Product.objects.filter(category='N')
  
  return render(request, 'app/shop.html',{'topwear':topwear, 'bottomwear':bottomwear, 'footwear':footwear, 'digital':digital,'home':home,'new':new})


def category(request):
  return render(request, 'app/category.html')