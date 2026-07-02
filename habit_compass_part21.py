# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: HabitCompass
import datetime, json, os
from pathlib import Path

class ReminderManager:
    def __init__(self):
        self.data_file = "reminders.json"
        self.reminders = []
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump({"tasks": [], "completed": []}, f)

    def add_reminder(self, task_name: str, due_date_str: str):
        try:
            due = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
            self.reminders.append({"task": task_name, "due": due})
            self._save()
            return True
        except ValueError:
            print("Неверный формат даты. Используйте YYYY-MM-DD.")
            return False

    def _save(self):
        with open(self.data_file, 'w') as f:
            json.dump({"tasks": [r["task"] for r in self.reminders], "completed": []}, f)

    def check_and_notify(self):
        today = datetime.date.today()
        completed_tasks = set()
        for reminder in self.reminders.copy():
            if reminder["due"] == today and reminder["task"] not in completed_tasks:
                print(f"🔔 Напоминание: выполните '{reminder['task']}' сегодня!")
                completed_tasks.add(reminder["task"])
                self._save()
