from django.urls import path
from .views import HomeView, CloudNavodView, BootTipsView, DebianInstalaceView, AptView

urlpatterns = [
    path('', HomeView, name='home'),
    path('cloud-navod/', CloudNavodView, name='cloudnávod'),
    path('boot-tips/', BootTipsView, name='boot-tips'),
    path('debian-instalace/', DebianInstalaceView, name='debian-instalace'),
    path('apt/', AptView, name='apt'),
]
