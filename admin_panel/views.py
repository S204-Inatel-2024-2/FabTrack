# admin_panel/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the core index.")
