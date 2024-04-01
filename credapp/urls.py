from . import views
from django.urls import path
from credapp import views

urlpatterns = [
    path('reg/',views.reg,name='reg'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]