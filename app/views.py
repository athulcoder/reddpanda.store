from django.shortcuts import render
from django.views import View
from . models import Customer, Product, Cart, OrderPlaced

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

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

def shop(request):
 return render(request, 'app/shop.html')

def category(request):
 return render(request, 'app/category.html')