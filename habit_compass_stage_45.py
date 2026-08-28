# === Stage 45: Добавь восстановление из резервной копии ===
# Project: HabitCompass
import json, os, sys

def load_backup(source):
    try:
        with open(source, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_backup(data):
    path = "habit_compass_backup.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path

def restore_backup(source=None):
    data = load_backup(source)
    if data is None:
        print("Резервная копия не найдена или повреждена.")
        return False
    try:
        with open("habit_compass_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Резервная копия восстановлена из {source or 'habit_compass_backup.json'}.")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False

def list_backups():
    backups = []
    for name in ("habit_compass_backup.json", "habit_compass_backup_*.json"):
        pattern = name.replace("*", "**")
        matches = [f for f in os.listdir(".") if f.startswith(name.replace("*", ""))]
        backups.extend(matches)
    return sorted(set(backups))

def main():
    if len(sys.argv) < 2:
        print("Использование: python -m habit_compass backup restore [путь_к_файлу]")
        return
    cmd = sys.argv[1]
    if cmd == "restore":
        path = sys.argv[2] if len(sys.argv) > 2 else None
        restore_backup(path)
    elif cmd == "list":
        print("Доступные резервные копии:", list_backups())
    elif cmd == "save":
        save_backup()
    else:
        print(f"Неизвестная команда: {cmd}")

if __name__ == "__main__":
    main()
