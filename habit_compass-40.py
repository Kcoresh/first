# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: HabitCompass
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="HabitCompass CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    
    cmd_track = sub.add_parser("track", help="Отметить привычку")
    cmd_track.add_argument("--habit", required=True, help="Имя привычки")
    cmd_track.add_argument("--date", default=None, help="Дата (YYYY-MM-DD)")
    
    cmd_stats = sub.add_parser("stats", help="Показать статистику")
    cmd_stats.add_argument("--days", type=int, default=7, help="Количество дней")
    cmd_stats.add_argument("--habit", help="Конкретная привычка")
    
    args = parser.parse_args()
    
    if hasattr(args, "command"):
        print(f"Команда: {args.command}")
        if hasattr(args, "habit"):
            print(f"Привычка: {args.habit}")
        if hasattr(args, "date"):
            print(f"Дата: {args.date}")
        if hasattr(args, "days"):
            print(f"Дней: {args.days}")

if __name__ == "__main__":
    main()
