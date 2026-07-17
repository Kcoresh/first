# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: HabitCompass
import json, os

PROFILES_PATH = "profiles.json"

def load_profiles():
    if not os.path.exists(PROFILES_PATH):
        return [{"name": "Default", "active": True}]
    with open(PROFILES_PATH) as f:
        data = json.load(f)
    for p in data:
        if isinstance(p, dict):
            p["active"] = p.get("active", False)
    return data

def save_profiles(profiles):
    with open(PROFILES_PATH, "w") as f:
        json.dump(profiles, f, indent=2)

def switch_profile(name):
    profiles = load_profiles()
    for p in profiles:
        if isinstance(p, dict) and p["name"].lower() == name.lower():
            p["active"] = True
            save_profiles(profiles)
            return True
    print(f"Profile '{name}' not found.")
    return False

def get_active_profile():
    profiles = load_profiles()
    for p in profiles:
        if isinstance(p, dict) and p.get("active"):
            return p
    return profiles[0] if profiles else None
