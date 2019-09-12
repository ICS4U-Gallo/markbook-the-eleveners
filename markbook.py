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
# points: float


def create_student(first_name: str, last_name: str,
                   gender: str, image: str,
                   student_number: int, grade: int,
                   email: str) -> Dict:
    """Creates a student dictionary"""
    return {first_name, last_name,  gender, image,
            student_number, grade, email}


def create_classroom(course_code: str,
                     course_name: str, period: int,
                     teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    return {course_code, course_name, period, teacher}


def create_assignment(due: str, name: str,
                      points: float):
    """Creates an assignment represented as a
    dictionary"""
    return {due, name, points}


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    return 0


print(create_student("Joshua", "Chuang", "Male",
                     "Image", 6479299892, 11,
                     "joshthegreatsayshi@gmail.com"))
