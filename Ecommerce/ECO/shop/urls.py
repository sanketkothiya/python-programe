from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='shop'),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact,name="ContactUs"),
    path('search/', views.search,name="Search"),
    path('tracker', views.tracker,name="TrackingStatus"),
    path('productview/', views.productView,name="TrackingStatus"),
    path('checkout/', views.checkout,name="Checkout"),

]