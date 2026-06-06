# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: HabitCompass
def edit_habit_entry(habit_id, new_data):
    """
    Редактирует запись по habit_id.
    new_data: dict с полями 'name', 'date', 'note'.
    Если поля не указаны, оставляют старые значения.
    """
    if not isinstance(new_data, dict):
        raise ValueError("new_data должен быть словарем")

    # Ищем запись в списке записей (предполагается глобальная переменная habit_entries)
    for entry in habit_entries:
        if entry['id'] == habit_id:
            # Обновляем только указанные поля
            if 'name' in new_data:
                entry['name'] = new_data['name']
            if 'date' in new_data:
                entry['date'] = new_data['date']
            if 'note' in new_data:
                entry['note'] = new_data['note']
            return {"status": "success", "message": f"Запись #{habit_id} обновлена"}

    # Если запись не найдена
    return {"status": "error", "message": f"Запись с id={habit_id} не найдена"}
