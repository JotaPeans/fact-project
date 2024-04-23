from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

class SignIn(View):
    def get(self,req): 
        if(req.user.is_authenticated): 
            return redirect("feedbackApp:root")

        return render(req, "autenticacao/login.html")
    
    def post(self,req):
        username = req.POST.get("username")
        password = req.POST.get("password")

        USER = auth.authenticate(username = username, password = password)
        if not USER:
            return render(req, 'autenticacao/login.html')
        else:
            auth.login(req, USER)
            return redirect("feedbackApp:root")
