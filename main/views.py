from django.shortcuts import render
from .models import *
from django.views.generic import  DetailView

# Create your views here.
def homeView(request):
    context = {
        'MainPages': MainPage.objects.all().order_by('-id'),
        'categories': Category.objects.all(),
        'travels' : TravelTicket.objects.prefetch_related('img').select_related('category').all(),
        'pictures' : Picture.objects.all().order_by('?')[:8]
    }
    return render(request, 'index.html', context)

class detail(DetailView):
    model = TravelTicket
    template_name = 'detail.html'