# student_register.py

# Ask the user how many students are registering
num_students = int(input("How many students are registering for the exam venue? "))

# Open the file in write mode to clear previous content
with open("reg_form.txt", "w") as file:
    file.write("Students IDs for the exam.\n")
    # Loop through each student
    for i in range(num_students):
        student_id = input("Enter student ID for student {}: ".format(i+1))
        # Write the student ID to the file with a dotted line
        file.write(student_id + "\n")
        file.write("-" * len(student_id) + "\n")

print("Registration completed. Check reg_form.txt for the registration form.")
