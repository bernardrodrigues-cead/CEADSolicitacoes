from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from django.urls import reverse_lazy
from django import forms

# Importe a função message_producao do arquivo utils.py
from SolicitacoesApp.utils import message_producao

# Importe os módulos necessários do Django
from django.conf import settings
from django.core.mail import send_mail

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
        return form
        
    # Defina o método form_valid na sua classe CreateView
    def form_valid(self, form):
        """
        Caso o formulário seja válido, envie um e-mail com os dados do formulário para o responsável
        """
        send_mail(
            subject=f"Solicitação - {form.cleaned_data['professor_responsavel']}",  # Defina o assunto do e-mail
            message=message_producao(form.cleaned_data),  # Defina o corpo do e-mail usando a função message_producao
            from_email=settings.EMAIL_HOST_USER,  # Defina o remetente do e-mail 
            recipient_list=['seu@email.com']  # Defina os destinatários do e-mail
        )
        
        # Continue com o comportamento padrão do form_valid
        return super().form_valid(form)


