# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: HabitCompass
def calculate_weekly_stats(records):
    from datetime import date, timedelta
    if not records: return {}
    today = date.today()
    week_start = (today - timedelta(days=today.weekday())).isoformat()
    week_end = (week_start + timedelta(days=6)).isoformat()
    weekly_data = {d: {"completed": 0, "notes": []} for d in range(int(week_start), int(week_end) + 1)}
    for r in records:
        if not isinstance(r.get("date"), str): continue
        try: rec_date = date.fromisoformat(r["date"])
        except ValueError: continue
        if week_start <= rec_date.isoformat() <= week_end:
            weekly_data[rec_date.isoformat()]["completed"] += r.get("count", 1)
            notes = r.get("notes", []) or []
            for note in notes:
                weekly_data[rec_date.isoformat()]["notes"].append(note)
    return weekly_data
