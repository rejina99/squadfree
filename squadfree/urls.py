from django.urls import path
from .views import squad, contactus
from . import views

urlpatterns = [
    path("squad", views.squad, name="squad"),
    path('', squad),
    path("contactus", views.contactus, name="contactus"),
    path('', contactus),
]