class Person:
    # Initialize the Person with name, age, and gender attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Method to introduce the person
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Create an instance of the Person class
person_instance = Person("Moyahabo", 30, "Female")

# Call the introduce method to display the person's information
person_instance.introduce()
