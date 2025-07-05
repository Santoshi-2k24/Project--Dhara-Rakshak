from django.shortcuts import render

def index(request):
 return render(request, 'index.html')

def guidelines(request):
 return render(request, 'guidelines.html')

def officer_login(request):
 return render(request, 'officer_login.html')

def officer_dashboard(request):
 return render(request, 'officer_dashboard.html')

def registration_form(request):
 return render(request, 'registration_form.html')

def search_dashboard(request):
 return render(request, 'search_dashboard.html')