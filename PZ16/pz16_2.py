# Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол". От этого
# класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них свойства,
# связанные с социальным положением (например, "семейное положение",
# "количество детей" и т.д.).
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Man(Person):
    def __init__(self, name, age, gender, marital_status, children_count):
        super().__init__(name, age, gender)
        self.marital_status = marital_status
        self.children_count = children_count

class Woman(Person):
    def __init__(self, name, age, gender, marital_status, children_count):
        super().__init__(name, age, gender)
        self.marital_status = marital_status
        self.children_count = children_count

# Example usage
man = Man("John", 30, "Male", "Married", 2)
woman = Woman("Alice", 28, "Female", "Single", 0)

print(f"Name: {man.name}, Age: {man.age}, Gender: {man.gender}, Marital Status: {man.marital_status}, Children Count: {man.children_count}")
print(f"Name: {woman.name}, Age: {woman.age}, Gender: {woman.gender}, Marital Status: {woman.marital_status}, Children Count: {woman.children_count}")