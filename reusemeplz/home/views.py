from django.shortcuts import render

def HomeView(request):
  return render(request, 'home.html')

def CloudNavodView(request):
  return render(request, 'cloud-návod.html')

def BootTipsView(request):
  return render(request, 'boot-tips.html')

def DebianInstalaceView(request):
  return render(request, 'debian-instalace.html')

def AptView(request):
  return render(request, 'apt.html')