import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def convert_to_currency(value):
    return locale.currency(value)