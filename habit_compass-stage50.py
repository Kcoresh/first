# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: HabitCompass
from datetime import date, timedelta

def _week_range():
    """Return (monday, sunday) dates for the week containing today."""
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    return monday, sunday

def _week_summary(records):
    """Produce a compact weekly summary: per-day hit counts and total streak."""
    mon, sun = _week_range()
    counts = {mon: 0, mon + timedelta(days=1): 0, mon + timedelta(days=2): 0,
              mon + timedelta(days=3): 0, mon + timedelta(days=4): 0,
              mon + timedelta(days=5): 0, mon + timedelta(days=6): 0,
              mon + timedelta(days=7): 0}
    for rec in records:
        d = rec["completed_at"]
        if mon <= d <= sun:
            counts[d] = counts.get(d, 0) + 1
    return counts

def _pretty_weekly(counts):
    """Format weekly counts as a short readable string."""
    mon, sun = _week_range()
    parts = []
    for d in range(7):
        day_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][d]
        parts.append(f"{day_name}: {counts[mon + timedelta(days=d)]}")
    return ", ".join(parts)

def _streak_length(completed_dates):
    """Calculate the current streak from a sorted list of completed dates."""
    if not completed_dates:
        return 0
    streak = 1
    for i in range(1, len(completed_dates)):
        if (completed_dates[i] - completed_dates[i - 1]).days != 1:
            break
        streak += 1
    return streak
