#  Read a .txt file and show only the lines that contain a specific word.
with open("Files ios/file_handling-file.txt", 'r') as f:
    lines_spec=f.readlines()
    for lines_specific in lines_spec:
        if "file" in lines_specific:
            print(lines_specific)
        # else:
        #     print("No word Exist")
       