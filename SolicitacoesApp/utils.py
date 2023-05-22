from django.conf import settings
from django.core.mail import send_mail
from typing import List

def message_producao(data: dict) -> str:
    message = f'''
        Professor Responsável: {data['professor_responsavel']}
        Finalidade da Gravação: {data['finalidade_gravacao']}
        Horário de Agendamento: {data['horario_agendamento']}
        Duração da Gravação: {data['duracao_estimada']}
        Data de Entrega do Material: {data['data_entrega_material']}
        Serviços: {', '.join(data['servicos']) if 'servicos' in data else ''} 
        Arte para produção de material: {data['arte_pronta'] if 'arte_pronta' in data else ''}
        Precisa criar arte? {data['criar_arte']}
        Setor Curso: {data['setor_curso']}
        Equipamentos: {', '.join(data['equipamentos']) if 'equipamentos' in data else ''}  
        Precisará de nossa equipe de cinegrafistas? {data['equipe_cead']}
        Número de participantes: {data['numero_participantes']}
        E-mail: {data['email']}
        Telefone: {data['telefone']}
        Observações: {data['observacao']}         
    '''

    return message