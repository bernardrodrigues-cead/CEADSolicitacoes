from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from django.urls import reverse_lazy
from django import forms

# Create your views here.
def Index(request):

    return render(request, 'SolicitacoesApp/index.html')


class ProducaoDeMaterialCreateView(CreateView) :
    model = ProducaoDeMaterial
    fields = '__all__'
    template_name = 'SolicitacoesApp/producao/create.html'
    success_url = reverse_lazy('index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['horario_agendamento'].widget = forms.TimeInput(attrs={'type': 'time'})
        form.fields['data_entrega_material'].widget = forms.DateInput(attrs={'type': 'date'})

        form.fields['equipamentos'] = forms.ModelMultipleChoiceField(
            queryset=EquipamentoProducaoDeMaterial.objects.all(), 
            widget=forms.CheckboxSelectMultiple
        )

        form.fields['servicos'] = forms.ModelMultipleChoiceField(
            queryset=ServicoProducaoDeMaterial.objects.all(), 
            widget=forms.CheckboxSelectMultiple
        )

        return form

    def form_invalid(self, form) :
        print(form.errors)

        
        return super().form_invalid(form)     

