from django.contrib import admin
from .models import Product, ProductImage, ProductReview

# Register your models here.

admin.site.register(Product)

admin.site.register(ProductImage)

admin.site.register(ProductReview)