#Name- Rishit Swain
#Regd. No.- 24E119F02
#Objective No.- 5(b)
# Define a function that eliminates the duplicate values in the list. Write a Python program
# that reads in ten integers, invokes the method, and displays the result.

def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

nums = []
print("Enter 10 integers:")
for i in range(10):
    n = int(input())
    nums.append(n)

result = remove_duplicates(nums)
print("List after removing duplicates:", result)


