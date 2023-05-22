from django.conf import settings
from django.test import TestCase
from django.urls import reverse_lazy
from django.core import mail

from SolicitacoesApp.models import ProducaoDeMaterial

DATA = { # Constante com dados aptos para validação
    'professor_responsavel': 'Fulano de Tal',
    'setor_curso': 'Letras',
    'email': 'test@example.com',
    'telefone': '32999998888',
    'data_agendamento': '2023-01-01',
    'horario_agendamento': '0:00',
    'duracao_estimada': '2 horas',
    'data_entrega_material': '2023-01-01',
    'criar_arte': False,
    'finalidade_gravacao': 'Gravar um vídeo muito bom que alegre todos os envolvidos',
    'detalhes_arte': 'Uma linda arte que envolve a magia do bom artista em seu ápice',
    'equipe_cead': True,
    'numero_participantes': 2,
    'observacao': ''
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
        data = {**DATA, 'finalidade_gravacao': 'A'}
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), data)
        # verifica o status code da resposta
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