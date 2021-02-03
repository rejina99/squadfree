from django.urls import path
from .views import squad
from . import views

urlpatterns = [
    path("squad", views.squad, name="squad"),
    path('', squad),
]