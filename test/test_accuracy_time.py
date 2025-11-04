import time

TIMER = None
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0


def countdown_timer(seconds):
    start_time = time.perf_counter()
    end_time = start_time + seconds

    while time.perf_counter() < end_time:
        remaining = end_time - time.perf_counter()
        mins, secs = divmod(int(remaining), 60)
        print(mins, ":", secs)
        time.sleep(0.5)

    print("time`s up!")


countdown_timer(100)
