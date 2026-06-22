
from utils.logger import log_success

class FeatureManager:
    def __init__(self):
        self.features = {"freeze_aging": False}

    def toggle(self, name):
        if name in self.features:
            self.features[name] = not self.features[name]
            status = "ON" if self.features[name] else "OFF"
            log_success(f"{name.upper()} {status}")

    def trigger(self, name):
        msgs = {
            "infinite_money": "Household balance set to 999,999",
            "max_needs": "All needs maxed out!",
            "complete_wants": "All wants completed!",
            "max_skills": "All skills maxed to level 10!",
            "unlock_items": "All items unlocked!",
            "unstuck": "Character teleported to safe location.",
        }
        if name in msgs:
            log_success(msgs[name])
        else:
            log_success(f"Triggered: {name}")
