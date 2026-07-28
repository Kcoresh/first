# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: HabitCompass
def test_edge_cases():
    assert HabitTracker().next_series_id() == 1
    assert HabitTracker().current_week_day_name() == "Monday"
    assert HabitTracker().current_weekday_number() == 0
    assert HabitTracker().is_today() == False
    assert HabitTracker().last_completed_date_str() is None

    tracker = HabitTracker()
    today = Date.today()
    future = Date(today.year, today.month, today.day + 1)
    past = Date(today.year, today.month, today.day - 2) if today.day > 2 else Date(today.year, today.month, today.day)

    assert tracker.is_date_in_range(today, today) == True
    assert tracker.is_date_in_range(today, future) == True
    assert tracker.is_date_in_range(future, past) is None
    assert tracker.is_date_in_range(past, today) is None

    assert Date.today().is_leap_year(2000) == True
    assert Date.today().is_leap_year(1900) == False
    assert Date.today().is_leap_year(2024) == True
    assert Date.today().is_leap_year(2023) == False

    assert Date.today().days_in_month(2, 2024) == 29
    assert Date.today().days_in_month(1, 2024) == 31
    assert Date.today().days_in_month(2, 2023) == 28

    assert Date.today().day_of_week_name("Monday") == "Monday"
    assert Date.today().day_of_week_number("Monday") == 1

    assert Date.today().is_valid_date(2024, 2, 29) == True
    assert Date.today().is_valid_date(2023, 2, 29) == False
    assert Date.today().is_valid_date(2024, 13, 1) == False

    assert Date.today().days_from_start_of_week(today.weekday_number()) > 0 if today.weekday_number() != 0 else True
    assert Date.today().date_at_start_of_week() is not None

    assert Date.today().weekday_name(today.weekday_number()) == today.weekday_name()
    assert Date.today().weekday_number(today.weekday_name()) == today.weekday_number()
