import statistics
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.SingleProductDetailView.as_view(), name='product-detail'),

    path('cart/', views.show_my_cart, name='cart'),
    # path('cart/', views.add_to_cart, name='cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('category/', views.category, name='category'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login_, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop/',views.shop, name='shop'),
    path('edit/address/<int:ck>',views.edit_address, name='edit'),
    path('delete/address/<int:ck>',views.delete_address, name='delete_address'),
    
    path('logout/',views.logout_, name='logout'),
    path('logout_account/',views.logout_view, name='logout_view'),
    path('profile_info/',views.account_info, name='account_info')
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

