import scripting_1
import scripting_2
import scrippting_3
import scripting_4
while True:
    print("\n====Cli_project_scripting====")
    print("1.File Monitering Syestem")
    print("2.Log System")
    print("3.Current File system")
    print("4.Reminder system")
    print("5.Exit")
    
    choise=(input("enter your choise:"))
    if choise=='1':
        scripting_1.manage_files()
        
    elif choise=='2':
        task=input("Enter the log message")
        scripting_2.add_logs(task)
    elif choise=='3':
        scrippting_3.checking_curent_file()
        
    elif choise=='4':
        scripting_4.reminder_system()
        
    elif choise=='5':
        print("existing")
        break
    else:
        print("invalid choice")