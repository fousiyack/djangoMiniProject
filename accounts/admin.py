from django.contrib import admin
from . models import Product,Offers


# admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_display=('name','price')
class OfferAdmin(admin.ModelAdmin):
    list_display=('code','discount')
    
admin.site.register(Product,ProductAdmin)  
admin.site.register(Offers,OfferAdmin)  

