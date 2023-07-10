from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Product(models.Model):
    meal_name = models.CharField(max_length=100)
    meal_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.meal_name


class ProductImage(models.Model):
    meal = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='product_images')
    image = CloudinaryField('file')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.meal.meal_name}"


class ProductReview(models.Model):
    meal = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.meal.meal_name}"