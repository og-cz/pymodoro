list = ["11:00", "59:00", "60:00"]
error = ["1231:10", "100:-1", "61:00", "0:0", "0"]


def time_seperator(time):
    try:
        if ":" not in time:
            raise Exception('invalid formatting, missing ":"')

        minutes, seconds = time.rsplit(":", 1)
        minutes, seconds = int(minutes), int(seconds)

        if minutes == 0 and seconds == 0:
            raise Exception("invalid cannot put minutes and seconds as 0")
        if minutes < 0 or seconds < 0:
            raise Exception("Minutes or seconds cannot be negative")
        if minutes > 60 and seconds >= 60:
            raise Exception("minutes can be 0-69, seconds 0-59")

        return minutes, seconds
    except Exception as e:
        return ("time_seperator error at ", str(e))


for x in list:
    print(time_seperator(x))

for x in error:
    print(time_seperator(x))
