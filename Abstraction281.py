

from abc import ABC, abstractmethod #imports Abstract base class
class animal(ABC):
    def animalCost(self, amount):
        print("You new family member costs: ",amount)
    @abstractmethod
    def payment(self, amount):
        pass

class CardPayment(animal):
    #implements payment function from its parent class animalCost
    def payment(self, amount):
        print('Your new pet amount of {} exceeded you $500 limit '.format(amount))
obj = CardPayment()
obj.payslip("$500")
obj.payment("$500")
