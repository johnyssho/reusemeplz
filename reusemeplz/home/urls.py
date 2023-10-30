from django.urls import path
from .views import HomeView, CloudNavodView

urlpatterns = [
    path('', HomeView, name='home'),
    path('cloud-navod/', CloudNavodView, name='cloudnávod'),
]
