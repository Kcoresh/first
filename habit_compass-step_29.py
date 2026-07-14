# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: HabitCompass
def get_app_config():
    """Возвращает текущую конфигурацию приложения."""
    return {
        "app_name": "HabitCompass",
        "version": 29,
        "features": ["series", "notes", "weekly_analytics"],
        "settings": {}
    }

def set_app_config(config):
    """Записывает конфигурацию в файл и возвращает её."""
    with open("habitchompas.json", "w") as f:
        json.dump({"version": 29, **config}, f)
    return config
