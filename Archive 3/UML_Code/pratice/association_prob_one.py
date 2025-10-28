# Concept: Association (mutual relationship, no ownership)
# **Association** this is a relationship that indicates one class is related to another 
# but not necesarrily dependent
# A doctor treats a patient 
# -- a doctor can exist without a patient 
# -- a patient can exist without a doctor 

class Doctor:
    def __init__(self, name: str, specialization: str):
        self.name = name 
        self.specialization = specialization
        self.patients = [] # holds reference to Patient Objects 
    def add_patients(self, patient: 'Patient'):
        if patient not in self.patients:
            self.patients.append(patient)
            print(f"Dr. {self.name} is now seeing {patient.name}")
        else: 
            print(f"Dr. {self.name} already has {patient.name} as a patient.")
            
    def show_patients(self):
        for patient in self.patients:
            print(f"-{patient.name}, age: {patient.age}")
        if not self.patients:
            print(" (No patients yet)")
    
class Patient:
    def __init__(self, name: str, age: int):
        self.name = name 
        self.age = age 
        
    def visit_doctor(self, doctor: Doctor, room: str, time: str):
        print(f"{self.name} (age {self.age}) visits Dr. {doctor.name} in room {room} at {time}.")
        doctor.add_patients(self)

#create independent objects 

doc1 = Doctor("Smith", "Cardiology")
doc2 = Doctor("Lee", "Pediatrics")

pat1 = Patient("Alice", 29)
pat2 = Patient("Ben", 12)
pat3 = Patient("Carla", 45)

#Create associations (vists)

pat1.visit_doctor(doc1, "101A", "10:30 AM")
pat2.visit_doctor(doc2, "202B", "1:00 PM")
pat3.visit_doctor(doc1, "101A", "9:30 AM")

#show associations 

doc1.show_patients()
doc2.show_patients()
