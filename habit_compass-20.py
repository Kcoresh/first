# === Stage 20: Добавь восстановление записей из архива ===
# Project: HabitCompass
import json, os

ARCHIVE_FILE = "habits_archive.json"
DATA_FILE = "data.json"

def restore_from_archive():
    if not os.path.exists(ARCHIVE_FILE):
        return
    try:
        with open(ARCHIVE_FILE, 'r', encoding='utf-8') as f:
            archive_data = json.load(f)
        for habit_id, records in archive_data.items():
            if habit_id not in data.get('habits', {}):
                continue
            existing_records = data['habits'][habit_id].get('records', [])
            last_date = max((r['date'] for r in existing_records), default=None)
            new_records = [r for r in records if r['date'] > last_date]
            for rec in new_records:
                existing_records.append(rec)
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass
