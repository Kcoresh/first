# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: HabitCompass
def get_usage_scenarios(habits, notes_by_day):
    """Возвращает краткое описание сценариев использования приложения HabitCompass."""
    scenarios = []
    
    # Сценарий 1: Отслеживание серии привычек
    if habits:
        habit_names = [f"{h['name']} ({h.get('series', 0)}x)" for h in habits]
        scenarios.append(f"Отслеживаю серию: {', '.join(habit_names)}")
    
    # Сценарий 2: Просмотр заметок по дням
    if notes_by_day:
        days = sorted(notes_by_day.keys())
        day_notes = [f"{d}: {notes_by_day[d]}" for d in days]
        scenarios.append(f"Заметки за {len(days)} дней:\n  " + "\n  ".join(day_notes))
    
    # Сценарий 3: Еженедельная аналитика (если есть данные)
    if notes_by_day and len(notes_by_day) >= 7:
        total_days = len([d for d in sorted(notes_by_day.keys())])
        scenarios.append(f"Недельная статистика: {total_days} дней с записями")

    return "\n".join(scenarios) if scenarios else "Нет активных данных для анализа."


# Пример использования (для проверки):
if __name__ == "__main__":
    test_habits = [
        {"name": "Спорт", "series": 5},
        {"name": "Чтение", "series": 3},
    ]
    test_notes = {
        "Пн": "Тренерка прошла отлично!",
        "Вт": "Прочитал главу о Python.",
        "Ср": "",
        "Чт": "Спорт + книга",
    }
    
    print("=" * 50)
    print("📋 Сценарии использования HabitCompass:")
    print("=" * 50)
    result = get_usage_scenarios(test_habits, test_notes)
    print(result)
