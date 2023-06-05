import os, dotenv

from SolicitacoesApp.models import EquipamentoProducaoDeMaterial, ServicoProducaoDeMaterial
from SolicitacoesApp.utils import EQUIPAMENTOS_PRODUCAO, SERVICOS_PRODUCAO

dotenv.load_dotenv('.env')

for servico in SERVICOS_PRODUCAO:
    new = ServicoProducaoDeMaterial.objects.create(nome=servico)
    new.save()

for equipamento in EQUIPAMENTOS_PRODUCAO:
    new = EquipamentoProducaoDeMaterial.objects.create(nome=equipamento)
    new.save()