# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: HabitCompass
def delete_record(record_id):
    """
    Удаляет запись по ID, если она существует.
    Возвращает True при успешном удалении, False если запись не найдена.
    """
    if record_id in records:
        del records[record_id]
        return True
    return False

def get_missing_ids(limit=5):
    """
    Возвращает список первых N отсутствующих ID для текущей серии.
    Используется для восстановления пропущенных дней в аналитике.
    """
    if not 'current_series_id' in records:
        return []
    
    series = records['current_series_id']
    if not series or 'days' not in series:
        return []
    
    existing_days = set(series['days'])
    missing = []
    current_date = datetime.now().date()
    
    # Ищем пропуски начиная с первого дня серии
    start_date = series.get('start_date', current_date)
    for delta in range(30):  # Проверка на месяц вперед
        check_date = start_date + timedelta(days=delta)
        if check_date not in existing_days:
            missing.append(check_date)
            if len(missing) >= limit:
                break
    
    return missing
