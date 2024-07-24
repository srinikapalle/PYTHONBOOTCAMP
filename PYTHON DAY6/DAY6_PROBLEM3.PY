#inheritance
class animal:
    def speak():
        return"animal is speaking"
#single inheritance
class dog(animal):
    def bark():
        return"bow......"
#multiple inheritance
class puppy(dog):
    def puppy_speak():
        return"aww..."
obj1=animal
obj2=dog
obj3=puppy
print(obj1.speak())    
print(obj2.bark()) 
print(obj3.puppy_speak()) 
