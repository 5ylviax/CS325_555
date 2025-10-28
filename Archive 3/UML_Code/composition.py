import time

class Room:
    #The 'part' class. Its lifecycle is tied to the House.
    def __init__(self, name, area):
        self.name = name
        self.area = area
        print(f"    (A new room was built: {self.name})")

    def __str__(self):
        return f"Room: {self.name} ({self.area} sq ft)"
    
    def __del__(self):
        #This destructor will be called when the object is garbage collected.
        print(f"    (The {self.name} room is being destroyed...)")


class House:
    #The 'whole' class. It creates and owns its Room objects.
    def __init__(self, address):
        self.address = address
        self.rooms = []  # This list will OWN the Room objects
        print(f"\nBuilding a new House at: {self.address}")
        
    def add_room(self, name, area):
        """
        IMPORTANT: The House CREATES its own part.
        The Room object is instantiated INSIDE the House.
        """
        print(f"  > Constructing a {name} for the house.")
        new_room = Room(name, area) # **IMPORTAN**: Instantiating room inside of house
        self.rooms.append(new_room)

    def show_rooms(self):
        print(f"\n--- House at {self.address} ---")
        for room in self.rooms:
            print(f"  - {room}")
        print("-------------------------------")

    def __del__(self):
        """This destructor is called when the House is destroyed."""
        print(f"\n--- The House at {self.address} is being DEMOLISHED! ---")
        # When this object is destroyed, its 'self.rooms' list is also
        # destroyed. If nothing else refers to the Room objects in
        # that list, they will be garbage collected.
        
print("--- 1. Creating the House (the 'whole') ---")
my_house = House("123 Main St")

print("\n--- 2. The 'whole' (House) creates its 'parts' (Rooms) ---")
# We don't create 'kitchen' or 'bedroom' variables here.
# The rooms are *only* referenced from within the my_house object.
my_house.add_room("Kitchen", 200)
my_house.add_room("Living Room", 350)
my_house.add_room("Bedroom", 250)

my_house.show_rooms()

print(f"\n--- 3. Deleting the House object ---")
del my_house

print("\n--- 4. Checking what happens to the parts ---")
print("Because the 'whole' (House) was destroyed, its 'parts' (Rooms)")
print("were also destroyed (garbage collected), triggering their __del__ methods.")