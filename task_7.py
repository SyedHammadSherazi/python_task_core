tupel1=("orange","mango")
list_tuple=list(tupel1)
list_tuple[1]="banana"
tupel1=tuple(list_tuple)
print(tupel1)
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])