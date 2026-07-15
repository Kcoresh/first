# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: HabitCompass
class HabitCompass:
    def __init__(self):
        self.profiles = {}

    def register_profile(self, name, **kwargs):
        self.profiles[name] = kwargs
        return self.profiles[name]

    def get_active_profiles(self):
        return list(self.profiles.keys())
