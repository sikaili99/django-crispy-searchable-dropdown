from django.shortcuts import render
from .form import CarForm
 
def home_view(request):
    context ={}
    context['form']= CarForm()
    return render(request, "crispyform/home.html", context)
    