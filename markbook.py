"""
Markbook Application
Group members: Joseph, Joshua
"""
from typing import Dict
import json

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
            "student_list": {}, "assignment_list": []}


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""

    return sum(student["marks"]) / len(student["marks"])


def add_student_to_classroom(student, classroom):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """

    first_name = student["first_name"]
    last_name = student["last_name"]

    data[classroom]["student_list"][f"{first_name} {last_name}"] = None


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """

    del data[classroom]["student_list"][student]


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



# Loading in file

loading_file = True
tried_to_load = False

while loading_file:
    if tried_to_load == False:
        load_file = input("Would you like to load in a file?\n[Y]Yes [N]No\n").upper()

    if load_file == "Y":
        while loading_file:
            file_name = str(input("Please enter the file name, including the file type. (File must be in this folder.)\n"))
            try:
                with open(file_name, "r") as f:
                    data = json.load(f)
            except:
                print("\nFile does not exist in this folder.")
                load_file = input("Would you like to try again?\n[Y]Yes [N]No\n").upper()
                tried_to_load = True
                break
            else:
                print("\nInformation successfully loaded.")
                loading_file = False
      
    elif load_file == "N":
        data = {
                "student_List": [],
                "student_Data": {},
                "classroom_List": [], 
                "classroom_Data": {}
                }

        loading_file = False

# Menu    

print("\nWhat would you like to do?")

while True:
    try:
        category = int(input("\n [0] Create new information\n [1] Edit current information\n [2] Preview saved information\n [3] Exit\n"))
    except:
        print("\nPlease enter a number from the categories below.")
    else:
        if category not in range(0, 4):
            print("\nPlease enter a number from the categories below.")
        elif category == 0:
            while True:
                try:
                    selection = int(input("\n [0] Register Student\n [1] Create Classroom\n [2] Create Assignment\n [3] Back\n"))
                except:
                    print("\nPlease enter a number from the selection above.")
                else:
                    if selection not in range(0, 4):
                        print("\nPlease enter a number from the selection above.")
                    
                    elif selection == 0:
                        print("Register Student\n")

                        first_name = str(input("Enter the student's first name: "))
                        last_name = str(input("Enter the student's last name: "))
                        gender = str(input("Enter the student's gender: "))
                        image = str(input("Enter the student's image: "))
                        student_number = int(input("Enter the student's student number: "))
                        grade = int(input("Enter the student's grade: "))
                        email = str(input("Enter student's email: "))

                        full_name = f"{first_name} {last_name}"
                        data["student_Data"][full_name] = create_student(first_name, last_name, gender, image,
                                                                         student_number, grade, email)

                        data["student_List"].append(full_name)
                        

                    elif selection == 1:
                        print("Create Classroom\n")

                        course_code = str(input("Enter the course code: "))
                        course_name = str(input("Enter the course name: "))
                        period = int(input("Enter the period of the class: "))
                        teacher = str(input("Enter the name of the teacher: "))

                        data["classroom_Data"][course_code] = create_classroom(course_code, course_name, period, teacher)

                        data["classroom_List"].append(course_code)


                    elif selection == 2:
                        print("Create Assignment\n")
                        
                        class_code = str(input("Which class is this assignment for? (Please enter class code)\n"))
                        name = str(input("Enter the assignment title: "))
                        due = str(input("Enter the due date: "))
                        points = int(input("Enter how many points is the assignment worth: "))

                        assignment = create_assignment(name, due, points)
                        data["classroom_Data"][class_code]["assignment_list"].append(assignment)

                    
                    elif selection == 3:
                        break

        elif category == 1:
            while True:
                try:
                    selection = int(input("\n [0] Add Student to Classroom\n [1] Edit Student Information\n [2] Remove student from Classroom\n [3] Back\n"))
                except:
                    print("\nPlease enter a number from the selection above.")
                else:
                    if selection not in range(0, 4):
                        print("\nPlease enter a number from the selection above.")

                    elif selection == 0:
                        while True:
                            student = input("Which student would you like to change classes? (First and last name)\n")
                            if student in data["student_List"]:
                                break
                        
                        while True:
                            selected_class = input(f"\nWhich class would you like to put {student}? (Course code)\n")
                            if selected_class in data["classroom_List"]:
                                if student in data["classroom_Data"][selected_class]["student_list"].keys():
                                    print(f"\n{student} is already in this class.")
                                else:
                                    teacher = data["classroom_Data"][selected_class]["teacher"]
                                    period_num = data["classroom_Data"][selected_class]["period"]
                                    break

                        while True:
                            confirmation = input(f"\nAre you sure you want to put {student} in {selected_class} with {teacher} for period {period_num}?\n[Y]Yes [N]No\n").upper()
                            if confirmation == "Y":
                                add_student_to_classroom(student, selected_class)
                                print("\nStudent added to classroom.")
                                break
                            elif confirmation == "N":
                                secondary_confirmation = input("\nWould you like to discard changes?\n[Y]Yes [N]No\n").upper()
                                if secondary_confirmation == "Y":
                                    print("\nDiscarding changes...")
                                    break
        
                    elif selection == 1:
                        if len(data["student_List"]) != 0:
                            while True:
                                student = input("\nWhich student's information would you like to change? (First name and last name)\n")
                                if student in data["student_List"]:
                                    break
                                else:
                                    print("\nPlease enter a registered student.\n")

                            while True:
                                try:
                                    selection = int(input("What would you like to change?\n [0] First Name\n [1] Last Name\n [2] Gender\n [3] Image\n [4] Student Number\n [5] Grade\n [6] Email\n [7] Display Current Info\n"))
                                except:
                                    print("Please enter a number from the selection above.\n")
                                else:
                                    if selection not in range(0, 9):
                                        print("Please enter a number from the selection above.\n")
                                    elif selection == 0:
                                        while True:
                                            change = input(f"What would you like to change {student}'s first name to?\n")
                                            confirmation = input(f"Are you sure you want to change {student}'s first name to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                data["student_Data"][student]["first_name"] = change
                                                print("Successfully changed.")
                                            elif confirmation == "N":
                                                break


                                    elif selection == 1:
                                        while True:
                                            change = input(f"What would you like to change {student}'s last name to?\n")
                                            confirmation = input(f"Are you sure you want to change {student}'s last name to?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                data["student_Data"][student]["last_name"] = change
                                                print("Successfully changed.")
                                            elif confirmation == "N":
                                                break

                                    elif selection == 2:
                                        while True:
                                            change = input(f"What would you like to change {student}'s gender to?\n")
                                            confirmation = input(f"Are you sure you want to change {student}'s gender to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                data["student_Data"][student]["gender"] = change
                                                print("Successfully changed.")
                                            elif confirmation == "N":
                                                break

                                    elif selection == 3:
                                        while True:
                                            change = input(f"What would you like to change {student}'s image to?\n")
                                            confirmation = input(f"Are you sure you want to change {student}'s image to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                data["student_Data"][student]["image"] = change
                                                print("Successfully changed.")
                                            elif confirmation == "N":
                                                break

                                    elif selection == 4:
                                        while True:
                                            change = input(f"What would you like to change {student}'s student number to?\n")
                                            confirmation = input(f"Are you sure you want to change {student}'s student number to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                data["student_Data"][student]["student_number"] = change
                                                print("Successfully changed.")
                                            elif confirmation == "N":
                                                break

                                    elif selection == 5:
                                        while True:
                                            change = input(f"What would you like to change {student}'s grade to?\n")
                                            confirmation = input(f"Are you sure you want to change {student}'s grade to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                data["student_Data"][student]["grade"] = change
                                                print("Successfully changed.")
                                            elif confirmation == "N":
                                                break

                                    elif selection == 6:
                                        while True:
                                            change = input(f"What would you like to change {student}'s enail to?\n")
                                            confirmation = input(f"Are you sure you want to change {student}'s email to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                data["student_Data"][student]["email"] = change
                                                print("Successfully changed.")
                                            elif confirmation == "N":
                                                break

                                    elif selection == 7:
                                        while True:
                                            which_student = input(f"Which student would you like to view?\n")
                                            if which_student in data["student_Data"][student]:
                                                print(data["student_Data"][student]["first_name"],
                                                      data["student_Data"][student]["last_name"],
                                                      data["student_Data"][student]["gender"],
                                                      data["student_Data"][student]["image"],
                                                      data["student_Data"][student]["student_number"],
                                                      data["student_Data"][student]["grade"],
                                                      data["student_Data"][student]["email"])
                                            else:
                                                pass         

                        else:
                            print("\nThere are currently no registered students.")
                            break
                    elif selection == 2:
                        if len(data["classroom_List"]) != 0:
                            if len(data["student_List"]) != 0:
                                while True:
                                    selected_class = input("Which class would you like to choose? (Please enter the class code)\n")
                                    if selected_class in data["classroom_List"]:
                                        break

                                while True:
                                    student = input(f"Which student would you like to remove from {selected_class}? (Please enter student's first and last name)")
                                    if student not in data["student_List"]:
                                        print(f"There is no student by the name of {student} registered.")
                                    elif student not in data["classroom_Data"][selected_class]["student_list"]:
                                        print(f"{student} is not attending this class.")
                                    else:
                                        while True:
                                            confirmation = input(f"Are you sure you want to remove {student} from {selected_class}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                remove_student_from_classroom(student, selected_class)
                                                print("Student removed from class.")
                                                break
                                            elif confirmation == "N":
                                                break
                            else:
                                print("There are currently no registered students.")
                        else:
                            print("There are no classes currently running.")

                    elif selection == 3:
                        break

        elif category == 2:
            while True:
                try:
                    selection = int(input("\n [0] Student List\n [1] Classroom List\n [2] Student Average Mark\n [3] Class Average Mark\n [4] Back\n"))
                except:
                    print("\nPlease enter a number from the selection above.")
                else:
                    if selection not in range(0, 5):
                        print("\nPlease enter a number from the selection above.\n")

                    elif selection == 0:
                        for student in data["student_List"]:
                            print(student)

                    elif selection == 1:
                        for class_code in data["classroom_List"]:
                            print(class_code)

                    elif selection == 2:
                        pass
                    elif selection == 3:
                        pass
                    elif selection == 4:
                        break
        elif category == 3:
            save = input("Would you like to save the changes?\n[Y]Yes [N]No\n").upper()
            if save == "Y":
                if load_file == "N":
                    confirmation = "None"
                    while True:
                        if confirmation != "Y":
                            confirmation = "None"
                            file_name = str(input("What would you like to name the new file?\n"))
                            while confirmation != "Y" or confirmation != "N":
                                confirmation = input(f"Are you sure you want to save all changes in {file_name}.json?\n[Y]Yes [N]No\n").upper()

                        if ".json" not in file_name:
                            file_name += ".json"
                            break

                with open(file_name, "w") as f:
                    json.dump(data, f)
                
                print("Saved all changes.")
                exit()
            elif save == "N":
                while True:
                    secondary_confirmation = input("Are you sure you want to discard all the changes?\n[Y]Yes [N]No\n").upper()
                    if secondary_confirmation == "Y":
                        print("Discarding changes")
                        exit()
                    elif secondary_confirmation == "N":
                        break
