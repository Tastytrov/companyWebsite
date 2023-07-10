from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home_view"),
    path("contact/", views.ContactView.as_view(), name="contact_view"),
    path("gallery/", views.GalleryView.as_view(), name="gallery_view"),
    path("menu/", views.MenuView.as_view(), name="menu_view"),
    path("meal-detail/", views.MealDetailView.as_view(), name="meal_detail_view"),
    path("make-reservation/", views.RevservationView.as_view(), name="reservation_view"),
    path("confirm-reservation/", views.ConfirmRevservationView.as_view(), name="confirm_reservation_view"),
    path("confirm-offmenu-order/", views.ConfirmOffMenuView.as_view(), name="confirm_offmenu_view"),
    path("make-testimonial/", views.TestimonialView.as_view(), name="review_view"),
]