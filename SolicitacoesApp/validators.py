from django.core.exceptions import ValidationError

def validate_professor_responsavel(value): # Verifica se a string contém dois ou mais palavras com dois ou mais caracteres 
    substrings = value.split() # Quebra a string em substrings (partes da cadeia de caracteres divididas por espaço)
    valid_substrings = sum(1 for substring in substrings if len(substring) >= 2) # adiciona +1 a valid_substrings para cada substring de tamanho >= 2
    if valid_substrings < 2: # Se a quantidade de substrings válidas forem menores que 2,
        raise ValidationError('Nome inválido (Preencha o nome completo).') # Chama o erro

def validate_finalidade_gravacao(value): # Verifica se a string contém dois ou mais caracteres
    substrings = value.split()  # Quebra a string em substrings (partes da cadeia de caracteres divididas por espaço)
    valid_substrings = sum(1 for substring in substrings if len(substring) >= 2) # adiciona +1 a valid_substrings para cada substring de tamanho >= 2
    if valid_substrings < 2 or len(value) < 30:  # Se a quantidade de substrings válidas forem menores que 2, ou a quantidade de caracteres for maior que 30
        raise ValidationError('O campo deve conter pelo menos 30 caracteres.') # Chama o erro

