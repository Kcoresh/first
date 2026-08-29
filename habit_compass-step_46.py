# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: HabitCompass
import json
from pathlib import Path

PROJECT_FILE = Path(__file__).resolve()

SCHEMA_VERSION = 46

def migrate_habit_compass_schema():
    """Миграция структуры данных HabitCompass до версии 46."""
    data = {}
    if PROJECT_FILE.exists():
        with open(PROJECT_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        data = json.loads(content)
    else:
        data = {}

    if data.get("schema_version") < SCHEMA_VERSION:
        data["schema_version"] = SCHEMA_VERSION
        data.setdefault("habits", {})
        data.setdefault("days", {})
        data.setdefault("notes", {})
        data.setdefault("stats", {})

    with open(PROJECT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
