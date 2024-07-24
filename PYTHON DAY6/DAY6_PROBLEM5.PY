class animal:
    def speak():
        return"animal is speaking"
#single inheritance
class dog(animal):
    def speak():
        return"dog is speaking"
#multiple inheritance
class puppy(dog):
    def speak():
        return"puppy is speaking"
obj3=puppy
print(obj3.speak())    