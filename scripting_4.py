# Make a "reminder" script that uses time.sleep() to print a message every X seconds
import time
def reminder_system():
    x=int(input ("the interval time:"))
    while True:
        time.sleep(x)
        print("Please take a water")
# reminder_system()