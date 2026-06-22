#  Save a dictionary to a JSON file, then load it back and print it.

import json
student={
    "name" : "Hammad",
    "age"  : 26,
    "city"  : "Lahore"
}
with open("student_dis.json", 'w') as f:
    json.dump(student,f)

with open("student_dis.json", 'r') as f:
   student_show=json.load(f)
   print(student_show)
