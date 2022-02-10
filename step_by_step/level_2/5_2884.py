time = input().split()

hour, min = int(time[0]), int(time[1])

min -= 45
if min  < 0:
    hour -= 1
    min += 60

if hour < 0 :
    hour += 24

print(hour, min)
