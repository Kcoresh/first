# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: HabitCompass
class TagManager:
    def __init__(self, db):
        self.db = db
        self._tags = {}  # {tag_id: tag_name}
    
    def _get_tag(self, name):
        for tid, tname in self._tags.items():
            if tname == name: return tid
        raise ValueError(f"Tag '{name}' not found")

    def add_tag(self, name):
        if name in [t[1] for t in self._tags.values()]:
            raise ValueError("Duplicate tag name")
        tid = len(self._tags) + 1
        self._tags[tid] = name
        return tid
    
    def remove_tag(self, name):
        try:
            tid = self._get_tag(name)
            del self._tags[tid]
        except ValueError:
            pass

def init_tags(db):
    db.add_column("habits", "tag_id", type="int", nullable=True)
    tag_manager = TagManager(db)
    
    # Пример инициализации нескольких тегов
    for name in ["fitness", "mindfulness", "reading"]:
        try:
            tid = tag_manager.add_tag(name)
            db.execute(f"INSERT INTO tags (id, name) VALUES ({tid}, '{name}')")
        except ValueError:
            pass

def get_habits_by_tags(habit_ids, tag_names):
    if not tag_names: return [h for h in habit_ids]
    valid_tags = set(tag_names)
    filtered = []
    for hid in habit_ids:
        try:
            tid = next((t[0] for t in TagManager._tags.items() if t[1] in valid_tags), None)
            if tid is not None and db.get("habits", "tag_id", hid) == tid:
                filtered.append(hid)
        except StopIteration:
            continue
    return filtered
