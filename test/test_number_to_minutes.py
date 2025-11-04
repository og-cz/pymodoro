def number_to_minutes(t):
    return t // 60, t % 60


list = [120, 151, 123, 717, 23, 40, 60, 900, 240]

for x in list:
    print(number_to_minutes(x)[0], ":", number_to_minutes(x)[1])
