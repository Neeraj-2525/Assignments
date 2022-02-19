# To make a time calculator by taking user input in milliseconds
# name:) NEERAJ

print("***TIME CALCULATOR***")
millisec = input("Enter time in milliseconds: ")
millisec = int(millisec)
seconds = (millisec / 1000) % 60                # seconds in n milliseconds
seconds = int(seconds)
minutes = (millisec / (1000 * 60)) % 60         # minutes in n milliseconds
minutes = int(minutes)
hours = (millisec / (1000 * 60 * 60)) % 24      # hours in n milliseconds

print("%d(hours):%d(mins):%d(sec)" % (hours, minutes, seconds))      # %d converts the decimal value to integer

