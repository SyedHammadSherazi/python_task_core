# Write a function that returns both the sum and average of a list.

def sum_average():
    numbers = [2, 3, 4, 5, 6, 7, 8]
    total = sum(numbers)
    average = total / len(numbers)

    return total, average

total, average = sum_average()

print("Sum:", total)
print("Average:", average)
