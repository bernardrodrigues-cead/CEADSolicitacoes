from django.conf import settings
from django.test import TestCase
from django.urls import reverse_lazy
from django.core import mail
from django.utils import timezone
from SolicitacoesApp.models import ProducaoDeMaterial, ServicoProducaoDeMaterial

DATA = { # Constante com dados aptos para validação
    # 'servico': ServicoProducaoDeMaterial.objects.last(),
    'professor_responsavel': 'José da Silva',
    'setor_curso': 'Física',
    'email': 'jose@silva.com',
    'data_entrega_material': (timezone.now() + timezone.timedelta(days=1)).strftime('%Y-%m-%d'),
    'finalidade_solicitacao': "Gravar um vídeo único com a equipe única que é a da produção",
    'equipe_cead': False,
    'numero_participantes': 1
}

# Create your tests here.
class ProducaoDeMaterialTests(TestCase):
    def test_valid_form(self):
        """
        Verifica se o status code de uma requisição do tipo post com dados válidos é 302 (Found)
        """
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), DATA)
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
        self.client.post(reverse_lazy('producao_create'), DATA)
        # verifica a criação de um novo objeto
        self.assertEqual(ProducaoDeMaterial.objects.count(), 1)

    def test_professor_responsavel_failure(self):
        """
        Verifica se ocorreu o erro ao enviar o dado  invalido de professor responsavel
        """
        data = {**DATA, 'professor_responsavel': 'A'}
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), data)
        # verifica o status code da resposta
        self.assertEqual(response.status_code, 200)

    def test_finalidade_gravacao_failure(self):
        """
        Verifica se ocorreu o erro ao enviar o dado  invalido de finalidade de gravação
        """
        data = {**DATA, 'finalidade_solicitacao': 'A'}
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), data)
        # verifica o status code da resposta
        self.assertEqual(response.status_code, 200)

    def test_past_data_agendamento_failure(self):
        """
        Test_past_data_agendamento_failure: O formulário envia uma data de agendamento no passado 
        (geralmente um dia) e verifica se o status code da requisição é 200, indicando erro no envio.
        """
        data = {**DATA, 'data_agendamento': timezone.now() - timezone.timedelta(days=1)}

        response = self.client.post(reverse_lazy('producao_create'), data)

        self.assertEqual(response.status_code, 200)
        
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

# class DadosPrepostoTest(TestCase):
#     DADOS = {
#         'cpf' : '08710804609',
#         'rg' : '454332313',
#         'filiacao_mae' : 'Genoveva Martins',
#         'filiacao_pai' : 'Seu carlos',
#         'agencia' : '54342',
#         'conta_corrente' : '2424124',
#         'banco' : '212121122',
#         'endereco_logradouro' : 'saasassasasas',
#         'endereco_numero' : 111,
#         'endereco_bairro' : 'Triângulo',
#         'complemento' : 'fodase',
#     }
 
#     def test_cpf(self):
#         self.client.post()     