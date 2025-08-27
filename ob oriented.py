#activity 1 of object oriented progrramming
class Student():
    grade = 10 
    print ("Hi I am a student of grade", grade)
    
ob = Student()

#activity 2
class Vehicle():
    def __init__(self, max_spped, mileage):
        
        self.max_speed = max_spped
        self.mileage = mileage
    
mode1X = Vehicle(240, 18) 

print("model max speed:", mode1X.max_speed)
print("model mileage:", mode1X.mileage)

#activity 3
class Parrot:
    
    species = "bird" 
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

#class is a blue print
#object is an intance of a class
#varieables are nothing but properties and attributtes of a class
#methods are like members or a function of a class no function keyword is used
#class varieables are directly called with the object
#object variables are past with the object in the process of object creation
#self is the one who points to a perticular object
