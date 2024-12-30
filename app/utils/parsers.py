import logging
import re


# Utilidad para convertir strings a números de forma segura
def parse_number_stocks(value, number_type=float, default=0):
    try:
        if not value:
            return default
        if number_type == int:
            return int(value.replace(",", ""))
        return float(value.replace(",", "."))
    except Exception as e:
        logging.error(f"Error al parsear el número '{value}': {e}")
        return default


def parse_number_summary(value, value_type=float, default_value=0.0):
    """Parses a number considering comma as thousand separator and dot as decimal separator."""
    try:
        value = value.replace('.', '')
        value = value.replace(',', '.')
        return value_type(value)
    except Exception as e:
        logging.error(f"Error al parsear el valor '{value}': {e}")
        return default_value