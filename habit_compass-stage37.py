# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: HabitCompass
import unittest


class TestHabitCompass(unittest.TestCase):
    def setUp(self):
        from project import HabitCompassApp as app
        self.app = app()

    def test_initial_state_is_empty(self):
        self.assertEqual(len(self.app.habits), 0)
        self.assertEqual(len(self.app.notes), 0)
        self.assertIsNone(self.app.weekly_stats)

    def test_add_and_get_habit(self):
        self.app.add_habit("Дыхание")
        habits = self.app.get_habits()
        self.assertIn("Дыхание", habits)

    def test_mark_as_done(self):
        self.app.add_habit("Дыхание")
        self.app.mark_day(0, "Дыхание")
        stats = self.app.weekly_stats
        self.assertEqual(stats["Дыхание"], 1)

    def test_add_note(self):
        self.app.add_note(0, "Пробовал технику", "Дыхание")
        notes = self.app.get_notes()
        self.assertIn("Пробовал технику", notes)


if __name__ == "__main__":
    unittest.main()
