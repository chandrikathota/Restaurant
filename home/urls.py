from django.urls import path
from . import views

urlpatterns=[
    path('', views.HomePageView.as_view(),name='home'),
    path('user_catalog/', views.User_catalogView.as_view(),name='user_catalog'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminhome/orderdetails',views.OrderDetails.as_view(),name='orderdetails'),
    path('usercatalog/order_status/',views.Order_statusView.as_view(),name='order_status'),
    path('user_catalog/about',views.AboutUsView.as_view(),name='about'),
]