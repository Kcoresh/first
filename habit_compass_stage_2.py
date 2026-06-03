# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: HabitCompass
class Habit:
    def __init__(self, name: str, streak: int = 0, notes: list = None):
        self.name = name
        self.streak = streak
        self.notes = notes or []

    def add_note(self, text: str) -> bool:
        if not isinstance(text, str) or len(text.strip()) == 0:
            return False
        self.notes.append(text.strip())
        return True

    def increment_streak(self) -> bool:
        if not self.name or not isinstance(self.name, str):
            return False
        self.streak += 1
        return True

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "streak": self.streak,
            "notes": self.notes
        }

def validate_input(name: str, text: str = None) -> tuple:
    if not isinstance(name, str) or len(name.strip()) == 0:
        return False, "Имя привычки должно быть непустой строкой."
    if text is not None:
        if not isinstance(text, str) or len(text.strip()) == 0:
            return False, "Заметка должна быть непустой строкой."
    return True, "Ввод корректен."
