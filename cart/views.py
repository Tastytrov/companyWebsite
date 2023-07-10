from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Cart, CartItem
from products.models import Product
from django.views import View

# Create your views here.

class AddToCartView(View):
    def get(self, request,  PRODUCT_ID, *args, **kwarg):
        product = get_object_or_404(Product, id=PRODUCT_ID)
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Check if the item is already in the cart
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        # Increment the quantity if the item is already in the cart
        if not item_created:
            cart_item.quantity += 1
            cart_item.save()
        
        # Redirect the user back to the product details page or any desired page
        return redirect('product_details', PRODUCT_ID=product.id)
