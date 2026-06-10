# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: HabitCompass
def filter_records(records, filters=None):
    if filters is None:
        return records
    
    filtered = []
    for record in records:
        match = True
        if 'status' in filters and record.get('status') != filters['status']:
            match = False
        if 'category' in filters and record.get('category') != filters['category']:
            match = False
        if 'tags' in filters:
            if not isinstance(filters['tags'], list):
                filters['tags'] = [filters['tags']]
            if not any(tag in record.get('tags', []) for tag in filters['tags']):
                match = False
        if match:
            filtered.append(record)
    return filtered

# Пример использования:
# filtered_habits = filter_records(all_habits, {'status': 'active', 'category': 'health'})
