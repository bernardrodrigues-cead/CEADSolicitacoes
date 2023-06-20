from django.core.exceptions import ValidationError
from datetime import datetime
from validate_docbr import CPF

def validate_nome_completo(value):
    """Verifica se a string contém dois ou mais palavras com dois ou mais caracteres 

    Args:
        value (string): string a ser validada

    Raises:
        ValidationError: Erro de validação
    """
    # Quebra a string em substrings (partes da cadeia de caracteres divididas por espaço)
    substrings = value.split() 
    # adiciona +1 a valid_substrings para cada substring de tamanho >= 2
    valid_substrings = sum(1 for substring in substrings if len(substring) >= 2) 
    # Se a quantidade de substrings válidas forem menores que 2,
    if valid_substrings < 2: 
        raise ValidationError('Nome inválido (Preencha o nome completo).') # Chama o erro

def validate_min_30(value):
    """Verifica se a string contém pelo menos 30 caracteres

    Args:
        value (string): string a ser validada

    Raises:
        ValidationError: Erro de validação
    """
    # Quebra a string em substrings (partes da cadeia de caracteres divididas por espaço)
    substrings = value.split()  
    # adiciona +1 a valid_substrings para cada substring de tamanho >= 2
    valid_substrings = sum(1 for substring in substrings if len(substring) >= 2)
    # Se a quantidade de substrings válidas forem menores que 2
    # ou a quantidade de caracteres for menor que 30
    # ou a quantidade de caracteres for maior que 250
    if valid_substrings < 2 or len(value) < 30 or len(value) > 250:  
        raise ValidationError('O campo deve conter pelo menos 30 caracteres.') # Chama o erro

def validate_data_futuro(value):
    if value and value < datetime.now().date():
        raise ValidationError('A data de agendamento precisa ser no futuro')

def validate_horario_agendamento(value):
    # Verifica se o horário de agendamento está entre 8:30 e 17:00
    if value and (value < datetime.strptime('8:30', '%H:%M').time() or value > datetime.strptime('17:00', '%H:%M').time()):
        raise ValidationError('O horário de agendamento precisa estar entre 8:30 e 17:00.')
    
def validate_cpf(value):
    # Filtra os simbolos dos caracteres e verifica se o valor tem 11 digitos  
    doc_cpf = CPF()
    if not doc_cpf.validate(value):
        raise ValidationError('CPF inválido')