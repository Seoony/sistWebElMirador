from django.shortcuts import render

def myHomeView(request, *args, **kwargs):
  return render(request, "home.html")