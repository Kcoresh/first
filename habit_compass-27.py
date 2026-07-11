# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: HabitCompass
def reset_demo_data():
    """Сбросить все демо-данные в начало списка."""
    demo = [
        (1, "Пить воду", True),
        (2, "Читать 30 мин", False),
        (3, "Медитация", True),
        (4, "Спорт", False),
        (5, "Вести дневник", True),
    ]
    habits = []
    for i, name, active in demo:
        if not active:
            continue
        habit_id = len(habits) + 1
        entry_count = 0
        series_start = 0
        last_date = None
        notes = {}
        streaks = {i: 0 for i in range(7)}
        history = []
        for j in range(3):
            d = (2024, 1, 1 + j)
            entry_count += 1
            series_start = len(series_start) if not series_start else series_start
            last_date = d
            notes[d] = f"Демо-заметка {j}"
            for i in range(7):
                streaks[i] = 0
        return habits, entry_count, series_start, last_date, notes, streaks, history


def clear_state():
    """Полностью очистить все данные и сбросить в начальное состояние."""
    habits = []
    entry_count = 0
    series_start = 0
    last_date = None
    notes = {}
    streaks = {i: 0 for i in range(7)}
    history = []
    return habits, entry_count, series_start, last_date, notes, streaks, history


def get_initial_state():
    """Возвращает начальные значения всех переменных состояния."""
    return [], 0, 0, None, {}, {i: 0 for i in range(7)}, []
