# 2 Build a logger that writes every action to a log file with a timestamp. Medium
import datetime

def add_logs(tasks):
    with open("actions.log", "a") as file:
        check_time = str(datetime.datetime.now())

        add_records = check_time + " - " + tasks

        file.write(add_records + "\n")


add_logs("Start the action")
add_logs("Open the App")
add_logs("close The action")