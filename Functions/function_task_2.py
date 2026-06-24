# Write a function that returns both the sum and average of a list.
def sum_average():
    total_number=[2,3,4,5,6,7,8]
    sum_of= sum(total_number)
    print("Sum of this function is :", sum_of)
    average=sum_of/len(total_number) 
    print( "average of this function is : ", average)
sum_average()