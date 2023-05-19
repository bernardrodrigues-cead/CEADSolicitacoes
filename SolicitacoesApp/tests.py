from django.test import TestCase

data = {
    'professor_responsavel': 'Fulano de Tal',
    'horario_agendamento': '11:00',
    'duracao_gravacao': '2 horas',
    'data_entrega_material': '2023-06-06',
    'criar_arte': False,
    'setor_curso': 'Letras',
    'finalidade_gravacao': 'Gravar',
    'equipe_cead': True,
    'numero_participantes': 2,
    'email': 'test@example.com',
    'telefone': '32999998888',
    'observacao': ''
}

# Create your tests here.
class ProducaoDeMaterialTests(TestCase):
    def test_valid_form(self):
        pass