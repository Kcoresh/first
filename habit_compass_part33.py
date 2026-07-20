# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: HabitCompass
class UndoManager:
        MAX_UNDO = 5

        def __init__(self):
            self._stack = []

        def record(self, action_type, payload):
            if len(self._stack) >= self.MAX_UNDO:
                self._stack.pop(0)
            self._stack.append({"type": action_type, "payload": payload})

        def undo_last(self):
            if not self._stack:
                return None
            entry = self._stack.pop()
            return {"action": entry["type"], "undo_payload": entry["payload"]}

    # Примеры использования UndoManager в HabitCompass:
    # 1. При добавлении новой привычки записываем пустой список.
    # 2. При обновлении статуса серии (добавление/удаление дня) — сохраняем предыдущую серию.
    # 3. При изменении заметки по дню — запоминаем старое значение.
