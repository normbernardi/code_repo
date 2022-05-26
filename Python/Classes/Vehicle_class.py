class Vehicle:
    def __init__(self, make, model, cost):
        self.make = make
        self.model = model
        self.cost = cost

    def __repr__(self):
        return f'{self.make}{self.model}{self.cost}'

    def discount(self, drate: float):
        discount = self.cost * drate
        return self.cost - discount

    def tax(self, trate: float):
        tax = self.cost * trate
        return self.cost + tax

    def depreciation(self, fmv):
        return self.cost - fmv

from datetime import date
class Truck(Vehicle):
    def __init__(self, make, model, cost, year):
        super().__init__(make, model, cost)
        self.year = year

    def __repr__(self):
        return f'{self.make} {self.model} {self.cost} {self.year}'

    def age(self):
        current_year = date.today().year
        return current_year - self.year

    def discount(self, drate: float):
        return super().discount(drate)

    def tax(self, trate: float):
        return super().tax(trate)

    def depreciation(self, fmv):
        return super(self.cost, fmv)




t = Truck("ford", "raptor", 50000, 2015)
print(t)
print(t.age())
print(t.tax(0.07))
print(t.discount(0.1))