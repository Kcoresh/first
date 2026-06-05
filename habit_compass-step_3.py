# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: HabitCompass
class HabitCompass:
    def __init__(self):
        self.records = []

    def add_record(self, habit_name, date, completed, note=""):
        record = {
            "habit": habit_name,
            "date": date,
            "completed": completed,
            "note": note
        }
        self.records.append(record)
        return record

    def get_weekly_stats(self):
        today = datetime.date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        
        week_records = [r for r in self.records if week_start <= r["date"] <= week_end]
        
        stats = {}
        for record in week_records:
            habit = record["habit"]
            if habit not in stats:
                stats[habit] = {"completed": 0, "total_days": 0}
            
            if record["completed"]:
                stats[habit]["completed"] += 1
            
            # Упрощённая логика подсчёта дней в неделю для конкретного привычка
            # В реальном проекте нужно учитывать все дни недели, даже без записей
            pass 
        
        return stats

# Пример использования
if __name__ == "__main__":
    app = HabitCompass()
    app.add_record("Спорт", datetime.date.today(), True, "Бег 5км")
    print(f"Добавлено: {app.records[-1]}")
