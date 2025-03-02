"""
COMP.CS.100 Project: Course Registry
This program helps a student selecting suitable courses to enroll
Creator: Thanh Tuyen Truong <thanhtuyen.truong@tuni.fi>
Student id number: 153156296
"""

# Funtion to load courses from a file
def load_courses(filename):
    """
    Try to load data from a text file.

    :param filename: str, the name of the file containing the data
    :return: dict, a dictionary of lists, where the keys are the departments
            and the values are lists containing the departments'courses and
            credits
    """
    try:
        # Try to open the file for reading of the data
        file = open(filename, mode = "r")

        # Dictionary to store departments, their courses, and credits
        departments = {}

        for line in file:
            # Remove the characters that end the line
            line = line.rstrip()

            # Split the line into departments, courses, and credits
            fields = line.split(";")

            # Check that each line has exactly 3 fields
            if len(fields) != 3:
                print("Error in file!")
                return None

            # Put the data in fields into departments, course name, and credits
            department, course_name, credit_points = fields

            # Credit points should be integers
            credit_points = int(credit_points)

            # Add the course to the apartment
            if department not in departments:
                departments[department] = []

            departments[department].append((course_name, credit_points))

        return departments

    except OSError:
        print("Error opening file!")
        return None

# Function to add a course to a department
def add_course(departments, text):
    """
    Adds a new course to a department. If the department doesn't exist, it creates it.

    :param departments: a dictionary to store departments, their courses, and credits
    :param text: the user's input so that a course or a department can be added to the dictionary

    """
    # Extract the department and credit points
    department = text[1]

    # Convert last element to integer for credits
    credit_points = int(text[-1])

    # Concatenate the words in between to form the course name
    course_name = " ".join(text[2:-1])

    # If department exists, add the course
    if department in departments:
        print(f"Added course {course_name} to department {department}")
        departments[department].append((course_name, credit_points))
    else:
        # If department doesn't exist, create it and add the course
        departments[department] = [(course_name, credit_points)]
        print(f"Added department {department} with course {course_name}")

# Function to delete a department or a specific course
def delete(departments, department, course_name=None):
    """
    delete a department or a specific course

    :param departments: a dictionary to store departments, their courses, and credits
    :param department: str the department to be deleted
    :param course_name: str the course name to be deleted

    """
    if department not in departments:
        print(f"Department {department} not found!")
        return

    # If a course name is provided, delete the course
    if course_name:
        # Check if the course is in the department
        for course in departments[department]:
            if course[0] == course_name:
                departments[department].remove(course)
                print(f"Department {department} course {course_name} removed.")
                return

        # If the course was not in the department, print error message
        print(f"Course {course_name} from {department} not found!")

    # If a course name is not provided, then delete the whole department
    else:
        del departments[department]
        print(f"Department {department} removed.")

# Function to print all departments and their courses
def print_all(departments):
    """
    print all departments and their courses

    :param departments: a dictionary to store departments, their courses, and credits

    """
    for department, courses in sorted(departments.items()):
        print(f"*{department}*")
        for course_name, credit_points in sorted(courses):
            print(f"{course_name} : {credit_points} cr")

# Function to print courses for a specific department
def print_department(departments, department):
    """
    print courses for a specific department

    :param departments: a dictionary to store departments, their courses, and credits
    :param department: str the department in which all courses and credits will be printed out

    """
    if department in departments:
        print(f"*{department}*")
        for course_name, credit_points in sorted(departments[department]):
            print(f"{course_name} : {credit_points} cr")
    else:
        print("Department not found!")

# Function to calculate and print total credit points for a department.
def department_credits(departments, department):
    """
    calculate and print total credit points for a department.

    :param departments: a dictionary to store departments, their courses, and credits
    :param department: str the department in which all credits will be sum up

    """
    if department in departments:
        total_credits = sum(course[1] for course in departments[department])
        print(f"Department {department} has to offer {total_credits} cr.")
    else:
        print("Department not found!")

def main():
    filename = input("Enter file name: ")
    print()

    departments = load_courses(filename)

    if departments is None:
        return

    while True:
        command = input("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department / [Q]uit\nEnter command: ")
        print()

        # Handle add command
        if command.startswith("a "):
            parts = command.split()
            if len(parts) < 4:
                print("Invalid command!")
                continue
            add_course(departments, parts)
            print()

        # Handle credit command
        elif command.startswith("c "):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                department = parts[1]
                department_credits(departments, department)
                print()

        # Handle delete command
        elif command.startswith("d "):
            parts = command.split(maxsplit=2)
            if len(parts) == 2:
                department = parts[1]
                delete(departments, department)
            elif len(parts) == 3:
                department, course_name = parts[1], parts[2]
                delete(departments, department, course_name)
            print()

        # Handle print all command
        elif command == "p":
            print_all(departments)
            print()

        # Handle print a specific department command
        elif command.startswith("r "):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                department = parts[1]
                print_department(departments, department)
                print()

        # Handle quit command
        elif command == "q":
            print("Ending program.")
            break

        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()