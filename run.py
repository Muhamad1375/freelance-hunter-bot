import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.runner import run
from bot.callback import run_callback_loop

import threading

if __name__ == "__main__":

    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run_callback_loop)

    t1.start()
    t2.start()

    t1.join()
    t2.join()