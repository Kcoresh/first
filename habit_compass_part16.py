# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: HabitCompass
def calculate_monthly_stats(records):
    from datetime import date, timedelta
    
    if not records:
        return {}
    
    today = date.today()
    month_start = today.replace(day=1)
    stats = {d.strftime('%Y-%m'): {'completed': 0, 'total_days': 0} for d in range(month_start, (month_start + timedelta(days=32)).replace(day=1))}
    
    for rec in records:
        try:
            d = date.fromisoformat(rec['date'])
            if month_start <= d < stats.keys().__iter__().__next__() or d.month == today.month and d.year == today.year:
                key = d.strftime('%Y-%m')
                if key in stats:
                    stats[key]['completed'] += 1
        except (ValueError, KeyError):
            continue
            
    for month_key in stats:
        year_month = date.fromisoformat(month_key)
        current_year = today.year
        current_month = today.month
        
        while True:
            try:
                next_date = date(year=year_month.year, month=year_month.month + 1, day=1)
                if next_date > date(today.year, today.month, 1):
                    break
                stats[next_date.strftime('%Y-%m')]['total_days'] += 1
            except ValueError:
                break
                
    return {k: v for k, v in sorted(stats.items())}
