CARD_CONTENT = [
    {
        'titulo': 'Produção de Materiais',
        'resumo': "Assessoria de comunicação, edição e gravação de vídeos, criação de artes e diagramação",
        'img': 'assets/audiovisual.png',
        'alt_text': 'Equipamentos de audiovisual',
        'lazy_url': 'producao_create'
    },
    {
        'titulo': 'Administração',
        'resumo': "Pagamento de bolsas, desvinculação de bolsistas, viagens e diárias, almoxarifado e gráfica.",
        'img': 'assets/Adm.png',
        'alt_text': 'Pastas de documentos',
        'lazy_url': 'administracao',
    }
]

SUBMENUS = {
    'administracao': [
        {
            'nome': 'Pagamento de Bolsas',
            'lazy_url': 'viagens_create',
        },
        {
            'nome': 'Desvinculação de bolsista, pedido de bolsas a mais ou pedido de lote complementar',
            'lazy_url': 'viagens_create',
        },
        {
            'nome': 'Viagens e diárias',
            'lazy_url': 'viagens_create',
        },
        {
            'nome': 'Almoxarifado e gráfica',
            'lazy_url': 'viagens_create',
        },
        
    ]
}


CHOICES_PARTICIPANTES = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
)

CHOICES_EQUIPE_CEAD = (
    (False, 'Não, iremos utilizar a nossa própria equipe'),
    (True, 'Sim, precisaremos da equipe do CEAD')
)

SERVICOS_PRODUCAO = (
    'Gravação de vídeo', 
    'Edição de vídeo', 
    'Gravação de apenas áudio', 
    'Edição de apenas áudio', 
    'Criação de arte (logo, banner, animação, vinheta, post)', 
    'Divulgação', 
    'Outro'
)
EQUIPAMENTOS_PRODUCAO = (
    'Câmera', 
    'Tripé', 
    'Luzes', 
    'Microfone', 
    'Slide', 
    'Teleprompter'
)

ERROR_MESSAGES = {
    'entrega_lt_agendamento': 'A data de entrega do material precisa ser posterior à data de agendamento da gravação.',
    'cpf': 'Informe um CPF válido.',
    'horario_agendamento': 'O horário de agendamento precisa estar entre 8:30 e 17:00.',
    'data_no_passado': 'A data de agendamento precisa ser no futuro',
    'min_caracteres': 'O campo deve conter pelo menos 30 caracteres.',
    'nome_invalido': 'Nome inválido (Preencha o nome completo).',
    'retorno_lt_saida': 'A data de retorno precisa ser posterior à data de saída.'
}