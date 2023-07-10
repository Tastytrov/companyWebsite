from django.db import models
from cloudinary.models import CloudinaryField
import magic

# Create your models here.

CAT = (
    ("Delights","Food and Drinks"),
    ("Atmosphere","Ambiance and Decor"),
    ("Culinary","Chef and Kitchen"),
    ("Celebrations","Events and Special Occasions"),
    ("Alfresco","Outdoor Dining and Patio"),
    ("Hospitality","Team and Staff"),
    ("Capture","Dining Experience"),
)
class Gallery(models.Model):
    file = CloudinaryField('file')
    #file = models.FileField()
    file_type = models.CharField(max_length=255, null=True, blank=True, editable=False)
    category = models.CharField(max_length=255, choices=CAT)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("TastyTrov Gallery")
        verbose_name_plural = ("TastyTrov Gallery")
        ordering = ("-timestamp",)

    def __str__(self):
        return f"{self.timestamp} - {self.file_type}"
    
    def save(self, *args, **kwargs):
        # Check the file type before saving
        if self.file:
            mime_type = magic.from_buffer(self.file.read(), mime=True)
            if 'video' in mime_type:
                self.file_type = 'video'
            elif 'image' in mime_type:
                self.file_type = 'image'
            else:
                self.file_type = 'unknown'

        super().save(*args, **kwargs)



class Menu(models.Model):
    meal_image = CloudinaryField('image')
    #meal_image = models.ImageField()
    meal_name = models.CharField(max_length=255)
    meal_description = models.CharField(max_length=255, blank=True, null=True)
    meal_amount = models.FloatField()
    available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("TastyTrov Menu")
        verbose_name_plural = ("TastyTrov Menu")
        ordering = ("meal_name",)

    def __str__(self):
        if self.available == True:
            return f"{self.meal_name} - Available"
        else:
            return f"{self.meal_name} - Unavailable"
        

ET = (
    ("30 Minutes","30 Minutes"),
    ("45 Minutes","45 Minutes"),
    ("1 Hour","1 Hour"),
    ("3 Hours","3 Hours"),
)
class OffMenu(models.Model):
    meal_name = models.CharField(max_length=255)
    meal_description = models.CharField(max_length=255, blank=True, null=True)
    meal_amount = models.FloatField()
    estimated_time = models.CharField(max_length=255, choices=ET)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("TastyTrov Off Menu")
        verbose_name_plural = ("TastyTrov Off Menu")
        ordering = ("meal_name",)

    def __str__(self):
        return f"{self.meal_name}"
    

DAYS = (
    ("Monday","Monday"),
    ("Tuesday","Tuesday"),
    ("Wednesday","Wednesday"),
    ("Thursday","Thursday"),
    ("Friday","Friday"),
    ("Saturday","Saturday"),
    ("Sunday","Sunday"),
)
class WeeklyDeal(models.Model):
    deal_day = models.CharField(max_length=50, choices=DAYS, unique=True)
    meal_name = models.CharField(max_length=50)
    meal_meta = models.CharField(max_length=50, blank=True, null=True)
    meal_amount = models.FloatField()
    meal_discount_amount = models.FloatField()
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Weekly Deals")
        verbose_name_plural = ("Weekly Deals")
        ordering = ("deal_day",)

    def __str__(self):
        return f"{self.deal_day} Deal"


class TastyTrovChef(models.Model):
    chef_image = CloudinaryField('image')
    #chef_image = models.ImageField()
    chef_first_name = models.CharField(max_length=255)
    chef_last_name = models.CharField(max_length=255)
    chef_bio = models.TextField()
    chef_facebook_profile_link = models.URLField(blank=True, null=True)
    chef_twitter_profile_link = models.URLField(blank=True, null=True)
    chef_instagram_profile_link = models.URLField(blank=True, null=True)
    chef_linkedin_profile_link = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Tasty Trov Chefs")
        verbose_name_plural = ("Tasty Trov Chefs")
        ordering = ("chef_first_name",)

    def __str__(self):
        return f"{self.deal_day} Deal"


class Testimonial(models.Model):
    client_first_name = models.CharField(max_length=255)
    client_last_name = models.CharField(max_length=255)
    testimonial = models.TextField()
    star_rating = models.IntegerField()
    client_social = models.URLField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Testimonials")
        verbose_name_plural = ("Testimonials")
        ordering = ("-timestamp",)

    def __str__(self):
        return f"{self.client_first_name} {self.client_last_name} Testimony"
    
    