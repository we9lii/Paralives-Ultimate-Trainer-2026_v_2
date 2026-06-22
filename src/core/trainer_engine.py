
import time
from utils.logger import log_info

class TrainerEngine:
    def __init__(self):
        self.running = True
        self.addresses = {
            "money": 0x00PARA01,
            "needs": 0x00PARA02,
            "wants": 0x00PARA03,
            "skills": 0x00PARA04,
            "age": 0x00PARA05,
            "items": 0x00PARA06,
            "position": 0x00PARA07,
        }

    def write_memory(self, addr, value):
        pass

    def run(self, feature_manager):
        log_info("Trainer engine started")
        while self.running:
            if feature_manager.features.get("freeze_aging", False):
                self.write_memory(self.addresses["age"], 0)
            time.sleep(0.1)
