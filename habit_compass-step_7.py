# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: HabitCompass
class HabitCompass:
    def __init__(self):
        self.records = []

    def add_record(self, name, priority, date_str, notes=""):
        record = {"name": name, "priority": int(priority), "date": date_str, "notes": notes}
        self.records.append(record)
        return len(self.records)

    def sort_records_by_date(self):
        self.records.sort(key=lambda x: x["date"])
        return self.records

    def sort_records_by_priority_desc(self):
        self.records.sort(key=lambda x: x["priority"], reverse=True)
        return self.records

    def sort_records_by_name_asc(self):
        self.records.sort(key=lambda x: x["name"].lower())
        return self.records

    def get_sorted_records(self, by="date"):
        if by == "date":
            return self.sort_records_by_date()
        elif by == "priority":
            return self.sort_records_by_priority_desc()
        else:
            return self.sort_records_by_name_asc()
