# Write a script that moves all files in a folder into subfolders by type (images, docs,
# etc.).
import os
# os.mkdir("Automation_Pro")
import shutil
def manage_files():
        listing=os.listdir("Automation_Pro")
        # os.makedirs("Automation_Pro/Images")
        # os.makedirs("Automation_Pro/Documents")
        #print(listing)
        for Automation_file in listing:
                # print("Automation Folder showes this : ",Automation_file)
                extention_check=  os.path.splitext(Automation_file)
                # print("This file Extention is :",extention_check)
                images_extention=['.jpg','.png','.jpeg']
                pdf_extention=('.pdf','.docx','.txt')
                if extention_check[1] in images_extention:
                #  print("This file is exist in ",Automation_file)
                        shutil.move("Automation_Pro/" + Automation_file,"Automation_Pro/Images/" + Automation_file)
                elif extention_check[1] in pdf_extention:
                #  print("This is Documents file :", Automation_file)
                        shutil.move("Automation_Pro/" + Automation_file ,"Automation_Pro/Documents/" + Automation_file)
manage_files()