import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(ROOT_DIR, "logs")
LOG_FILE = os.path.join(ROOT_DIR, "execution.log")

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w'):
        pass