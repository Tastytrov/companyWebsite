from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserAdditionalDetail

# Create your views here.

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/register.html")

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        password = request.POST.get("password")
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with the email already exist")
            return redirect("accounts:register_view")
        else:
            if len(password) > 7:
                l, u, s, d = 0, 0, 0, 0
                for i in password:
                    if (i.islower()):
                        l += 1
                    if (i.isupper()):
                        u += 1
                    if (i.isdigit()):
                        d += 1
                    if (i=="!" or i=="@" or i=="#" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")" or i=="-" or i=="_" or i=="+" or i=="=" or i=="{" or i=="}" or i=="[" or i=="]" or i=="|" or i=="\\" or i=="<" or i==">" or i=="?" or i=="/"):
                        s += 1
                print(l, u, s, d, l+s+u+d, len(password))
                if (l>=1 and u>=1 and s>=1 and d>=1 and l+s+u+d==len(password)):
                    new_user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
                    new_user.save()
                    new_additional_detail = UserAdditionalDetail.objects.get(user=new_user)
                    new_additional_detail.address = address
                    new_additional_detail.phone = phone
                    new_additional_detail.save()
                    return redirect("accounts:login_view")
                else:
                    messages.error(request, "Password must contain atleast 1 Uppercase, 1 lowercase, 1 digit and a special character and at least 8 characters long")
                    return redirect("accounts:register_view")
            else:
                messages.error(request, "Password too short. Your password must contain at least 8 characters.")
        return redirect("accounts:register_view")
        


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/login.html")

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("")
        else:
            return redirect("accounts:login_view")
        