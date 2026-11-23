class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} yrs"
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
print(blu.description())
