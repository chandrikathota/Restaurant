from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name='home.html'
class User_catalogView(TemplateView):
    template_name='user_catalog.html'
class Order_statusView(TemplateView):
    template_name='order_status.html'
class AboutUsView(TemplateView):
    template_name='about.html'
class AdminLoginView(TemplateView):
    template_name='adminlogin.html'
class AdminSignupView(TemplateView):
    template_name='adminsignup.html'