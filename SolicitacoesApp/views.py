import os, dotenv
from django.shortcuts import render
from django.views.generic.edit import CreateView

from SolicitacoesApp.forms import DadosDaViagemForm, DadosDoPrepostoForm
from .models import *
from django.urls import reverse_lazy
from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound

# Importa a função message_producao do arquivo utils.py
from SolicitacoesApp.utils import CARD_CONTENT, ERROR_MESSAGES, SUBMENUS

dotenv.load_dotenv()

# Create your views here.
def Index(request):
    context = {'card_info': CARD_CONTENT}
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
                form.add_error(None, ERROR_MESSAGES['entrega_lt_agendamento'])
                return self.form_invalid(form)

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
    
class ViagensCreateView(CreateView):
    model = Viagens
    template_name = 'administracao/viagens/create.html'
    fields=['curso', 'coordenador', 'email']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_preposto'] = DadosDoPrepostoForm()
        context['form_viagem'] = DadosDaViagemForm()
        return context
    
    def form_valid(self, form):
        form_preposto = DadosDoPrepostoForm(self.request.POST)
        form_viagem = DadosDaViagemForm(self.request.POST)
        
        if form_preposto.is_valid() and form_viagem.is_valid():
            if form_viagem.cleaned_data['data_retorno'] <= form_viagem.cleaned_data['data_saida']:
                form.add_error(None, ERROR_MESSAGES['retorno_lt_saida'])
                return self.form_invalid(form)
               
            
            new_preposto = DadosDoPreposto.objects.create(
                nome=form_preposto.cleaned_data['nome'],
                cpf=form_preposto.cleaned_data['cpf'],
                rg=form_preposto.cleaned_data['rg'],
                filiacao_1=form_preposto.cleaned_data['filiacao_1'],
                filiacao_2=form_preposto.cleaned_data['filiacao_2'],
                banco=form_preposto.cleaned_data['banco'],
                agencia=form_preposto.cleaned_data['agencia'],
                conta_corrente=form_preposto.cleaned_data['conta_corrente'],
                preposto_logradouro=form_preposto.cleaned_data['preposto_logradouro'],
                preposto_numero=form_preposto.cleaned_data['preposto_numero'],
                preposto_complemento=form_preposto.cleaned_data['preposto_complemento'],
                preposto_bairro=form_preposto.cleaned_data['preposto_bairro'],
                preposto_cidade=form_preposto.cleaned_data['preposto_cidade'],
                preposto_UF=form_preposto.cleaned_data['preposto_UF']
            )
            new_dados_da_viagem = DadosDaViagem.objects.create(
                logradouro=form_viagem.cleaned_data['logradouro'],
                numero=form_viagem.cleaned_data['numero'],
                complemento=form_viagem.cleaned_data['complemento'],
                bairro=form_viagem.cleaned_data['bairro'],
                cidade=form_viagem.cleaned_data['cidade'],
                UF=form_viagem.cleaned_data['UF'],
                data_saida=form_viagem.cleaned_data['data_saida'],
                horario_saida=form_viagem.cleaned_data['horario_saida'],
                data_retorno=form_viagem.cleaned_data['data_retorno'],
                horario_retorno=form_viagem.cleaned_data['horario_retorno'],
                objetivo_viagem=form_viagem.cleaned_data['objetivo_viagem'],
                outras_informacoes=form_viagem.cleaned_data['outras_informacoes']
            )

            new_viagens = form.save(commit=False)
            new_viagens.preposto = new_preposto
            new_viagens.dados_da_viagem = new_dados_da_viagem
            
            new_preposto.save()
            new_dados_da_viagem.save()
            new_viagens.save()

            subject=f"Solicitação - {form.cleaned_data['curso']}"  # Define o assunto do e-mail
            message = render_to_string('administracao/viagens/email_template.html', {'data': {
                **form.cleaned_data,
                **form_preposto.cleaned_data,
                **form_viagem.cleaned_data
            }})
            from_email=settings.EMAIL_HOST_USER  # Define o remetente do e-mail 
            recipient_list=[os.getenv('EMAIL_TESTES') if os.getenv('DEBUG') == 'True' else os.getenv('EMAIL_VIAGENS')]  # Define os destinatários do e-mail

            email = EmailMessage(subject, message, from_email, recipient_list)

            email.content_subtype = 'html'
            email.send()

        else:
            errors = [form_preposto.errors, form_viagem.errors]
            form.add_error(None, errors)
            return self.form_invalid(form)
            
        return super().form_valid(form)
            

def MenuAdministracao(request):
    return render(request,'administracao/menu.html', SUBMENUS)

def Error404View(request, exception):
    return HttpResponseNotFound(render(request, 'errors/404.html', status=404))