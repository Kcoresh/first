# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: HabitCompass
def demo():
    """Демонстрация основного сценария HabitCompass."""
    from datetime import date, timedelta
    import random

    today = date.today()
    habits = {
        "Спорт": [],
        "Чтение": [],
        "Медитация": [],
        "Водный режим": [],
    }

    for _ in range(14):
        for habit in habits:
            if random.random() > 0.2:
                habits[habit].append(today - timedelta(days=random.randint(0, 13)))

    streaks = {h: calculate_streak(habits[h]) for h in habits}

    print("=== HabitCompass Demo ===")
    for habit, dates in habits.items():
        print(f"\n{habit}:")
        for d in sorted(dates, reverse=True)[:5]:
            print(f"  {d}")
    print("\nСтreakы:")
    for habit, streak in streaks.items():
        print(f"  {habit}: {streak} дней")

    print("\nНедельная аналитика:")
    for i in range(-6, 1):
        week_start = today + timedelta(days=i*7)
        week_dates = [d for d in dates if week_start <= d < week_start + timedelta(days=7)]
        if week_dates:
            print(f"  Неделя от {week_start} до {week_start + timedelta(days=6)}: {len(week_dates)} выполнений")

    print("\nДемо завершена.")

if __name__ == "__main__":
    demo()
