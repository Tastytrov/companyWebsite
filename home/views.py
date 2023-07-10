from django.shortcuts import render, redirect
from django.views import View
from .models import Gallery, Menu, OffMenu, TastyTrovChef, Testimonial, WeeklyDeal
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        deals = WeeklyDeal.objects.filter(active=True).order_by("deal_day")
        team = TastyTrovChef.objects.all()[:4]
        testimonial = Testimonial.objects.filter(approved=True).order_by("-timestamp")
        context = {
            "deals":deals,
            "team":team,
            "testimonial":testimonial
        }
        return render(request, "home/index-trove.html", context)


class GalleryView(View):
    def get(self, request, *args, **kwargs):
        all_uploads = Gallery.objects.all().order_by("-timestamp")
        context = {
            "all_uploads":all_uploads
        }
        return render(request, "home/gallery.html", context)
    

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/contact.html")
    
    def post(self, request, *args, **kwargs):
        return redirect("home:contact_view")
    

class TestimonialView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/review.html")
    
    def post(self, request, *args, **kwargs):
        return redirect("home:review_view")
    

class MenuView(View):
    def get(self, request, *args, **kwargs):
        available_food = Menu.objects.filter(available=True).order_by("meal_name")
        offmenu_food = OffMenu.objects.all().order_by("meal_name")
        context = {
            "available_food":available_food,
            "offmenu_food":offmenu_food
        }
        return render(request, "home/menu.html", context)
    

# Get details of the off menu meal 
class MealDetailView(View):
    def post(self, request, *args, **kwargs):
        food_id = request.POST.get("meal_id")
        print(food_id)
        try:
            offmenu_food_detail = OffMenu.objects.get(id=food_id)
            data = {
                "success": True,
                "food_detail": {
                    "id": offmenu_food_detail.id,
                    "meal_name": offmenu_food_detail.meal_name,
                    "meal_amount": offmenu_food_detail.meal_amount,
                    "meal_description": offmenu_food_detail.meal_description,
                    "estimated_time": offmenu_food_detail.estimated_time,
                }
            }
        except OffMenu.DoesNotExist:
            data = {
                "success": False,
                "message": "Food not found."
            }

        return JsonResponse(data)



class RevservationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/reservation.html")
    


class ConfirmOffMenuView(LoginRequiredMixin, View):
    #redirected here once paystack payment for off-menu meal is successful
    def get(self, request, *args, **kwargs):
        return render(request, "home/offmenu-successful.html")
    
    def post(self, request, *args, **kwargs):
        meal_id = int(request.POST.get("meal_id"))
        try:
            offmenu_food_detail = OffMenu.objects.get(id=meal_id)
            data = {
                "offmenu_food_detail":offmenu_food_detail
            }
        except OffMenu.DoesNotExist:
            data = {
                "offmenu_food_detail":None
            }
        return render(request, "home/offmenu-confirmation.html", data)
    
    
    
class ConfirmRevservationView(LoginRequiredMixin, View):
    #redirected here once paystack payment for reservation is successful
    def get(self, request, *args, **kwargs):
        return render(request, "home/reservation-successful.html")

    def post(self, request, *args, **kwargs):
        resdate = request.POST.get("resdate")
        restime = request.POST.get("restime")
        respurpose = request.POST.get("respurpose")
        numperson = request.POST.get("numperson")
        print(resdate)
        print(restime)
        print(respurpose)
        print(numperson)
        if respurpose == "Birthday Party":
            pay = 1500
        else:
            pay = 0
        context = {
            "resdate":resdate,
            "restime":restime,
            "respurpose":respurpose,
            "numperson":numperson,
            "pay":pay
        }
        return render(request, "home/reservation-confirmation.html", context)
    