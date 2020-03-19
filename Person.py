class Person:
    def __init__(self, name, age, health):
        self.age = age
        self.name = name
        self.health = health

    def __add__(self, other_obj):
        add_obj = Person("Shelly", self.age + other_obj.age)
        return add_obj

    def __sub__(self, other_obj):
        return self.age - other_obj.age

    def __mul__(self, other_obj):
        return self.age * other_obj.age

    def __radd__(self, age):
        print(age)
        return self.age + age


p1 = Person("Goshko", 15, "Fine")
p2 = Person("Ivan", 14, "Infected")
print(p2 * p1)