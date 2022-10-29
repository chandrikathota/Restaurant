from django.urls import path
from . import views

urlpatterns=[
    path('', views.HomePageView.as_view(),name='home'),
    path('user_catalog/', views.User_catalogView.as_view(),name='user_catalog'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('orderdetails/adminhome',views.AdminHomeView.as_view(),name='adminhome'),
    path('adminhome/',views.OrderDetailsView.as_view(),name='adminhome'),
    path('adminhome/orderdetails',views.OrderDetailsView.as_view(),name='orderdetails'),
    path('orderdetails/adminhome',views.OrderDetailsView.as_view(),name='adminhome'),
    path('usercatalog/order_status/',views.Order_statusView.as_view(),name='order_status'),
    path('user_catalog/about',views.AboutUsView.as_view(),name='about'),
]