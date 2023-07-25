import statistics
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.SingleProductDetailView.as_view(), name='product-detail'),

    path('cart/', views.show_my_cart, name='show_my_cart'),
    path('empty/', views.empty_cart, name='empty_cart'),
    path('remove/<int:uid>', views.remove_cart_item, name='remove_cart_item'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('buy/', views.buy_now, name='buy-now'),
    # path('category/', views.category, name='category'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    
    path('add_address_once/', views.add_address_once, name='add_address_once'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login_, name='login'),
    path('signup/', views.signup, name='signup'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop/',views.shop, name='shop'),
    path('add_address/',views.addAddressFromCheckout, name='add_address'),
    path('edit/address/<int:ck>',views.edit_address, name='edit'),
    path('delete/address/<int:ck>',views.delete_address, name='delete_address'),
    path('increase_quantity/<int:cartId>', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cartId>', views.decrease_quantity, name='decrease_quantity'),
    path('logout/',views.logout_, name='logout'),
    path('logout_account/',views.logout_view, name='logout_view'),
    path('profile_info/',views.account_info, name='account_info'),
    path('handlerequest/',views.handleRequest, name='handlerequest'),


    path('digital/',views.category_digital, name='digital'),
    path('bottomwear/',views.category_bottomwear, name='bottomwear'),
    path('topwear/',views.category_topwear, name='topwear'),
    path('homie/',views.category_homie, name='homie'),
    path('fashion/',views.category_fashion, name='fashion'),
    path('arrivals/',views.category_arrivals, name='arrivals'),



] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

