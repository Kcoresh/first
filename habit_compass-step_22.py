# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: HabitCompass
def check_overdue_reminders():
    today = datetime.date.today()
    overdue_list = []
    for habit in habits:
        if not habit.enabled or habit.reminder_date is None:
            continue
        reminder_dt = datetime.datetime.combine(today, datetime.time(8))
        last_check = getattr(habit, '_last_checked', datetime.datetime.min)
        if last_check < reminder_dt and today >= habit.reminder_date:
            overdue_list.append({
                'habit': habit.name,
                'days_overdue': (today - habit.reminder_date).days,
                'message': f"Не забудьте выполнить '{habit.name}' — вы пропустили напоминание!"
            })
        if today > last_check.date():
            habit._last_checked = datetime.datetime.combine(today, datetime.time(0))
    return overdue_list
