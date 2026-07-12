# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: HabitCompass
def print_metrics():
    total_days = sum(len(d) for d in data.values())
    completed = sum(1 for i, day_list in enumerate(data.values()) for j, done in enumerate(day_list) if done and i < len(days_per_week))
    streaks = {k: 0 for k in range(4)}
    for _, day_list in data.items():
        current_streak = 0
        for done in reversed(day_list):
            if done:
                current_streak += 1
            else:
                break
        streaks[current_streak] += 1
    missed_weekly = sum(1 for i, day_list in enumerate(data.values()) if not any(day_list[i:i+days_per_week]))
    print(f"Total days tracked: {total_days}")
    print(f"Completed habits this week: {completed}/{total_days * 7}")
    print(f"Weekly completion rate: {completed/(total_days*7)*100:.1f}%")
    print(f"Streak distribution: {streaks}")
    print(f"Weeks with missed goals: {missed_weekly}")

print_metrics()
