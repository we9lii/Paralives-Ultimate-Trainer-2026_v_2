
import configparser
import os

def load_config(filename="config.ini"):
    config = configparser.ConfigParser()
    if not os.path.exists(filename):
        config["Settings"] = {
            "money_key": "f2",
            "needs_key": "f3",
            "wants_key": "f4",
            "skills_key": "f5",
            "age_key": "f6",
            "items_key": "f7",
            "unstuck_key": "f8",
            "exit_key": "f9"
        }
        with open(filename, "w") as f:
            config.write(f)
    else:
        config.read(filename)
    return config["Settings"]
