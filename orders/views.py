from django.shortcuts import render, redirect
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404, redirect
from cart.models import Cart, CartItem
from django.views import View

# Create your views here.

class PlaceOrderView(View):
    def get(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, user=request.user)
        
        # Create a new order instance
        order = Order(user=request.user, total_amount=cart.total_amount)
        order.save()
        
        # Move cart items to order
        for cart_item in cart.items.all():
            order_item = OrderItem(order=order, product=cart_item.product, quantity=cart_item.quantity)
            order_item.save()
        
        # Clear the cart after placing the order
        cart.items.all().delete()
        
        # Redirect the user to an order success or confirmation page
        return redirect('order_success')
