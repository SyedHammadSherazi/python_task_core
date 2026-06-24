#  Count how many lines and words are in a file. 
words_number=0
line_count=0
with open("Files ios/file_handling-file.txt") as f:
    
    for words in f:
        
        c_word= words.split()
        line_count +=1
        words_number += len(c_word)
print("words in files :", words_number)
print("line count :", line_count)
        
