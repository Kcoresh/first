# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: HabitCompass
def show_menu():
    print("\n=== HabitCompass Menu ===")
    print("1. Add new habit")
    print("2. View habits list")
    print("3. Mark today's habits as done")
    print("4. View weekly analytics")
    print("5. Exit")
    try:
        choice = input("Select an option (1-5): ").strip()
        return int(choice) if choice.isdigit() else None
    except ValueError:
        return None

if __name__ == "__main__":
    while True:
        opt = show_menu()
        if opt is None:
            print("Invalid input. Try again.")
            continue
        elif opt == 1:
            name = input("Habit name: ").strip() or "Unnamed"
            streak = int(input("Initial streak (days): ") or "0")
            notes = input("Notes (optional): ") or ""
            habits.append({"name": name, "streak": streak, "notes": notes})
            print(f"Habit '{name}' added.")
        elif opt == 2:
            if not habits:
                print("No habits yet.")
            else:
                for i, h in enumerate(habits):
                    print(f"{i+1}. {h['name']} (Streak: {h['streak']})")
        elif opt == 3:
            today = datetime.date.today().isoformat()
            if not habits:
                print("No habits to mark.")
            else:
                for h in habits:
                    if h["last_completed"] != today:
                        h["streak"] += 1
                        h["last_completed"] = today
                        h["notes"] = input(f"Notes for {h['name']} ({today}): ") or h.get("notes", "")
                print("Habits updated.")
        elif opt == 4:
            if not habits:
                print("No data for analytics.")
            else:
                # Simplified weekly stats logic placeholder
                print("Weekly summary generated (logic to be implemented).")
        elif opt == 5:
            print("Goodbye!")
            break
