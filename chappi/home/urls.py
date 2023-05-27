from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('gallary/', views.gallary,name="gallary"),
    path('cooldrinks/',views.cooldrinks,name="cooldrinks"),
    path('hotdrinks/', views.hotdrinks,name="hotdrinks"),
    path('snacks/',views.snacks,name="snacks"),
]
