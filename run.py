import sys
import os
import threading

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.runner import run
from bot.callback import run_callback_loop


if __name__ == "__main__":

    print("🚀 Bot started (single-user mode)")

    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run_callback_loop)

    t1.daemon = True
    t2.daemon = True

    t1.start()
    t2.start()

    t1.join()
    t2.join()