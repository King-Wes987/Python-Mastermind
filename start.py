import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

sys.path.append(resource_path('main_folder'))

from main_folder import run_game
from main_folder import button_gui
from main_folder import game_loop
#from main_folder import main
