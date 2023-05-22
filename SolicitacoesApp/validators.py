from django.core.exceptions import ValidationError

def validate_professor_responsavel(value):
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

