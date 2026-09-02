# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: HabitCompass
def weekly_analytics(habits_data, week_start):
    """Generate weekly analytics for each habit.

    Args:
        habits_data: Dict mapping habit_name to list of daily entries.
        week_start: Date string ('YYYY-MM-DD') marking start of the week.

    Returns:
        Dict mapping habit_name to analytics dict with keys:
            'completed_days', 'streak', 'average_daily_score', 'weekly_notes'
    """
    from datetime import datetime, timedelta

    current = datetime.strptime(week_start, "%Y-%m-%d")
    end = current + timedelta(days=6)
    days_in_week = []
    while current <= end:
        days_in_week.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)

    analytics = {}
    for habit_name, daily_entries in habits_data.items():
        completed = 0
        streak = 0
        max_streak = 0
        scores = []
        notes = []
        completed_dates = []

        for entry in daily_entries:
            date_str = entry.get("date", "")
            score = entry.get("score", 0)
            note = entry.get("note", "")

            if date_str in days_in_week:
                if score > 0:
                    completed += 1
                    completed_dates.append(date_str)
                    streak += 1
                else:
                    streak = 0
                scores.append(score)
                notes.append(note)

        max_streak = max(streak, max_streak)
        avg_score = sum(scores) / len(scores) if scores else 0.0
        analytics[habit_name] = {
            "completed_days": completed,
            "streak": max_streak,
            "average_daily_score": avg_score,
            "weekly_notes": notes,
        }

    return analytics
