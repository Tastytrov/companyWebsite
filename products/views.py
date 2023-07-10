from django.shortcuts import render
from django.views import View
from .models import Product

# Create your views here.

class ShopView(View):
     def get(self, request, *args, **kwargs):
         all_product = Product.objects.filter(available=True).order_by("-timestamp")
         context = {
              "all_product":all_product
         }
         return render(request, "products/shop.html", context)