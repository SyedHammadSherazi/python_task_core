# Build a dictionary of student names and marks, then calculate the average.
student={
    "Ahsan" : 400,
    "Ali" : 300,
    "Ahmad" : 250
}
All_marks= (student["Ali"] + student["Ahmad"] + student["Ahsan"])
print("students name and marks: " , student )
print("Total marks", All_marks)
Avg_marks=All_marks/len(student)

print("average marks of all student  : ", Avg_marks)
# print("All marks average is : " , Total_marks)