from django.http import HttpResponse

def index(request):
    return HttpResponse("✅ Django backend working. Template coming soon.")
