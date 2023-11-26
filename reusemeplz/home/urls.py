from django.urls import path
from .views import HomeView, CloudNavodView, BootTipsView

urlpatterns = [
    path('', HomeView, name='home'),
    path('cloud-navod/', CloudNavodView, name='cloudnávod'),
    path('boot-tips/', BootTipsView, name='boot-tips'),
]
