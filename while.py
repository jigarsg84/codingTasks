# while.py

# Initialize variables
total = 0
count = 0

# Continually ask the user to enter a number
while True:
    enternum = input("Enter a number (or -1 to stop): ")
    
    # Check if the input is '-1' to stop the loop
    if enternum == '-1':
        break
    
    # Convert the input to a float
    enternum = float(enternum)
    
    # Add the number to the total and increment count
    total += enternum
    count += 1

# Calculate the average if at least one number was entered
if count > 0:
    average = total / count
    print("Average of the numbers entered (excluding -1):", average)
else:
    print("No numbers entered (excluding -1).")



