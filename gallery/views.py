from django.shortcuts import render
from .models import Images, Locations

# Create your views here.
def home(request):
    pictures = Images.get_all()
    return render(request, 'home.html', {'pictures': pictures})