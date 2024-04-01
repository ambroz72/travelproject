
from . import views
from django.urls import path,include
from travelapp import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('next_page/',views.next_page,name='next_page'),
    # path('add/',views.addition,name='addition'),
]
