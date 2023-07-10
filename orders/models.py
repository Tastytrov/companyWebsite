from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk}"

    def place_order(self):
        # Perform any order-specific actions or additional processing
        # Update the status, initiate payment processing, etc.
        self.status = 'processing'
        self.save()

    def cancel_order(self):
        # Perform any cancellation-specific actions or additional processing
        # Update the status, restock items, refund payment, etc.
        self.status = 'cancelled'
        self.save()

    def track_order(self):
        # Perform any tracking-specific actions or additional processing
        # Return relevant tracking information (e.g., shipment details, delivery status, etc.)
        return "Order is in transit."



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"OrderItem for {self.order} - {self.product}"

    @property
    def subtotal(self):
        return self.price * self.quantity
