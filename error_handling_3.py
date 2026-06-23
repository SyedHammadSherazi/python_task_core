#  Try to open a file that doesn't exist and handle the error gracefully. Medium

try:
   with open("contact1.txt", 'r') as f:
      print(f.read())
except:
  print("file cannot exist")