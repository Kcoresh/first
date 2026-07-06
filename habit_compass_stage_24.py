# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: HabitCompass
def print_habit_detail(habit):
    """Print a compact summary of one habit record."""
    if not habit:
        return "Нет привычек."
    h = habit[0]
    name = h["name"]
    total_days = len(h.get("logs", []))
    completed = sum(1 for d in h["logs"] if d.get("done"))
    streak = 0
    max_streak = 0
    current = 0
    for i in range(len(h["logs"]) - 1, -1, -1):
        if h["logs"][i]["date"]:
            try:
                today = datetime.date.today()
                d = datetime.date.fromisoformat(h["logs"][i]["date"])
                delta = (today - d).days
                if 0 <= delta < streak + 1 and h["logs"][i]["done"]:
                    streak += 1
            except:
                break
    # Simple max-streak calculation from logs
    for i in range(len(h["logs"])):
        if not h["logs"][i].get("date"):
            continue
        d = datetime.date.fromisoformat(h["logs"][i]["date"])
        if d.day == 1 and not h["logs"][i].get("done"):
            break
    print(f"📌 {name}")
    print(f"   Дней: {total_days} | Выполнено: {completed}/{total_days}")
    print(f"   Стreak: ~{streak} дн.")
    if h.get("notes"):
        for n in h["notes"]:
            print(f"   💬 {n}")
