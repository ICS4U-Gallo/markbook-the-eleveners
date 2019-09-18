"""
Markbook Application
Group members: Joshua, Joseph
"""
from typing import Dict

# Students:
# first_name: str
# last_name: str
# gender: str
# image: filepath: str
# student number: int
# grade: int
# email: str
# marks: list[float]
# comments: str
# Class
# course_code: str
# course_name: str
# period: int
# teacher_name: str
# student_list: list[dict]
# assignments_list: list[dict]
# Assignments
# due: str
# name: str
# points: int


def create_student(first_name: str, last_name: str,
                   gender: str, image: str,
                   student_number: int, grade: int,
                   email: str) -> Dict:
    """Creates a student dictionary"""
    return {"first_name": first_name, "last_name": last_name,
            "gender": gender, "image": image, "student_number":
            student_number, "grade": grade, "email": email}


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary

    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    return {"name": name, "due": due, "points": points}


def create_classroom(course_code: str, course_name: str,
                     period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""

    return {"course_code": course_code, "course_name": course_name,
            "period": period, "teacher": teacher,
            "student_list": [], "assignment_list": []}


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""

    return sum(student["marks"]) / len(student["marks"])


def add_student_to_classroom(student, classroom):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    classroom["student_list"].append("{} {}".format(
        student["first_name"], student["last_name"]))


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    classroom["student_list"].remove("{} {}".format(
        student["first_name"], student["last_name"]))


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be updated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    for data in kwargs.keys():
        student[data] = kwargs[data]


while True:
    print("Hello, what would you like to do?")

    try:
        selection = int(input(
            "\n Create Student[0]\n Create Assignment[1]\n Create Classroom[2]\n Calculate Average Mark[3]\n Add Student To Classroom[4]\n Remove Student From Classroom[5]\n Edit Student[6]\n "))
    except:
        print("Please enter a number from the selection above.")
    else:
        print("processing request...")

        if selection == 0:
            pass
        elif selection == 1:
            print("Create Assignment\n")

            name = str(input("Enter the assignment title: "))
            due = str(input("Enter the due date: "))
            points = int(
                input("Enter how many points the assignment is worth: "))

            assignment = create_assignment(name, due, points)

            print(assignment)

        elif selection == 2:
            # print("Create Classroom\n")

            # course_code = str(input("Enter the course code: "))
            # course_name = str(input("Enter the course name: "))
            # period = int(input("Enter the period of the class: "))
            # teacher = str(input("Enter the name of the teacher: "))

            # classroom = create_classroom(course_code, course_name, period, teacher)

            # print(classroom)
            pass

        elif selection == 3:
            pass
        elif selection == 4:
            pass
        elif selection == 5:
            pass
        elif selection == 6:
            pass
