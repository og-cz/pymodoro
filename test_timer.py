import time
from multiprocessing import Process

"""state: running, paused, stopped"""
state = "running"
timer = 0


def number_to_minutes(t):
    minutes = t // 60
    second = t % 60
    return minutes, second


def countdown(t):

    while t > 0:
        if state == "running":
            min, sec = number_to_minutes(t)
            print(min, ":", sec)
            time.sleep(1)
            t -= 1
            timer = t
        elif state == "paused":
            res = input("press P to pause, S to Stop, C to continue: ").upper()
            if res == "C":
                state = "running"
            elif res == "P":
                state = "paused"
            elif res == "S":
                state = "Stopped"
        elif state == "stopped":
            timer = 0
            print("start again...")

    print("over!!")


def process_one(t):
    countdown(int(t))


def process_two():
    while timer > 0:
        res = input("press P to pause, S to Stop, C to continue: ").upper()
        if res == "C":
            state = "running"
        elif res == "P":
            state = "paused"
        elif res == "S":
            state = "stopped"


if __name__ == "__main__":
    t = input("enter a time: ")

    p1 = Process(target=process_one, args=t)
    p2 = Process(target=process_two)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("p1 and p2 is done")
