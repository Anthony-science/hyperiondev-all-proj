# Request times (int) in minutes for each event
swim_time = input("Enter the swimming time in minutes: ")
cycle_time = input("Enter the cycling time in minutes: ")
running_time = input("Enter the running time in minutes: ")
# Cast to int
swim_time = int(swim_time)
cycle_time = int(cycle_time)
running_time = int(running_time)
# Sum times, display
total_time = swim_time + cycle_time + running_time
## Set "if" conditions, followed by "elif" for each award, "else" for 111+ mins
if total_time <= 100:
    print("Provincial colours!")
elif total_time <=105:
    print("Provincial half colours!")
elif total_time <= 110:
    print("Provincial scroll!")
else: print("No award")
