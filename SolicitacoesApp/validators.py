from django.core.exceptions import ValidationError

def validate_professor_responsavel(value):
    substrings = value.split()
    valid_substrings = sum(1 for substring in substrings if len(substring) >= 2)
    if valid_substrings < 2:
        raise ValidationError('Nome inválido (Preencha o nome completo).')

def validate_finalidade_gravacao(value):
    substrings = value.split()
    valid_substrings = sum(1 for substring in substrings if len(substring) >= 2)
    if valid_substrings < 2 or len(value) < 30:
        raise ValidationError('O campo deve conter pelo menos 30 caracteres.')
