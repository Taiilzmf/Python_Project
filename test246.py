class Marzett:
    #parent class created for Marzett family
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    #creates a method
    def hello(self):
        print("Hello", self.name, " your age is", self.age)

class Parents(Marzett):
    #child created through inheritance
    job = ' '
    car = ' '
    #adds job to hello function in self
    def hello(self):
        print("Hello", self.name, " your age is", self.age, " and your job is " job)
        
class Children(Marzett):
    #second child created through inheritance from Marzett
    fav_subject = ' '
    hobby = ' '

    #adds hobby instead of job to hello function
    def hello(self):
        print("Hello", self.name, " your age is", self.age, " and your hobby is " hobby)
        

