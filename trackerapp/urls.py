from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('tracker_form/', views.tracker_form, name='tracker_form'),
    path('success/', views.success, name='success'),
    path('display_data/',views.display_data,name='display_data'),
]
