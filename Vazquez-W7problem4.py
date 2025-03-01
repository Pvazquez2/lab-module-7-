# paola Vazquez
#worked on feb 27,2025
# Problem 4: Return a list with unique elements

def uniqueElements(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

# Get user input for the list of numbers
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))  # Convert input into a list of integers

# Call function and print result
print(f"Unique elements from the list {numbers}: {uniqueElements(numbers)}")
