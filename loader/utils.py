from datetime import datetime
from .models import Record

def validate_json_record(record):
    name = record.get('name')
    date_str = record.get('date')

    if not name or not date_str:
        return False, 'Отсутствует нужный ключ'

    if len(name) >= 50:
        return False, 'Поле слишком длинное'

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d_%H:%M")
    except ValueError:
        return False, 'Неверный формат даты'

    return True, Record(name=name, date=date)
