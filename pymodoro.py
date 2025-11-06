import threading
import time
import math

c = threading.Condition()

SECONDS = 0

# states of pymodoro
STATE = 1
RUNNING = 1
PAUSED = 2
STOPPED = 3


def countdown_timer():
    global SECONDS, STATE
    start_time = time.perf_counter()
    end_time = start_time + SECONDS

    while True:
        with c:
            if STATE == PAUSED:
                c.wait()
            if STATE == STOPPED:
                print("stopped")
                break

        remaining = end_time - time.perf_counter()
        if remaining <= 0:
            print("time's up!")
            with c:
                SECONDS = 0
                STATE = STOPPED
                c.notify_all()
            break
        secs_display = int(math.ceil(remaining))
        mins, secs = divmod(int(remaining), 60)
        print(f"{mins}:{secs:02d}")

        sleep_time = remaining - (secs_display - 1)
        if sleep_time <= 0:
            sleep_time = 0.05
        time.sleep(sleep_time)


class Process_one(threading.Thread):
    def run(self):
        countdown_timer()


class Process_two(threading.Thread):
    def run(self):
        global STATE
        while SECONDS > 0 and STATE != 3:
            res = input(
                "press EnterC to Continue, EnterS to Stop, EnterX to exit: "
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
        while True:
            res = input(
                "press EnterC to Continue, EnterS to Stop, EnterX to exit: "
            ).upper()
            with c:
                if res == "C":
                    STATE = RUNNING
                    c.notify_all()
                elif res == "S":
                    STATE = PAUSED
                elif res == "X":
                    STATE = STOPPED
                    c.notify_all()
                    break
            if STATE == STOPPED:
                break


if __name__ == "__main__":
    SECONDS = int(input("enter a time in seconds: "))
    t1 = Process_one()
    t2 = Process_two()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
