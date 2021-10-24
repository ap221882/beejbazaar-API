from django.contrib import admin

from .models import Product,SeedItem,Seller,Sold,SubCategory,CategorySeed
# Register your models here.
admin.site.register(Product)
admin.site.register(SeedItem)
admin.site.register(Seller)
admin.site.register(Sold)
admin.site.register(SubCategory)
admin.site.register(CategorySeed)
