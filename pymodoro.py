import threading
import time

c = threading.Condition()

TIMER = None
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
STATE = 1
SECONDS = 0

RUNNING = 1
PAUSED = 2
STOPPED = 3


def countdown_timer():
    global SECONDS
    while SECONDS > 0:
        if STATE == RUNNING:
            mins, secs = divmod(SECONDS, 60)
            print(f"{mins}:{secs}")
            time.sleep(1)
            SECONDS -= 1
        elif STATE == PAUSED:
            with c:
                c.wait()
        elif STATE == STOPPED:
            print("stopped")
            break
    print("countdown finished")


class Process_one(threading.Thread):
    def run(self):
        countdown_timer()


class Process_two(threading.Thread):
    def run(self):
        global STATE
        while SECONDS > 0 and STATE != 3:
            res = input(
                "press Enter+C to Continue, Enter+S to Stop, Enter+X to exit: "
            ).upper()
            with c:
                if res == "C":
                    STATE = RUNNING
                    c.notify()
                elif res == "S":
                    STATE = PAUSED
                elif res == "X":
                    STATE = STOPPED
                    c.notify()


if __name__ == "__main__":
    SECONDS = int(input("enter a time in seconds: "))
    t1 = Process_one()
    t2 = Process_two()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
