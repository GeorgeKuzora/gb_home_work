from wtforms import ValidationError


def validate_len_80(form, field):
    if len(field.data) > 80:
        raise ValidationError("Field must be less or equal to 80 characters")
