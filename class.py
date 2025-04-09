class Vehicle:
    """Base class for all vehicles."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Display vehicle information."""
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    """Class representing a car, inheriting from Vehicle."""
    
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        """Display car information, including the number of doors."""
        return f"{super().display_info()} with {self.doors} doors"

    def honk(self):
        """Car-specific method to honk."""
        return "Beep beep!"

# Example usage
my_car = Car("Toyota", "Corolla", 2020, 4)
print(my_car.display_info())  # Output: 2020 Toyota Corolla with 4 doors
print(my_car.honk())          # Output: Beep beep!


#polymorphism
class Horse:
    """Base class for all horses."""
    
    def move(self):
        """Base move method to be overridden."""
        raise NotImplementedError("Subclasses must implement this method.")

class Thoroughbred(Horse):
    """Class representing a Thoroughbred horse."""
    
    def move(self):
        """Override move method for Thoroughbred."""
        return "Galloping swiftly "

class Clydesdale(Horse):
    """Class representing a Clydesdale horse."""
    
    def move(self):
        """Override move method for Clydesdale."""
        return "Trotting steadily "

class Pony(Horse):
    """Class representing a Pony."""
    
    def move(self):
        """Override move method for Pony."""
        return "Cantering playfully "

# Example usage
def demonstrate_movement(horse):
    print(horse.move())

# Create instances of each horse type
my_thoroughbred = Thoroughbred()
my_clydesdale = Clydesdale()
my_pony = Pony()

# Demonstrate polymorphism
demonstrate_movement(my_thoroughbred)  # Output: Galloping swiftly 
demonstrate_movement(my_clydesdale)     # Output: Trotting steadily 
demonstrate_movement(my_pony)           # Output: Cantering playfully 