# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: HabitCompass
def get_next_action(habits, today):
    """Рекомендует следующее действие на основе прогресса по сериям."""
    if not habits:
        return "Начни с одной простой привычки!"
    
    streaks = [(h['name'], h.get('streak', 0), h.get('last_date')) for h in habits]
    
    # Находим привычку с наименьшей серией, но не нулевой
    pending_habits = [(n, s) for n, s in streaks if s > 0 and (s < 5 or today.weekday() % 7 == s % 7)]
    if not pending_habits:
        # Если все серии >= 5 или текущий день совпадает с серией - рекомендуем первую привычку
        return f"Продолжай в том же духе! Следующая: {streaks[0][0]}"
    
    best = min(pending_habits, key=lambda x: x[1])
    return f"Сегодня фокусируйся на: {best[0]} (серия: {best[1]})"
