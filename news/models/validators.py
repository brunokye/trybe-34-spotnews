from django.core.exceptions import ValidationError


def validate_title(value):
    words = len(value.split())

    if words < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
