# Concept: Aggregation (whole - part, but independent parts)
import time 
 
class Course:
    #The 'part' class. It can exist independently
    def __init__(self, title: str, code: str, instructor: str):
        self.title = title
        self.code = code
        self.instructor = instructor
        
        print(f"      (Created {self})")
    def __str__(self):
        return f"{self.code}: {self.title} (Instructor: {self.instructor})"


class Department:
    #The 'whole' class. It aggregates existing University objects
    def __init__(self, name: str):
        self.name = name
        self.courses = []# This list will hold *REFERENCES* NOT ACTUAL OBJECTS
        print(f"\nCreated Department: {self.name}")
        
    def addCourse(self, course):
        print(f"  > Adding {course} to the {self.name} department.")
        self.courses.append(course)

    def showCourses(self):
        print(f"\n--- {self.name} University Courses ---")
        
        for course in self.courses:
            print(f" - {course}")
            # print(f"Title: {course.title}, Code: {course.code}, Instructor: {course.instructor.title}")
        print("-------------------------------------")
            
        # for course in self.courses:
        #     for key, value in course.items():
        #         print(f"\n{key.title()}: {value.title()}")
                

# print("--- 1. Creating Course Object (the 'parts') ---")

course1 = Course("Algorithm and Data structures", "CS340", "Xu")
course2 = Course("Introduction to Computing 1", "CS140", "Klein")

# print("\n --- 2. Creating the Department (the 'whole') ---")
dep1 = Department("Computer Science")

# print("\n--- 3. Aggregating the parts into the whole ---")
dep1.addCourse(course1)
dep1.addCourse(course2)



# print(f"\n--- 4. Deleting the Department Object '{dep1.name}'---")

# del dep1

# wait a moment for any garbage collection messages (though not guarenteed)
time.sleep(0.1)

dep2 = Department("Business Administration")

course3 = Course("Introduction to Programming Logic with Python", "CMIS130", "LaFreniere, Jill")

dep2.addCourse(course3)

dep3 = Department("Spanish")
course4 = Course("Intermediate Spanish", "SPAN201", "Licon Oppenheimer, Jose")
dep3.addCourse(course4)

dep1.showCourses()
dep2.showCourses()
dep3.showCourses()



