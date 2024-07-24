#INHERITANCE
class father:
    def father_speaker():
        return"father class"
class mother:
    def mother_speaker():
        return"mother class"
class kid(father,mother):
    def kid_speaker():
        return"i am a kid i have inheritance of mother and father"
obj1=kid
print(obj1.father_speaker())
print(obj1.mother_speaker())
print(obj1.kid_speaker())

            