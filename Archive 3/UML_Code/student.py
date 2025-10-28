class Student:
    def __init__(self, student_id: str, name: str, email:str):
        self.student_id = student_id
        self.name = name
        self.email = email
        self._enrolled_courses = []

    def enroll_course(self,course):
        if course not in self._enrolled_courses:
            self._enrolled_courses.append(course)
            course._add_student(self)
            print(f"student {self.name} enrolled in {course.title}")
        else:
            print(f"Student {self.name} is already enrolled in {course.title}")

    def get_all_enrolled_courses(self):
        return [course.title for course in self._enrolled_courses]

class Course:
    def __init__(self, course_code: int, title: str, credits: float):
        self.course_code = course_code
        self.title = title
        self.credits =credits
        self._enrolled_students = []

    def _add_student(self,student):
        if student not in self._enrolled_students:
            self._enrolled_students.append(student)

    def get_all_enrolled_students(self):
        return [student.name for student in self._enrolled_students]

student1 = Student("800123456","Zach","zack@email.com")
student2 = Student("800343563", "Charlie", "charlie@email.com")

course1 = Course("cs325","Software Engineering",3)
course2 = Course("cs234","web dev",2)
course3 = Course("cs425","software design",2.5)

student1.enroll_course(course1)
student1.enroll_course(course2)

student2.enroll_course(course2)
student2.enroll_course(course3)

print(f"{student1.name} enrolled in: {student1.get_all_enrolled_courses()}")

print(f"{course2.title} has students: {course2.get_all_enrolled_students()}")

student1.enroll_course(course1)