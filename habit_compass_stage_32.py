# === Stage 32: Добавь журнал действий пользователя ===
# Project: HabitCompass
class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, user, action, detail=""):
        entry = {"user": user, "action": action, "detail": detail, "timestamp": datetime.now()}
        self._entries.append(entry)
        return entry

    @property
    def entries(self):
        return list(self._entries)

    def by_user(self, user):
        return [e for e in self._entries if e["user"] == user]

    def recent(self, limit=10):
        return list(reversed(self._entries[-limit:]))

    def summary(self, days=-7):
        cutoff = (datetime.now() + timedelta(days=days)).replace(hour=0, minute=0, second=0)
        return [e for e in self._entries if datetime.combine(e["timestamp"].date(), time(0)) >= cutoff]

    @staticmethod
    def clear_all():
        ActionLog._all_logs = []
