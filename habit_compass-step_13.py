# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: HabitCompass
class HabitCompass:
    def __init__(self):
        self.habits = {}  # {id: {"name": str, "streak": int}}
        self.daily_logs = []  # [{date: str, habit_id: str, note: str}]
    
    def _case_insensitive_search(self, text: str) -> bool:
        if not text: return True
        pattern = re.compile(re.escape(text), re.IGNORECASE)
        return pattern.search

    def search_habits(self, query: str):
        if not self.habits: return []
        q_lower = query.lower()
        results = [h for h in self.habits.values() if q_lower in h['name'].lower()]
        return sorted(results, key=lambda x: x['streak'], reverse=True)

    def search_logs(self, query: str):
        if not self.daily_logs: return []
        q_lower = query.lower()
        results = [log for log in self.daily_logs 
                   if any(q_lower in field.lower() for field in ['date', 'note'])]
        return sorted(results, key=lambda x: x['date'], reverse=True)

    def add_habit(self, name: str):
        habit_id = len(self.habits) + 1
        self.habits[habit_id] = {"name": name, "streak": 0}
        return habit_id

    def complete_habit(self, habit_id: int, note: str = ""):
        if habit_id not in self.habits: raise ValueError("Habit not found")
        today_str = datetime.now().strftime("%Y-%m-%d")
        log_entry = {"date": today_str, "habit_id": habit_id, "note": note}
        self.daily_logs.append(log_entry)
        if not any(l["date"] == today_str and l["habit_id"] == habit_id for l in self.daily_logs):
            self.habits[habit_id]["streak"] += 1
        return log_entry

    def get_weekly_analytics(self, habit_id: int):
        if habit_id not in self.habits: raise ValueError("Habit not found")
        week_start = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        logs = [l for l in self.daily_logs 
                 if l["habit_id"] == habit_id and l["date"] >= week_start]
        completed_days = set(l["date"] for l in logs)
        total_days_in_week = (datetime.now() - datetime.strptime(week_start, "%Y-%m-%d")).days + 1
        completion_rate = len(completed_days) / total_days_in_week if total_days_in_week > 0 else 0.0
        return {"habit_id": habit_id, "completed_days": len(completed_days), 
                "completion_rate": round(completion_rate * 100, 2)}
