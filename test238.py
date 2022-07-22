class Marzett:
    #parent class created for Marzett family
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

class Parents(Marzett):
    #child created through inheritance
    jobs = ' '
    car = ' '
class Children(Marzett):
    #second child created through inheritance from Marzett
    fav_subject = ' '
    hobby = ' '
    
