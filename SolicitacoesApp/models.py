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
        (5, '5')
    )

    professor_responsavel = models.CharField(max_length=100)
    servicos = models.ManyToManyField(ServicoProducaoDeMaterial)
    dia_agendamento = models.DateField()
    horario_agendamento = models.TimeField()
    duracao_gravacao = models.CharField(max_length=20)
    data_entrega_material = models.DateField()
    arte_pronta = models.FileField(upload_to='arte_pronta/', null=True, blank=True)
    criar_arte = models.BooleanField(default=False)
    setor_curso = models.CharField(max_length=100)
    projeto_disciplina = models.TextField()
    equipamentos = models.ManyToManyField(EquipamentoProducaoDeMaterial)
    equipe_cead = models.BooleanField(default=True)
    numero_participantes = models.IntegerField(choices=CHOICES_PARTICIPANTES)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    observacao = models.CharField(max_length=255)

    def __str__(self):
        return f"Produção de Material - {self.professor_responsavel}"
