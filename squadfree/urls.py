from django.urls import path
from .views import video
from . import views

urlpatterns = [
    path("video", views.video, name="video"),
    path('', video),
]