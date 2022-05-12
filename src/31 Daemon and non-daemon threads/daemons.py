# Non-daemon: Blocks main programme -> all non-daemon threads should complete
# their work before programme ends

# Daemon: Background thread. Programme can exit even if thread hasn't finished

import time
import threading

def daemon():
    print("In daemon")
    time.sleep(5)
    print("Out of daemon")


def non_daemon():
    print("In non-daemon")
    time.sleep(2)
    print("Out of non-daemon")


if __name__ == "__main__":
    d = threading.Thread(target=daemon)
    d.setDaemon(True)
    nd = threading.Thread(target=non_daemon)

    d.start()
    nd.start()

    d.join(timeout=3)

