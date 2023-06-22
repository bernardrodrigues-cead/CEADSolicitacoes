CARD_CONTENT_PRODUCAO = [
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
        'alt_text': 'Ônibus de viagens',
        'lazy_url': 'producao_create'
    }
]

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