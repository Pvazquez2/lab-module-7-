#Paola Vazquez
# february 27,2025
# Problem 3: Multiply all numbers in a list

def multiplyList(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Get user input for the list of numbers
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))  # Convert input into a list of integers

# Call function and print result
print(f"The product of the list {numbers} is: {multiplyList(numbers)}")
