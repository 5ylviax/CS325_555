# Concept: Inheritance ("is-a relationship")
#Inheritance: a.k.a generalization, this is a relationship where subclass inherits attributes, methods
# and other relationships from super class 
# a solid line with an arrow head pointing to the parent class 

class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print(f"{self.year} {self.make.title()} {self.model.title()} engine has started!")
    def stop(self):
        print(f"{self.year} {self.make.title()} {self.model.title()} engine has stopped!")

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, doors: int, trunk_capacity: float):
        super().__init__(make, model, year)
        self.doors = doors
        self.trunk_capacity = trunk_capacity
        
    def get_doors(self):
        return self.doors
    
    # def add_trunk_capacity(self):
    #     print(f"{self.make.title()} {self.model.title()} trunk capacity: {self.trunk_capacity}")
        
        
class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, sidecar: bool):
        super().__init__(make, model, year)
        self.sidecar = sidecar
        
    # def add_sidecar(self):
        # if self.sidecar == False:
        #     print(f"{self.make.title()} {self.model.title()}: No sidecar")
        # else:
        #     print(f"{self.make.title()} {self.model.title()}: Sidecar available")
    
        
        
car1 = Car("ford","altima", 2025, 4, 15.6)
moto1 = Motorcycle("honda", "gold wing tour", 2025, False)

print(car1)
print(moto1)
car1.start()
car1.stop()

