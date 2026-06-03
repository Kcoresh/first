# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: HabitCompass
import json
from datetime import datetime, timedelta

# --- Демонстрационные данные ---
DEMO_DATA = {
    "user": "Олег",
    "habits": [
        {"name": "Чтение", "streak": 5, "notes": {"2023-10-27": "Книга 'Атомные привычки'", "2023-10-28": "Глава 3"}}
    ],
    "analytics": {
        "week_start": "2023-10-23",
        "completed_days": ["2023-10-27", "2023-10-28"]
    }
}

# --- Точка входа и запуск ---
def main():
    print(f"Добро пожаловать, {DEMO_DATA['user']}!")
    print(f"Текущая серия: {DEMO_DATA['habits'][0]['streak']} дней.")
    print(f"Аналитика за неделю: {len(DEMO_DATA['analytics']['completed_days'])} выполненных дней.")
    print("Проект HabitCompass запущен.")

if __name__ == "__main__":
    main()
