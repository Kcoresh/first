# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: HabitCompass
import json, os

def load_habits_from_file(filepath: str) -> list[dict]:
    if not os.path.exists(filepath):
        print(f"Файл {filepath} не найден.")
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            print(f"Загружено {len(data)} привычек из {filepath}.")
            return data
        elif isinstance(data, dict) and "habits" in data:
            habits = data["habits"]
            print(f"Загружено {len(habits)} привычек (из объекта).")
            return habits
        else:
            print("Неверный формат JSON файла.")
            return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
    except PermissionError:
        print("Нет прав на чтение файла.")
        return []
