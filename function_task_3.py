# 3 Write a function that takes a string and counts the vowels in it. 
def vowel_fun():

    alphabets_user=str(input("enter the string :"))
    alpha_string=alphabets_user.lower()
    count=0
    for vowel in alpha_string:
        if vowel=='a'or vowel =='e' or vowel =='i' or vowel =='o' or vowel =='u':
            count+=1
    if count==0:
                print("No vowel")
    else:
        print("Total numbers of vowels in ",  str(count))
vowel_fun()    
