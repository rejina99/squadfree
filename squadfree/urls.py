from django.urls import path
from .views import video
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', video),
]