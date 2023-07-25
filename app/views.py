from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.views import View
from . models import Customer, Product, Cart, OrderPlaced
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

class ProductView(View):
    def get(self, request):
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        footwear = Product.objects.filter(category='FW')
        digital = Product.objects.filter(category='D')
        home = Product.objects.filter(category='H')
        new = Product.objects.filter(category='N')

        return render(request, 'app/index.html', {'topwear': topwear, 'bottomwear': bottomwear, 'footwear': footwear, 'digital': digital, 'home': home, 'new': new})


# def home(request):
#  return render(request, 'app/index.html')


class SingleProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        all_products = Product.objects.filter(category=product.category)
        cart = ''
        try:
            cart = Cart.objects.get(user=request.user, product=product)
        except:
            print('hello')
        return render(request, 'app/sproduct.html', {'product': product, 'all_products': all_products, 'cart': cart},)

# def product_detail(request):
#  return render(request, 'app/sproduct.html')


def show_my_cart(request):

    if request.user.is_authenticated:
        cartItems = Cart.objects.filter(user=request.user)
        if cartItems:
            amount = 0.0
            shipping_amount = 40
            total_amount = 0.0
            cart_product = [
                p for p in Cart.objects.all() if p.user == request.user]

            if cart_product:
                for p in cart_product:
                    temp_amount = (p.quantity * p.product.discounted_price)
                    amount += temp_amount
                    total_amount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'cart': cartItems, 'total_amount': total_amount, 'amount': amount, 'shipping_amount': shipping_amount})
        else:
            return redirect('empty_cart')
    else:
        return render(request, 'app/404.html')


def empty_cart(request):
    if request.user.is_authenticated:
        return render(request, 'app/empty.html')
    else:
        return render(request, 'app/404.html')

def remove_cart_item(request, uid):
    if request.user.is_authenticated:
        Cart.objects.get(id=uid).delete()
        return redirect('show_my_cart')
    else:
        return render(request, 'app/404.html')

def add_to_cart(request, pk):
    if request.user.is_authenticated:
        try:
            user = request.user
            product = Product.objects.get(pk=pk)
            try:
                current_cart = Cart.objects.get(user=user, product=product)
                if current_cart:
                    print('nothing is here')
            except:
                cart = Cart(user=user, product=product)
                cart.save()
            result = "Item successfully added to your cart"
        except Exception as e:
            result = str(e)
    else:
        result = "Please sign in"
        # return render(request, 'app/login.html')
    return HttpResponse(result)

def logout_(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return render(request, 'app/404.html')

def logout_view(request):
    if request.user.is_authenticated:
        return render(request, 'app/logout.html')
    else:
        return render(request, 'app/404.html')

def account_info(request):
    if request.user.is_authenticated:
        return render(request, 'app/account_info.html')
    else:
        return render(request, 'app/404.html')

def buy_now(request):
    if request.user.is_authenticated:
        return render(request, 'app/buynow.html')
    else:
        return render(request, 'app/404.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'app/profile.html')
    else:
        return render(request, 'app/404.html')

def address(request):

    if request.user.is_authenticated:
        address_added = Customer.objects.filter(user=request.user)
        if request.method == "POST":
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

            
            costumer = Customer(locality=locality, name=name, user=user, mobile_number=phone, city=city,
                                pincode=pincode, state=state, address=address, landmark=landmark, other_mobile_number=alt_phone)
            costumer.save()
            print(request.POST.get('checkout'))
            if request.POST.get('checkout') =="True":
                print('HEllo word')
                return redirect('checkout')
            return redirect('address')
        return render(request, 'app/address.html', {'address_added': address_added})
    else:
        return render(request, 'app/404.html')


def add_address_once(request):
    if request.user.is_authenticated:
        if request.method == "POST":
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

            
            costumer = Customer(locality=locality, name=name, user=user, mobile_number=phone, city=city,
                                pincode=pincode, state=state, address=address, landmark=landmark, other_mobile_number=alt_phone)
            costumer.save()

            return redirect('checkout')

def edit_address(request, ck):
    
    address = Customer.objects.get(id=ck)

    if request.method == "POST":
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
    return render(request, 'app/address_edit.html', {'address': address})


def delete_address(request, ck):
    if  request.user.is_authenticated:
        address = Customer.objects.get(id=ck)
        address.delete()
        return redirect('address')
    else:
        return render(request, 'app/404.html')

def orders(request):
    if  request.user.is_authenticated:
        return render(request, 'app/orders.html')
    else:
        return render(request, 'app/404.html')

def change_password(request):
    return render(request, 'app/changepassword.html')


def mobile(request):
    return render(request, 'app/mobile.html')


def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'app/login.html',{'message':"User credentials doesn't match!"})
    else:

        return render(request, 'app/login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2 and '@' in email and '.' in email:
            messages.success(
                request, "Congratulations!! Account created successfully")
            my_user = User.objects.create_user(email, email, password1)
            my_user.first_name = first_name
            my_user.last_name = last_name
            my_user.save()
            login(request, my_user)

            return redirect('home')
        elif '@' not in email or '.' not in email:
            messages.error(request, 'Invalid Email Entered')
        else:
            messages.error(request, "Passwords doesn't match !")

    return render(request, 'app/signup.html')


def checkout(request):
    if request.user.is_authenticated:
        address_added = Customer.objects.filter(user=request.user)
        cart = Cart.objects.filter(user=request.user)
        if cart:
            amount = 0.0
            shipping_amount = 40
            total_amount = 0.0
            cart_product = [
                p for p in Cart.objects.all() if p.user == request.user]

            if cart_product:
                for p in cart_product:
                    temp_amount = (p.quantity * p.product.discounted_price)
                    amount += temp_amount
                    total_amount = amount + shipping_amount
            return render(request, 'app/checkout.html', {'cart': cart, 'total': total_amount, 'amount': amount, 'shipping_amount': shipping_amount,'address_added': address_added})
        
    else:
        return render(request, 'app/404.html')


def addAddressFromCheckout(request):
    if request.user.is_authenticated:
        from_checkout = True
        return render(request, 'app/address.html', {'checkout': from_checkout })
def shop(request):
    topwear = Product.objects.filter(category='TW')
    bottomwear = Product.objects.filter(category='BW')
    footwear = Product.objects.filter(category='FW')
    digital = Product.objects.filter(category='D')
    home = Product.objects.filter(category='H')
    new = Product.objects.filter(category='N')

    return render(request, 'app/shop.html', {'topwear': topwear, 'bottomwear': bottomwear, 'footwear': footwear, 'digital': digital, 'home': home, 'new': new})


def category_digital(request):
     topwear = Product.objects.filter(category='TW')
     bottomwear = Product.objects.filter(category='BW')
     footwear = Product.objects.filter(category='FW')
     digital = Product.objects.filter(category='D')
     home = Product.objects.filter(category='H')
     new = Product.objects.filter(category='N')

     return render(request, 'app/template_digital.html', {'topwear': topwear, 'bottomwear': bottomwear, 'footwear': footwear, 'digital': digital, 'home': home, 'new': new})

def category_topwear(request):
     topwear = Product.objects.filter(category='TW')
     bottomwear = Product.objects.filter(category='BW')
     footwear = Product.objects.filter(category='FW')
     digital = Product.objects.filter(category='D')
     home = Product.objects.filter(category='H')
     new = Product.objects.filter(category='N')

     return render(request, 'app/template_digital.html', {'topwear': topwear, 'bottomwear': bottomwear, 'footwear': footwear, 'digital': digital, 'home': home, 'new': new})

def category_bottomwear(request):
     topwear = Product.objects.filter(category='TW')
     bottomwear = Product.objects.filter(category='BW')
     footwear = Product.objects.filter(category='FW')
     digital = Product.objects.filter(category='D')
     home = Product.objects.filter(category='H')
     new = Product.objects.filter(category='N')

     return render(request, 'app/template_digital.html', {'topwear': topwear, 'bottomwear': bottomwear, 'footwear': footwear, 'digital': digital, 'home': home, 'new': new})

def category_fashion(request):
     topwear = Product.objects.filter(category='TW')
     bottomwear = Product.objects.filter(category='BW')
     footwear = Product.objects.filter(category='FW')
     digital = Product.objects.filter(category='D')
     home = Product.objects.filter(category='H')
     new = Product.objects.filter(category='N')

     return render(request, 'app/template_digital.html', {'topwear': topwear, 'bottomwear': bottomwear, 'footwear': footwear, 'digital': digital, 'home': home, 'new': new})

def category_arrivals(request):
     topwear = Product.objects.filter(category='TW')
     bottomwear = Product.objects.filter(category='BW')
     footwear = Product.objects.filter(category='FW')
     digital = Product.objects.filter(category='D')
     home = Product.objects.filter(category='H')
     new = Product.objects.filter(category='N')

     return render(request, 'app/template_arrivals.html', {'topwear': topwear, 'bottomwear': bottomwear, 'footwear': footwear, 'digital': digital, 'home': home, 'new': new})


def category_homie(request):
     topwear = Product.objects.filter(category='TW')
     bottomwear = Product.objects.filter(category='BW')
     footwear = Product.objects.filter(category='FW')
     digital = Product.objects.filter(category='D')
     home = Product.objects.filter(category='H')
     new = Product.objects.filter(category='N')

     return render(request, 'app/template_homie.html', {'topwear': topwear, 'bottomwear': bottomwear, 'footwear': footwear, 'digital': digital, 'home': home, 'new': new})






def increase_quantity(request, cartId):
    if request.method =="GET":
        # prod_id = request.GET['prod_id']
        c = Cart.objects.get(id=cartId)
        if c.quantity <5:
            c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 40
        total_amount = 0.0
        cart_product = [
            p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discounted_price)
                amount += temp_amount
                total_amount = amount + shipping_amount
                
            # data ={
            #     'quantity':c.quantity,
            #     'amount': amount,
            #     'total':total_amount
            # }

            return redirect('show_my_cart')

def decrease_quantity(request, cartId):
    if request.method =="GET":
        # prod_id = request.GET['prod_id']
        c = Cart.objects.get(id=cartId)

        if c.quantity >1:
            c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 40
        total_amount = 0.0
        cart_product = [
            p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discounted_price)
                amount += temp_amount
                total_amount = amount + shipping_amount
                
            # data ={
            #     'quantity':c.quantity,
            #     'amount': amount,
            #     'total':total_amount
            # }

            return redirect('show_my_cart')
        
        
@csrf_exempt
def handleRequest(request):
    # Paytm will send post request
    pass