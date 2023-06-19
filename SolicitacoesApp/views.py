import os, dotenv
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from django.urls import reverse_lazy
from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.http import HttpResponseNotFound 

# Importa a função message_producao do arquivo utils.py
from SolicitacoesApp.utils import CARD_CONTENT_PRODUCAO

dotenv.load_dotenv()

# Create your views here.
def Index(request):
    context = {'card_info': CARD_CONTENT_PRODUCAO}
    return render(request, 'index.html', context)


class ProducaoDeMaterialCreateView(CreateView) :
    model = ProducaoDeMaterial
    fields = '__all__'
    template_name = 'producao/create.html'
    success_url = reverse_lazy('index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['data_agendamento'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['horario_agendamento'].widget = forms.TimeInput(attrs={'type': 'time'})
        form.fields['data_entrega_material'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['servicos'] = forms.ModelMultipleChoiceField(
            queryset=ServicoProducaoDeMaterial.objects.all(), 
            widget=forms.CheckboxSelectMultiple,
            required=False
        )
        form.fields['equipamentos'] = forms.ModelMultipleChoiceField(
            queryset=EquipamentoProducaoDeMaterial.objects.all(), 
            widget=forms.CheckboxSelectMultiple,
            required=False
        )
        form.fields['numero_participantes'] = forms.ChoiceField(
            choices=CHOICES_PARTICIPANTES, 
            widget=forms.RadioSelect, 
            initial=0,
            required=False
        )
        return form
    
    # Define o método form_valid na sua classe CreateView
    def form_valid(self, form):
        """
        Caso o formulário seja válido, envie um e-mail com os dados do formulário para o responsável
        """
        # Verifica se foi preenchido o campo data_agendamento e data_entrega_material
        if form.cleaned_data['data_agendamento'] and form.cleaned_data['data_entrega_material']:
            # Verifica se a data de entrega do material é posterior à data de agendamento
            if form.cleaned_data['data_entrega_material'] <= form.cleaned_data['data_agendamento']:
                raise ValidationError('A data de entrega do material precisa ser posterior à data de agendamento da gravação.')

        form.save()
        
        subject=f"Solicitação - {form.cleaned_data['professor_responsavel']}"  # Define o assunto do e-mail
        # message=message_producao(form.cleaned_data)  # Define o corpo do e-mail usando a função message_producao
        message = render_to_string('producao/email_template.html', {'data': form.cleaned_data})
        from_email=settings.EMAIL_HOST_USER  # Define o remetente do e-mail 
        recipient_list=[os.getenv('EMAIL_TESTES') if os.getenv('DEBUG') == 'True' else os.getenv('EMAIL_PRODUCAO')]  # Define os destinatários do e-mail

        email = EmailMessage(subject, message, from_email, recipient_list)

        if form.cleaned_data['arte_pronta']:
            file = form.cleaned_data['arte_pronta']
            email.attach(file.name, file.read(), file.content_type)

        email.content_subtype = 'html'
        email.send()        

        # Reseta o comportamento da classe
        return super().form_valid(form)
    
def Error404View(request, exception):
    return HttpResponseNotFound(render(request, 'errors/404.html', status=404))