students = []

with open("names.csv") as file:
    for line in file:
        name , location = line.rstrip().split(",")
        student = {"name": name , "location": location}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} lives in {student['location']}")