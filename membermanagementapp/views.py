from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'membermanagementapp/index.html')

def add_item(request):
    return render(request, 'membermanagementapp/addItem.html')