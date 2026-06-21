# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: HabitCompass
def generate_summary(data):
    """Генерирует краткую текстовую сводку по данным привычек."""
    if not data:
        return "Данных нет."
    
    habits = list(data.values())
    total_habits = len(habits)
    completed_today = sum(1 for h in habits if h.get('completed', False))
    streaks = [h['streak'] for h in habits]
    avg_streak = sum(streaks) / len(streaks) if streaks else 0
    
    summary_lines = [f"Сводка за сегодня: {total_habits} привычек, выполнено {completed_today}."]
    
    if completed_today == total_habits and all(s > 0 for s in streaks):
        summary_lines.append("Отлично! Все серии продлены.")
    elif completed_today < total_habits:
        missed = [h['name'] for h in habits if not h.get('completed', False)]
        summary_lines.append(f"Пропущено: {', '.join(missed) if missed else 'Ничего'}")
    
    top_streak = max(streaks, default=0)
    if top_streak > 1:
        best_habit = next((h for h in habits if h['streak'] == top_streak), None)
        summary_lines.append(f"Рекорд серии ({top_streak} дней): {best_habit.get('name', 'неизвестно')}.")
    
    return "\n".join(summary_lines)
