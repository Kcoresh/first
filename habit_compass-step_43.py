# === Stage 43: Добавь пагинацию длинных списков ===
# Project: HabitCompass
def paginate(self, items, page_size=10):
        """Compact paginator: yields (start, end) slices."""
        for start in range(0, len(items), page_size):
            yield items[start:start + page_size]
