from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAdditionalDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Users Additional Information")
        verbose_name_plural = ("Users Additional Information")
        ordering = ("-timestamp",)

    def __str__(self):
        return f"{self.user.first_name} {self.user.first_name} Additional Info."