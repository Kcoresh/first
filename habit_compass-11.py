# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: HabitCompass
import json, os, sys
DATA_FILE = "habits.json"
def save_data(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[Error] Failed to save data: {e}")
        return False

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"habits": [], "streaks": {}, "notes": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Ensure structure integrity on load
            if not all(k in data for k in ["habits", "streaks", "notes"]):
                return {"habits": [], "streaks": {}, "notes": []}
        return data
    except Exception as e:
        print(f"[Error] Failed to load data: {e}")
        return {"habits": [], "streaks": {}, "notes": []}

def main():
    # Initialize or load existing data
    if len(sys.argv) > 1 and sys.argv[1] == "--init":
        initial_data = {"habits": [], "streaks": {}, "notes": []}
        save_data(initial_data)
        print("HabitCompass initialized.")
        return

    # Load current state (simulated usage pattern)
    data = load_data()
    
    # Example: Add a new habit and note to demonstrate persistence logic
    if len(sys.argv) > 2:
        habit_name = sys.argv[1]
        day_note = sys.argv[2] if len(sys.argv) > 3 else ""
        
        # Update streaks (mocking daily check-in)
        today_str = "today"
        data["streaks"][habit_name] = data["streaks"].get(habit_name, 0) + 1
        
        # Add note for the day
        if habit_name not in data["habits"]:
            data["habits"].append({"name": habit_name})
        
        notes_key = f"{habit_name}_{today_str}"
        data["notes"][notes_key] = day_note
        
        save_data(data)
        print(f"Updated: {habit_name} ({data['streaks'][habit_name]} streak).")

if __name__ == "__main__":
    main()
