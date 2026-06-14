# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: HabitCompass
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        
        # Валидация структуры данных
        required_keys = ['user', 'habits']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Отсутствует обязательное поле: {key}")
            
            if isinstance(data[key], list):
                for item in data[key]:
                    if not isinstance(item, dict):
                        raise TypeError(f"Элемент списка '{key}' должен быть словарем")
        
        # Сохранение данных в переменную для использования остальным кодом
        global HABIT_COMPASS_DATA
        HABIT_COMPASS_DATA = data
        
        print("Начальные данные успешно загружены.")
        return data
    
    except json.JSONDecodeError as e:
        sys.stderr.write(f"Ошибка парсинга JSON: {e}\n")
        raise

# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    sample_json = '''
    {
      "user": {"id": 1, "name": "Алексей"},
      "habits": [
        {"id": 101, "title": "Спорт", "streak": 5},
        {"id": 102, "title": "Чтение", "streak": 2}
      ]
    }'''
    
    load_initial_data(sample_json)
