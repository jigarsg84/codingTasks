# dob_task.py

# Read data from the text file
with open('DOB.txt', 'r') as file:
    data = file.readlines()

# Split the data into names and birthdates
names = []
birthdates = []
for line in data:
    parts = line.strip().split(' ')
    names.append(parts[0] + " " + parts[1])
    birthdates.append(parts[2] + " " + parts[3] + " " + parts[4])

# Print out names
print("\nName\n")
for name in names:
    print(name)

print()

# Print out birthdates
print("\nBirthdate\n")
for birthdate in birthdates:
    print(birthdate)
