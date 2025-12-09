# XMLHandler.py
from ITStudent import ITStudent
import xml.etree.ElementTree as ET
from io import StringIO

class XMLHandler:
    @staticmethod
    def wrap_to_xml(student, filename):
        try:
            root = ET.Element("ITStudent")
            ET.SubElement(root, "StudentName").text = student.get_student_name()
            ET.SubElement(root, "StudentID").text = student.get_student_id()
            ET.SubElement(root, "Programme").text = student.get_programme()
            courses = ET.SubElement(root, "Courses")
            for course, mark in student.get_courses_and_marks().items():
                course_elem = ET.SubElement(courses, "Course")
                ET.SubElement(course_elem, "Name").text = course
                ET.SubElement(course_elem, "Mark").text = str(mark)
            tree = ET.ElementTree(root)
            tree.write(filename, encoding="utf-8", xml_declaration=True)
            return True
        except Exception as e:
            print(f"Error wrapping to XML: {e}")
            return False

    @staticmethod
    def unwrap_from_xml(filename):
        student = ITStudent()
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            student.set_student_name(root.find("StudentName").text)
            student.set_student_id(root.find("StudentID").text)
            student.set_programme(root.find("Programme").text)
            courses = root.find("Courses")
            for course_elem in courses.findall("Course"):
                name = course_elem.find("Name").text
                mark = int(course_elem.find("Mark").text)
                student.add_course(name, mark)
            return student
        except Exception as e:
            print(f"Error unwrapping from XML: {e}")
            return student

    @staticmethod
    def generate_xml_string(student):
        root = ET.Element("ITStudent")
        ET.SubElement(root, "StudentName").text = student.get_student_name()
        ET.SubElement(root, "StudentID").text = student.get_student_id()
        ET.SubElement(root, "Programme").text = student.get_programme()
        courses = ET.SubElement(root, "Courses")
        for course, mark in student.get_courses_and_marks().items():
            course_elem = ET.SubElement(courses, "Course")
            ET.SubElement(course_elem, "Name").text = course
            ET.SubElement(course_elem, "Mark").text = str(mark)
        return ET.tostring(root, encoding="unicode")

    @staticmethod
    def parse_xml_string(xml_data):
        student = ITStudent()
        try:
            root = ET.fromstring(xml_data)
            student.set_student_name(root.find("StudentName").text)
            student.set_student_id(root.find("StudentID").text)
            student.set_programme(root.find("Programme").text)
            courses = root.find("Courses")
            for course_elem in courses.findall("Course"):
                name = course_elem.find("Name").text
                mark = int(course_elem.find("Mark").text)
                student.add_course(name, mark)
            return student
        except Exception as e:
            print(f"Error parsing XML string: {e}")
            return student