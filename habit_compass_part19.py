# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: HabitCompass
def archive_old_records(cutoff_date=None):
    if cutoff_date is None:
        from datetime import datetime, timedelta
        cutoff_date = datetime.now() - timedelta(days=365)
    
    archived_count = 0
    for record in records:
        if isinstance(record.get('created_at'), str):
            created_dt = datetime.fromisoformat(record['created_at'].replace('Z', '+00:00'))
        else:
            created_dt = record['created_at']
        
        if created_dt < cutoff_date and not record.get('archived'):
            record['archived'] = True
            archived_count += 1
    
    return archived_count
