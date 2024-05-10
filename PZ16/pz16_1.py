# Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная память".
# Напишите метод, который выводит информацию о компьютере в формате "Марка: марка, Процессор: процессор,
# Оперативная память: память".

class Computer:
    def __init__(self, marca, processor, ram):
        self.marca = marca
        self.processor = processor
        self.ram = ram

    def get_info(self):
        return f"Марка: {self.marca}, Процессор: {self.processor}, Оперативная память: {self.ram}"


computer = Computer("Dell", "Intel Core i7", "16GB")
print(computer.get_info())