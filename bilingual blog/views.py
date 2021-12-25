from django.shortcuts import redirect, render
from django.utils.translation import activate

# Create your views here.
def home(request):
    return render (request,'slideshow/home.html')

def change_lang(request):
    activate(request.GET.get('lang'))
    return redirect(request.GET.get('next'))