# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: HabitCompass
def demo_commands():
    """Demo commands for quick manual testing."""
    print("=== HabitCompass Demo Commands ===")
    
    # Command 1: Add a habit
    add_habit("Exercise", "2025-06-20")
    print(f"Added 'Exercise' habit on {date.today().strftime('%Y-%m-%d')}")

    # Command 2: Log completion for today
    log_completion("Exercise", date.today())
    print(f"Logged completion of 'Exercise' for {date.today()}")

    # Command 3: Add a note for today's entry
    add_note("Felt great after morning run!", "Exercise", date.today())
    print(f"Added note to today's 'Exercise' entry")

    # Command 4: Get weekly analytics summary
    week_start = (date.today() - timedelta(days=6)).strftime("%Y-%m-%d")
    week_end = date.today().strftime("%Y-%m-%d")
    print(f"Weekly analytics for {week_start} to {week_end}:")
    show_weekly_analytics(week_start, week_end)

    # Command 5: Get habit streaks
    all_habits = get_all_habits()
    if all_habits:
        print("\nHabit streaks:")
        for habit_id in all_habits:
            habit = get_habit(habit_id)
            if habit:
                print(f"  {habit['name']}: {get_streak_count(habit_id)} days")

    # Command 6: Delete a habit (cleanup demo)
    if "Exercise" in get_all_habits():
        delete_habit_by_name("Exercise")
        print("\nDeleted 'Exercise' habit for cleanup")

    print("\n=== Demo commands completed ===")
