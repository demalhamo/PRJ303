from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='cd-home'),
    path('cases',views.cases, name='cd-cases'),
    path('prediction',views.prediction, name='cd-prediction'),
    
]