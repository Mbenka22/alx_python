class Person:
    def __init__(self, name):#init takes a parameter(name) and the self and also create a ner field (name)
        self.name = name
         #There is no problem because the dotted notation self.name means that there is something called "name" that is part of the object called "self" and the other name is a local variable. Since we explicitly indicate which name we are referring to, there is no confusion

    def say_hi(self):
        print('Hello, my name is',self.name)

p = Person('Swaroop')#When creating new instance p, of the class Person, we do so by using the class name, followed by the arguments in the parentheses: p = Person('Swaroop').
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()
