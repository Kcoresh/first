# === Stage 17: Добавь группировку записей по категориям ===
# Project: HabitCompass
class CategoryManager:
    def __init__(self, storage):
        self.storage = storage
        self.categories = {}
    
    def load_categories(self):
        data = self.storage.get("categories", {})
        for cat_id, info in data.items():
            self.categories[cat_id] = {
                "id": cat_id,
                "name": info["name"],
                "color": info.get("color", "#ccc"),
                "icon": info.get("icon", "star")
            }
    
    def add_category(self, name, color=None):
        if not self.categories:
            self.load_categories()
        cat_id = f"cat_{len(self.categories) + 1}"
        entry = {
            "id": cat_id,
            "name": name,
            "color": color or "#ccc",
            "icon": "star"
        }
        self.categories[cat_id] = entry
        return cat_id
    
    def get_category_for_habit(self, habit_name):
        if not self.categories:
            self.load_categories()
        for cat in self.categories.values():
            if habit_name.lower().startswith(cat["name"].lower()):
                return cat
        return None

# Пример использования в коде трекинга привычек
def categorize_habit(habit_data):
    manager = CategoryManager(storage)
    category = manager.get_category_for_habit(habit_data['habit'])
    if not category:
        new_cat_id = manager.add_category(f"Категория для {habit_data['habit'][:5]}")
        category = manager.categories[new_cat_id]
    habit_data['category'] = category
    return habit_data
