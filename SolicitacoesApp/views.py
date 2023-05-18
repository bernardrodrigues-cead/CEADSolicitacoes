from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
def Index(request):

    return render(request, 'SolicitacoesApp/index.html')


class ProducaoDeMaterialCreateView(CreateView) :
    model = ProducaoDeMaterial
    fields = '__all__'
    template_name = 'SolitacoesApp/producao/create.html'
    success_url = reverse_lazy('index')