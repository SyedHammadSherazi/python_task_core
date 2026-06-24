# Write a script that prints the name of any new file added to a folder (basic file
# monitoring).
import os
import time
def checking_curent_file():
    folder = "Automation_Pro"
    previous_file = set(os.listdir(folder))

    while True:
        
        time.sleep(1)
        

        currentfile = set(os.listdir(folder))
        new_files = currentfile - previous_file

        for file in new_files:
            print("New file is added:", file)

        previous_file = currentfile
# checking_curent_file()