# ITStudent.py

import random

class ITStudent:
    def __init__(self, name="", student_id="", programme=""):
        self.student_name = name
        self.student_id = student_id
        self.programme = programme
        self.courses_and_marks = {}

    def set_student_name(self, name):
        self.student_name = name

    def set_student_id(self, student_id):
        self.student_id = student_id

    def set_programme(self, programme):
        self.programme = programme

    def add_course(self, course_name, mark):
        self.courses_and_marks[course_name] = mark

    def get_student_name(self):
        return self.student_name

    def get_student_id(self):
        return self.student_id

    def get_programme(self):
        return self.programme

    def get_courses_and_marks(self):
        return self.courses_and_marks

    def calculate_average(self):
        if not self.courses_and_marks:
            return 0.0
        return sum(self.courses_and_marks.values()) / len(self.courses_and_marks)

    def has_passed(self):
        return self.calculate_average() >= 50

    def display(self):
        print(f"Student Name: {self.student_name}")
        print(f"Student ID: {self.student_id}")
        print(f"Programme: {self.programme}")
        print("Courses and Marks:")
        for course, mark in self.courses_and_marks.items():
            print(f"  {course}: {mark}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Status: {'Pass' if self.has_passed() else 'Fail'}")
        print()

    def generate_random_data(self):
        first_names = ["Anele", "Shadile", "Moonashe","Nkanyezi", "Lethukukhanya", "Zanele", "Precious", "Thandeka"]
        last_names = ["Ndwandwe", "Zwane", "Matsanura", "Mthethwa", "Mamba", "Gule", "Gina", "Jele"]
        self.student_name = random.choice(first_names) + " " + random.choice(last_names)

        
        self.student_id = "".join(str(random.randint(0, 9)) for _ in range(8))

        programmes = ["Computer Science", "Information Technology", "CyberSecurity", "Data Science"]
        self.programme = random.choice(programmes)

        courses = ["CSC493", "CSC461", "CSC301", "CSC411", "MAT101", "CSC400"]
        num_courses = random.randint(3, 6)
        selected_courses = random.sample(courses, num_courses)
        for course in selected_courses:

            self.add_course(course, random.randint(0, 100))
