# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: HabitCompass
import json, os

def backup_data_file(path: str, backup_dir: str = "backups") -> str:
    if not os.path.isdir(backup_dir):
        os.makedirs(backup_dir)
    stem = os.path.splitext(os.path.basename(path))[0]
    ext = os.path.splitext(path)[1] or ".json"
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    dst = os.path.join(backup_dir, f"{stem}_{timestamp}{ext}")
    shutil.copy2(path, dst)
    return dst
