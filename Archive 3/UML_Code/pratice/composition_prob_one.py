# Concept: Composition (whole-part, dependent lifecycle)
#Composition on the flipside is composition, where a part cannot exist without the whole or superclass 
#Task Create a computer class that creates and owns Component objects (e.g., GPU, CPU, RAM).



#The 'whole' class. It creates and owns its Computer objects.
class Computer:
    def __init__(self, name):
        self.name = name
        self.computers = []
        
    def addComponent(self, gpu_name:str, gpu_price: float, cpu_name: str, cpu_price: float, 
                     ram_name: str, ram_price: float, gb_total: int):
        gpu1 = GPU(gpu_name, gpu_price)
        cpu1 = CPU(cpu_name, cpu_price)
        ram1 = RAM(ram_name, ram_price, gb_total)   # **IMPORTANT**: Instantiating room inside of house
        #In computer science, instantiating means creating a specific, concrete instance (an object) from a general blueprint (a class)
        comp1 = {
            "GPU": gpu1, 
            "CPU": cpu1, 
            "RAM": ram1,
        }
        self.computers.append(comp1)
        
    def showComponents(self):
        print(f"\n --- {self.name.title()} ---")
        for computer in self.computers:
            for part_name, part_object in computer.items():
                print(f"{part_name}: {part_object}")
    def __del__(self):
        """This destructor is called when the Computer is destroyed."""
        
        print(f"\n --- The Computer at {self.name} is being destroyed! --- ")

#The 'part' class. Its lifecycle is tied to the Computer  
class GPU:
    def __init__(self, name: str, price: float):
        self.name = name 
        self.price = price
    def __str__(self):
        return f"{self.name.title()} (price: ${self.price})"
    def __del__(self):
        #This destructor will be called when the object is garbage collected.
        print(f"    (The {self.name} room is being destroyed...)")
    
class CPU: 
    def __init__(self, name: str, price: float):
        self.name = name 
        self.price = price
    def __str__(self):
        return f"{self.name.title()} (price: ${self.price})"
    def __del__(self):
        print(f"     The {self.name} CPU component is being destroyed... ")  
        
class RAM: 
    def __init__(self, name: str, price: float, gigabytes_total: int ):
        self.name = name 
        self.price = price 
        self.gigabytes_total = gigabytes_total
    def __str__(self):
        return f"{self.name} ({self.gigabytes_total} GB), price: ${self.price}"
    def __del__(self):
        print(f"     The {self.name} RAM component is being destroyed...")


print("--- 1. Creating the Computer (the 'whole')")

build1 = Computer("Build one")    

print("\n --- 2. The 'whole' (Computer) creates its 'parts' (Components: GPU, CPU and RAM)")

build1.addComponent("NVIDIA Founder Edition rtx 3080", 399.97, "Ryzen 9 5900x", 368.75, "Crucial DDR4-3200mhz", 145.99, 32)
build1.showComponents()

del build1

    
