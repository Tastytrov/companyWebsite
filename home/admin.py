from django.contrib import admin
from .models import Gallery, Menu, OffMenu, WeeklyDeal, TastyTrovChef, Testimonial

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    #fields = ["post_title", "post_image", "post_content", "meta_description", "category"]
    list_display = ("first_name", "last_name", "tradeType", "albumSerialNumber", "timestamp")
    list_filter = ("timestamp", "lga", "bankName",)
    search_fields = ("first_name", "last_name", "accountNumber", "phoneNumber")
admin.site.register(Gallery)


class MenuAdmin(admin.ModelAdmin):
    #fields = ["post_title", "post_image", "post_content", "meta_description", "category"]
    list_display = ("meal_name", "meal_amount", "available")
    list_editable = ("available",)
admin.site.register(Menu, MenuAdmin)


admin.site.register(OffMenu)


admin.site.register(WeeklyDeal)


admin.site.register(TastyTrovChef)


admin.site.register(Testimonial)