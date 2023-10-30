from django.shortcuts import render

def HomeView(request):
  return render(request, 'home.html')

def CloudNavodView(request):
  return render(request, 'cloud-návod.html')
