from SolicitacoesApp.models import ServicoProducaoDeMaterial, EquipamentoProducaoDeMaterial

CARD_CONTENT = [
    {
        'titulo': 'Produção de Materiais',
        'resumo': "Acessoria de comunicação, edição e gravação de vídeos, criação de artes e diagramação",
        'img': 'assets/audiovisual.png',
        'alt_text': 'Equipamentos de audiovisual',
        'lazy_url': 'producao_create'
    }   
]

def message_producao(data: dict) -> str:
        # Serviços: {', '.join(data['servicos']) if 'servicos' in data else ''} 
        # Equipamentos: {', '.join(data['equipamentos']) if 'equipamentos' in data else ''}  
    message = f'''
        Professor Responsável: {data['professor_responsavel']}
        Finalidade da Gravação: {data['finalidade_solicitacao']}
        Horário de Agendamento: {data['horario_agendamento']}
        Duração da Gravação: {data['duracao_estimada']}
        Data de Entrega do Material: {data['data_entrega_material']}
        Arte para produção de material: {data['arte_pronta'] if 'arte_pronta' in data else ''}
        Detalhes da arte: {data['detalhes_arte']}
        Setor Curso: {data['setor_curso']}
        Precisará de nossa equipe de cinegrafistas? {data['equipe_cead']}
        Número de participantes: {data['numero_participantes']}
        E-mail: {data['email']}
        Telefone: {data['telefone']}
        Observações: {data['observacao']}      
    '''

    return message