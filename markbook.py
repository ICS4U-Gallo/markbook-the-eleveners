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
# student_list: list[str]
# assignments_list: list[str]
# Assignments
# due: str
# name: str
# points: float


def create_student(first_name: str, last_name: str, gender: str, image: str, student_number: int, grade: int, email: str, mark:list, comments: str) -> Dict:
    """Creates a student dictionary"""
    return {}


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    classroomDict = {course_code, course_name, period, teacher}
    return classroomDict


def create_assignment(due: str, name: str, points: float):
    """Creates an assignment represented as a dictionary"""
    return {}


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    return 0
