# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: HabitCompass
def parse_date(date_str):
    """Парсит дату в формате 'YYYY-MM-DD' или 'DD.MM.YYYY'. Возвращает datetime.date или None."""
    if not date_str or not isinstance(date_str, str):
        return None
    for fmt in ("%Y-%m-%d", "%d.%m.%Y"):
        try:
            return datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    return None

def validate_date_input(user_input):
    """Валидирует дату от пользователя. Возвращает строку-сообщение об ошибке или True."""
    cleaned = user_input.strip()
    if not cleaned or cleaned.lower() in ("", "пусто", "нет"):
        return "Ошибка: Укажите корректную дату в формате YYYY-MM-DD или DD.MM.YYYY."
    
    parsed_date = parse_date(cleaned)
    if parsed_date is None:
        return f"Ошибка: Не удалось распознать дату '{cleaned}'. Используйте формат YYYY-MM-DD (2024-01-15) или DD.MM.YYYY (15.01.2024)."
    
    today = datetime.now().date()
    if parsed_date > today:
        return f"Ошибка: Дата {parsed_date} в будущем. Укажите прошедшую дату."
    
    return True

def format_date_output(date_obj):
    """Форматирует date для отображения. Возвращает строку или None."""
    if date_obj is None:
        return "Неизвестная дата"
    return date_obj.strftime("%d.%m.%Y")
