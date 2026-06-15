# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: HabitCompass
def export_state_to_json():
    import json
    from datetime import datetime, timedelta
    
    def serialize_date(dt):
        return dt.strftime("%Y-%m-%d") if dt else None
    
    serialized_data = {
        "app_name": "HabitCompass",
        "export_timestamp": serialize_date(datetime.now()),
        "habits": []
    }
    
    for habit in habits:
        habit_entry = {
            "id": habit["id"],
            "name": habit["name"],
            "streak_count": habit.get("streak", 0),
            "last_completed_date": serialize_date(habit.get("last_completed")),
            "notes": [note for note in habit.get("notes", []) if note.get("date")]
        }
        
        # Weekly analytics calculation
        current_week_start = datetime.now().replace(day=1) - timedelta(days=current_week_start.weekday())
        weekly_stats = {
            "completed_days": 0,
            "total_notes_count": 0
        }
        
        for day_offset in range(7):
            check_date = current_week_start + timedelta(days=day_offset)
            if habit_entry["last_completed_date"] and serialize_date(habit_entry["last_completed_date"]) == serialize_date(check_date):
                weekly_stats["completed_days"] += 1
            
            # Count notes for this week
            for note in habit.get("notes", []):
                if note.get("date") and check_date <= datetime.fromisoformat(note["date"].replace('Z', '+00:00')):
                    weekly_stats["total_notes_count"] += 1
        
        habit_entry["weekly_analytics"] = weekly_stats
        serialized_data["habits"].append(habit_entry)
    
    return json.dumps(serialized_data, indent=2, ensure_ascii=False)
