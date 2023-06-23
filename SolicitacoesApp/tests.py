from django.conf import settings
from django.test import TestCase
from django.urls import reverse_lazy
from django.core import mail
from django.utils import timezone
from SolicitacoesApp.models import DadosDaViagem, DadosDoPreposto, ProducaoDeMaterial, ServicoProducaoDeMaterial, Viagens
from SolicitacoesApp.utils import ERROR_MESSAGES

DATA = { # Constante com dados aptos para validação
    'producao': {
        'professor_responsavel': 'José da Silva',
        'setor_curso': 'Física',
        'email': 'jose@silva.com',
        'data_entrega_material': (timezone.now() + timezone.timedelta(days=1)).strftime('%Y-%m-%d'),
        'finalidade_solicitacao': "Gravar um vídeo único com a equipe única que é a da produção",
        'equipe_cead': False,
        'numero_participantes': 1
    },
    'viagens': {
        'curso': 'Física',
        'coordenador': 'José da Silva',
        'nome': 'José da Silva',
        'cpf': '00000000191',
        'rg': 'SP-1916283',
        
        'filiacao_1': 'Antônia da Silva',
        'filiacao_2': 'Mirelle da Silva',
        
        'banco': 'Banco do Brasil',
        'agencia': '2628-4',
        'conta_corrente': '48442-6',
        
        'preposto_logradouro': 'Rua das Camomilas',
        'preposto_numero': 10,
        'preposto_complemento': 'Fundos',
        'preposto_bairro': 'Murmúrios',
        'preposto_cidade': 'Jacarepaguá',
        'preposto_UF': 'SP',

        'logradouro': 'Rua dos Jardins Primaveris',
        'numero': 118,
        'complemento': '',
        'bairro': 'Luz Estrela',
        'cidade': 'Matozinhos',
        'UF': 'MT',

        'data_saida': (timezone.now() + timezone.timedelta(days=1)).strftime('%Y-%m-%d'),
        'data_retorno': (timezone.now() + timezone.timedelta(days=2)).strftime('%Y-%m-%d'),
        
        'objetivo_viagem': 'Viajar com os outros professores que vão',
        'outras_informacoes': ''
    }
}

# Create your tests here.
class ProducaoDeMaterialTests(TestCase):
    def test_valid_form(self):
        """
        Verifica se o status code de uma requisição do tipo post com dados válidos é 302 (Found)
        """
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), DATA['producao'])
        # verifica o status code da resposta
        self.assertEqual(response.status_code, 302)

    def test_invalid_form(self):
        """
        Verifica se o status code de uma requisição do tipo post com dados inválidos é 200
        """
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), {})
        # verifica o status code da resposta
        self.assertEqual(response.status_code, 200)

    def test_object_creation(self):
        """
        Verifica se, após o envio de um formulário válido, um dado do tipo ProducaoDeMaterial é criado no banco
        """
        # armazena o retorno da requisição post à view producao_create
        self.client.post(reverse_lazy('producao_create'), DATA['producao'])
        # verifica a criação de um novo objeto
        self.assertEqual(ProducaoDeMaterial.objects.count(), 1)

    def test_professor_responsavel_failure(self):
        """
        Verifica se ocorreu o erro ao enviar o dado  invalido de professor responsavel
        """
        data = {**DATA['producao'], 'professor_responsavel': 'A'}
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), data)
        # verifica o status code da resposta
        self.assertEqual(response.status_code, 200)

        form = response.context['form']

        self.assertIn(ERROR_MESSAGES['nome_invalido'], str(form.errors))

    def test_finalidade_gravacao_failure(self):
        """
        Verifica se ocorreu o erro ao enviar o dado  invalido de finalidade de gravação
        """
        data = {**DATA['producao'], 'finalidade_solicitacao': 'A'}
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), data)
        # verifica o status code da resposta
        self.assertEqual(response.status_code, 200)

    def test_past_data_entrega_material_failure(self):
        """
        Test_past_data_entrega_material_failure: O formulário envia uma data de entrega do material no passado 
        (geralmente um dia) e verifica se o status code da requisição é 200, indicando erro no envio.
        """
        data = {**DATA['producao'], 'data_entrega_material': (timezone.now() - timezone.timedelta(days=1)).strftime('%Y-%m-%d')}

        response = self.client.post(reverse_lazy('producao_create'), data)

        self.assertEqual(response.status_code, 200)

        form = response.context['form']

        self.assertIn(ERROR_MESSAGES['data_no_passado'], str(form.errors))

    def test_data_entrega_material_lt_data_agendamento(self):
        """
        test_data_entrega_material_lt_data_agendamento: Envia uma data de agendamento posterior à data de entre
        e se espera um erro de validação e status 200
        """
        data = {
            **DATA['producao'], 
            'data_agendamento': (timezone.now() + timezone.timedelta(days=2)).strftime('%Y-%m-%d'),
            'data_entrega_material': (timezone.now() + timezone.timedelta(days=1)).strftime('%Y-%m-%d'),
        }
        response = self.client.post(reverse_lazy('producao_create'), data)
        self.assertEqual(response.status_code, 200)

        form = response.context['form']

        self.assertIn(ERROR_MESSAGES['entrega_lt_agendamento'], str(form.errors))
    
class ViajensTests(TestCase):
    def test_valid_form(self):
        response = self.client.post(reverse_lazy('viagens_create'), DATA['viagens'])
        self.assertEqual(response.status_code, 302)

    def test_object_creation(self):
        self.client.post(reverse_lazy('viagens_create'), DATA['viagens'])
        self.assertEqual(Viagens.objects.count(), 1)
        self.assertEqual(DadosDoPreposto.objects.count(), 1)
        self.assertEqual(DadosDaViagem.objects.count(), 1)

    def test_invalid_cpf(self):
        data = {**DATA['viagens'], 'cpf': '07446974681'}
        response = self.client.post(reverse_lazy('viagens_create'), data)
        self.assertEqual(response.status_code, 200)

        form = response.context['form']

        self.assertIn(ERROR_MESSAGES['cpf'], str(form.errors))

    def test_past_data_saida_failure(self):
        data = {**DATA['viagens'], 'data_saida': (timezone.now() - timezone.timedelta(days=1)).strftime('%Y-%m-%d')}
        response = self.client.post(reverse_lazy('viagens_create'), data)
        self.assertEqual(response.status_code, 200)

        form = response.context['form']

        self.assertIn(ERROR_MESSAGES['data_no_passado'], str(form.errors))

    def test_past_data_retorno_failure(self):
        data = {**DATA['viagens'], 'data_retorno': (timezone.now() - timezone.timedelta(days=1)).strftime('%Y-%m-%d')}
        response = self.client.post(reverse_lazy('viagens_create'), data)
        self.assertEqual(response.status_code, 200)

        form = response.context['form']

        self.assertIn(ERROR_MESSAGES['data_no_passado'], str(form.errors))

    def test_data_retorno_lt_data_saida(self):
        data = {
            **DATA['viagens'],
            'data_retorno': (timezone.now() + timezone.timedelta(days=1)).strftime('%Y-%m-%d'),
            'data_saida': (timezone.now() + timezone.timedelta(days=2)).strftime('%Y-%m-%d'),
        }
        response = self.client.post(reverse_lazy('viagens_create'), data)
        self.assertEqual(response.status_code, 200)

        form = response.context['form']

        self.assertIn(ERROR_MESSAGES['retorno_lt_saida'], str(form.errors))

class EmailSenderTest(TestCase):
    def test_email_sending(self):
        """
        Verifica se o envio de email está funcional
        """

        # envia um email para o próprio remetente
        mail.send_mail(
            subject='test email',
            message='test body',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER]
        )

        # verifica se a caixa de saída possui um email
        self.assertEqual(len(mail.outbox), 1)

        # armazena os dados do email enviado numa variável
        sent_email = mail.outbox[0]

        # verifica se os dados enviados conferem com o os originais
        self.assertEqual(sent_email.subject, "test email")
        self.assertEqual(sent_email.body, "test body")
        self.assertEqual(sent_email.from_email, settings.EMAIL_HOST_USER)
        self.assertEqual(sent_email.to, [settings.EMAIL_HOST_USER])    