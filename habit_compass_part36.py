# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: HabitCompass
def check_and_repair():
    """Проверка целостности данных и ремонт простых проблем. Возвращает отчёт о найденных проблемах."""
    issues = []
    
    # Проверка 1: Все серии имеют корректные даты (не пустые строки)
    for habit_id, series in habits.items():
        if not isinstance(series, dict):
            issues.append(f"Серия для привычки {habit_id} не является словарём")
            continue
        for date_str in series:
            if not date_str or date_str.strip() == "":
                issues.append(f"Пустая дата в серии привычки {habit_id}")
    
    # Проверка 2: Все заметки имеют корректный формат (не пустые строки)
    for habit_id, notes in habits.items():
        if not isinstance(notes, dict):
            continue
        current_date = notes.get("current_date", "")
        if current_date and notes.get("daily_notes"):
            for date_key, day_note in notes["daily_notes"].items():
                if not isinstance(day_note, str) or day_note.strip() == "":
                    issues.append(f"Некорректная заметка для {date_key} в привычке {habit_id}")
    
    # Проверка 3: Данные о привычках не пустые
    for habit in habits.values():
        if not isinstance(habit, dict):
            continue
        name = habit.get("name", "")
        if not name or name.strip() == "":
            issues.append(f"Привычка без имени найдена")
    
    return issues

def repair_simple_issues(issues):
    """Ремонт простых проблем: очистка пустых строк в датах и заметках."""
    repaired = 0
    
    if not issues:
        return "Все данные целостны", 0
    
    for habit_id, series in list(habits.items()):
        if not isinstance(series, dict):
            continue
        # Ремонт пустых дат - удаление их из серии
        original_dates = list(series.keys())
        cleaned_dates = [d.strip() for d in original_dates if d and d.strip()]
        
        if len(cleaned_dates) != len(original_dates):
            issues.append(f"Удалено {len(original_dates) - len(cleaned_dates)} пустых дат из серии {habit_id}")
            habits[habit_id] = dict(zip(cleaned_dates, series.values()))
    
    for habit_id, notes in list(habits.items()):
        if not isinstance(notes, dict):
            continue
        
        # Ремонт пустых заметок - удаление их из daily_notes
        current_date = notes.get("current_date", "")
        if current_date and notes.get("daily_notes"):
            original_keys = list(notes["daily_notes"].keys())
            cleaned_keys = [k.strip() for k in original_keys if k and k.strip()]
            
            if len(cleaned_keys) != len(original_keys):
                issues.append(f"Удалено {len(original_keys) - len(cleaned_keys)} пустых заметок для {current_date}")
                notes["daily_notes"] = dict(zip(cleaned_keys, notes["daily_notes"].values()))
    
    return "Исправлено", repaired
