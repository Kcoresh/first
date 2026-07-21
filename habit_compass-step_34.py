# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: HabitCompass
class HabitTemplate:
    def __init__(self, name, schedule=None):
        self.name = name
        self.schedule = schedule or []  # list of (weekday_idx, hour) tuples

    @classmethod
    def create(cls, name, schedule=None):
        return cls(name=name, schedule=schedule)

    def to_json(self):
        import json
        return json.dumps({"name": self.name, "schedule": self.schedule})


def load_templates(storage):
    if not hasattr(load_templates, "_templates"):
        load_templates._templates = []
    for line in storage.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        try:
            t = HabitTemplate.from_json(line)
            load_templates._templates.append(t)
        except Exception:
            pass
    return load_templates._templates


def apply_template(storage, template):
    new_line = f"# Template applied\n{template.to_json()}\n"
    if storage.endswith('\n'):
        return storage + new_line
    return storage + '\n' + new_line
