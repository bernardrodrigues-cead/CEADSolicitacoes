# Create your models here.
from django.db import models

class ServicoProducaoDeMaterial(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class EquipamentoProducaoDeMaterial(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class ProducaoDeMaterial(models.Model):
   
    CHOICES_PARTICIPANTES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

    professor_responsavel = models.CharField(max_length=100, verbose_name='Professor Responsável')
    servicos = models.ManyToManyField(ServicoProducaoDeMaterial, verbose_name='Serviços')
    horario_agendamento = models.TimeField(verbose_name='Horário de Agendamento')
    duracao_gravacao = models.CharField(max_length=20, verbose_name='Duração da Gravação')
    data_entrega_material = models.DateField(verbose_name='Data de Entrega do Material')
    arte_pronta = models.FileField(upload_to='arte_pronta/', null=True, blank=True, verbose_name='Arte para produção de material')
    criar_arte = models.BooleanField(default=False, verbose_name='Precisa criar arte?')
    setor_curso = models.CharField(max_length=100, verbose_name="Setor Curso")
    finalidade_gravacao = models.TextField(verbose_name='Finalidade da Gravação')
    equipamentos = models.ManyToManyField(EquipamentoProducaoDeMaterial)
    equipe_cead = models.BooleanField(verbose_name='Precisará de nossa equipe de cinegrafistas?')
    numero_participantes = models.IntegerField(choices=CHOICES_PARTICIPANTES, verbose_name='Número de participantes')
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=20)
    observacao = models.CharField(max_length=255, verbose_name='Observações', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Produção de Material - {self.professor_responsavel}"
