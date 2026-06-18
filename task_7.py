# Find the largest and smallest number in a list — first with max()/min(), then without
# them
number_largest=[1, 2, 3, 55, 69]

max1 = number_largest[0]
min1 = number_largest[0]
for num in number_largest:
  if num>max1:
   max1 = num
print("the maximum value is : ", max1)

for mins in number_largest:
  if mins<min1:
   min1 = mins
print("the minimum value is : ", min1)

  

print("using with min and max function")

number_largest1=[23,44,55]
nums=max(number_largest1)
print("The maximum value is :",nums)
number_largest2=[2,2,1,0,100,-1]
numbers=min(number_largest2)
print("minimum value is:", numbers)