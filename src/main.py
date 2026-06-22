
import sys
import time
import threading
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.trainer_engine import TrainerEngine
from core.feature_manager import FeatureManager
from utils.logger import log_info, log_success
from utils.config_loader import load_config
from utils.hotkey_manager import HotkeyManager
from gui.console_renderer import ConsoleRenderer

def main():
    load_config("config.ini")
    log_info("Paralives Ultimate Trainer v1.0 starting...")
    engine = TrainerEngine()
    feature_mgr = FeatureManager()
    hotkey_mgr = HotkeyManager()
    renderer = ConsoleRenderer()
    hotkey_mgr.register_hotkey('f1', lambda: renderer.toggle_menu())
    hotkey_mgr.register_hotkey('f2', lambda: feature_mgr.trigger('infinite_money'))
    hotkey_mgr.register_hotkey('f3', lambda: feature_mgr.trigger('max_needs'))
    hotkey_mgr.register_hotkey('f4', lambda: feature_mgr.trigger('complete_wants'))
    hotkey_mgr.register_hotkey('f5', lambda: feature_mgr.trigger('max_skills'))
    hotkey_mgr.register_hotkey('f6', lambda: feature_mgr.toggle('freeze_aging'))
    hotkey_mgr.register_hotkey('f7', lambda: feature_mgr.trigger('unlock_items'))
    hotkey_mgr.register_hotkey('f8', lambda: feature_mgr.trigger('unstuck'))
    hotkey_mgr.register_hotkey('f9', lambda: sys.exit(0))
    engine_thread = threading.Thread(target=engine.run, args=(feature_mgr,), daemon=True)
    engine_thread.start()
    log_success("Trainer ready. Press F1 for help, F9 to exit.")
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        log_info("Shutting down...")
        sys.exit(0)

if __name__ == "__main__":
    main()
