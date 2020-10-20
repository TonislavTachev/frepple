from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ElementsDemo(request):
    return render(request, 'theme_demo.html')

def BaseSite(request):
    return render(request, 'base_site_nav.html')