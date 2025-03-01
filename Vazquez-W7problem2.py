# paola Vazquez 
#February 26,2025

# Problem 2: Check if a number is in a given range

def checkRange(num):
    if num in range(1, 10):
        print(f"{num} is in the range.")
    else:
        print(f"{num} is not in the range.")

num_to_check = int (input("enter a number to a check (range 1-10): "))

checkRange(num_to_check)