from django.contrib import admin

# Register your models here.
from .models import(
    Customer,
    Product,
    Cart,
    OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =['id','user', 'name','locality','city', 'pincode', 'state','mobile_number','other_mobile_number','address','landmark']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title', 'selling_price','discounted_price', 'description', 'brand','category',]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display =['id','user', 'product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display =['id','user', 'customer','product', 'quantity', 'ordered_date', 'status']
