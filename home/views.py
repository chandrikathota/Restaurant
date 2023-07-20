
from urllib import request
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Item
from .models import Order

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout


class HomePageView(TemplateView):
    template_name='home.html'
class User_catalogView(TemplateView):
    extra_context={'items': Item.objects.all(),'orders':Order.objects.all()}
    template_name='user_catalog.html'
    
class Order_statusView(TemplateView,):
    extra_context={'items': Item.objects.all(),'orders':Order.objects.all()}
    template_name='order_status.html'
class AboutUsView(TemplateView):
    template_name='about.html'
class AdminLoginView(TemplateView):
    template_name='adminlogin.html'
class OrderDetailsView(TemplateView):
    template_name='orderdetails.html'

class AdminHomeView(TemplateView):
    template_name='adminhome.html'
    
def adminlogin(request):
    if(request.method=="POST"):
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            login(request,user)
            context ={'orders':Order.objects.all()}
            return render(request,'adminhome.html',context )
        else:
            return redirect('home')
    
    else:
        print("Details not matched")
        return render(request,'adminlogin.html')



    