from django.contrib import admin

from .models import Product, ProductCategory, Icon, IconCategory

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Icon)
admin.site.register(IconCategory)
