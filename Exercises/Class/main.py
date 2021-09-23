class Dog:
    def __init__(self, name, gender, size):
        self.name = name
        self.gender = gender
        self.size = size

    def makeSound(self):
        print("wau-wau")

    def toString(self):
        print(f"name: {self.name} \tgender: {self.gender} \tsize {self.size}")



class Pitbull(Dog):
    def __init__(self, color, isAggressive, name, gender, size):
        super().__init__(name, gender, size)
        self.color = color
        self.isAggressive = isAggressive

    def attack(self):
        print(f"{self.name} attacks")

    def toString(self):
        print("super constructor")
        super().toString()
        print(f"name: {self.name} \tgender: {self.gender} \tsize {self.size} color: {self.color} \tisAggressive: {self.isAggressive}")

class GermanShepherd(Dog):
    def __init__(self, fur, name, gender, size):
        super().__init__(name, gender, size)
        self.fur = fur




dog1 = Dog("Felix", "male", "large")
dog1.makeSound()
dog1.toString()
print("\n")


pit = Pitbull("grey", True, "Bob", "male", "big")
pit.toString()

print("\n")
pit.attack()


