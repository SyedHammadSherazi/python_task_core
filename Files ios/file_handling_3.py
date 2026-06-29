#Take a name from the user and append it to a file (like a contact list)
#

with open("Files ios/contact.txt", 'a') as f:
    user_name= (input("Enter the user name:"))
    f.write("The user name is :" + user_name + "\n")
  
