class Person:
    def __init__(self,name,course,age,marks):
        self.name= name
        self.course= course
        self.age= age
        self.marks= marks


p1 = Person("john","btech",36,9.5)
print(p1.name)
print(p1.course)
print(p1.age)
print(p1.marks)