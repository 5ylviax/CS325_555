import time 
##  Aggregation: a special type of association, aggregation is where one class contains, or is composed
# of, other classes. A whole and its parts 

class Professor:
    #The 'part' class. It can exist independently.
    def __init__(self, name):
        self.name = name
        print(f"    (Created {self})")

    def __str__(self):
        return f"Prof. {self.name}"

class Department:
    #The 'whole' class. It aggregates existing Professor objects.
    def __init__(self, name):
        self.name = name
        self.professors = []  # This list will hold *REFERENCES* NOT ACTUAL OBJECTS
        print(f"\nCreated Department: {self.name}")

    def add_professor(self, professor):
        """
        This method takes an *existing* Professor object and aggregates
        """
        print(f"  > Adding {professor} to the {self.name} department.")
        self.professors.append(professor)

    def show_professors(self):
        print(f"\n--- {self.name} Department Roster ---")
        for prof in self.professors:
            print(f"  - {prof}")
        print("-----------------------------------")

print("--- 1. Creating Professor objects (the 'parts') ---")
# The 'parts' are created first and exist independently.
prof1 = Professor("Igor Crk")
prof2 = Professor("John Matta")

print("\n--- 2. Creating the Department (the 'whole') ---")
cs_dept = Department("Computer Science")

print("\n--- 3. Aggregating the parts into the whole ---")
cs_dept.add_professor(prof1)
cs_dept.add_professor(prof2)

cs_dept.show_professors()

print(f"\n--- 4. Deleting the Department object '{cs_dept.name}' ---")
del cs_dept

# Wait a moment for any garbage collection messages (though not guaranteed)
time.sleep(0.1) 

print("\n--- 5. Checking if the Professor objects still exist ---")
print("The 'whole' (Department) is gone, but the 'parts' (Professors) remain.")
print(f"Object prof1 still exists: {prof1}")
print(f"Object prof2 still exists: {prof2}")