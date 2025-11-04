import time
from multiprocessing import Process, Value


start_time = time.time()
duration = 25 * 60


def number_to_minutes(t):
    return t // 60, t % 60


def countdown(t):
    while t > 0:
        min, sec = number_to_minutes(t)
        time.sleep(1)
        t -= 1
        return min, sec
    print("over!!")


def process_one(timer, state):
    timer.value
    while timer.value > 0:
        if state.value == 1:
            min, sec = number_to_minutes(timer.value)
            print(min, ":", sec)
            for _ in range(10):
                time.sleep(0.1)
                if state.value == 3:
                    print("stopped")
                    return
            timer.value -= 1
        elif state.value == 2:
            time.sleep(0.1)
        elif state.value == 3:
            print("stopped")
            break
    print("countdown finished")


if __name__ == "__main__":
    t = int(input("enter a timer in seconds: "))
    timer = Value("i", t)
    state = Value("i", 1)  # 1=running, 2=paused, 3=stopped

    p1 = Process(target=process_one, args=(timer, state))
    p1.start()

    while timer.value > 0 and state.value != 3:
        res = input("press P to pause, S to Stop, C to Continue: ").upper()
        if res == "C":
            state.value = 1
        elif res == "P":
            state.value = 2
        elif res == "S":
            state.value = 3
            break
    p1.join()
    print("p1 and p2 are done")
