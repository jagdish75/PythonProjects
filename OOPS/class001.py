# A sample class with init method

class Car(object):
    #Property Assignment

    wheels = 4
    # Function Initializatioa

    def __init__(self, make, model):
        self.make = make
        self.model = model


class Human(object):

    def __init__(self, name="no name", age=0,
                 nationality="no nationality",
                 gender="no gender"):

        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender

    def speak(self):
        print("Hello, My Name is : ", self.name)


# Driver Code, Main application Code
# MAIN APPLICATION CODE


mustang = Car('Ford', 'Mustang')

print("MUSTANG  Attributes:")
print("#########################")

print ("No of Wheels",mustang.wheels)
print ("No of Wheels",Car.wheels)
print ("\n\n")

bob = Human("Bob", 42, "British", "Male")
kate = Human("kate", 22, "American", "Female")


print("Bob's Attributes:")
print("*************************")
print(bob.name)
print(bob.age)
print(bob.nationality)
print(bob.gender)
print("")

print("Bob's Methods:")
print("*************************")
bob.speak()
print("*************************")
print("*************************")

