from django.test import TestCase
from django.urls import reverse_lazy

from SolicitacoesApp.models import ProducaoDeMaterial

DATA = { # Constante com dados validos para comparação
    'professor_responsavel': 'Fulano de Tal',
    'horario_agendamento': '0:00',
    'duracao_gravacao': '2 horas',
    'data_entrega_material': '2023-06-06',
    'criar_arte': False,
    'setor_curso': 'Letras',
    'finalidade_gravacao': 'Gravar um vídeo muito bom que alegre todos os envolvidos',
    'equipe_cead': True,
    'numero_participantes': 2,
    'email': 'test@example.com',
    'telefone': '32999998888',
    'observacao': ''
}

# Create your tests here.
class ProducaoDeMaterialTests(TestCase):
    def test_valid_form(self):
        """
        Verifica se o status code de uma requisição
        do tipo post com dados válidos é 302 (Found)
        """
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), DATA)
        # verifica o status code da resposta
        self.assertEqual(response.status_code, 302)

    def test_invalid_form(self):
        """
        Verifica se o status code de uma requisição
        do tipo post com dados inválidos é 200
        """
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), {})
        # verifica o status code da resposta
        self.assertEqual(response.status_code, 200)

    def test_object_creation(self):
        """
        Verifica se, após o envio de um formulário válido,
        um dado do tipo ProducaoDeMaterial é criado no banco
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
        Verifica se ocorreu o erro ao enviar o dado  invalido de professor responsavel
        """
        data = {**DATA, 'finalidade_gravacao': 'A'}
        # armazena o retorno da requisição post à view producao_create
        response = self.client.post(reverse_lazy('producao_create'), data)
        # verifica o status code da resposta
        self.assertEqual(response.status_code, 200)

    