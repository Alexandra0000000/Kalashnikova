# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python
# в бинарном формате.
import pickle

class Computer:
    def __init__(self, marca, processor, ram):
        self.marca = marca
        self.processor = processor
        self.ram = ram

    def get_info(self):
        return f"Марка: {self.marca}, Процессор: {self.processor}, Оперативная память: {self.ram}"

def save_def(computers):
    with open('computers_data.pkl', 'wb') as file:
        pickle.dump(computers, file)

def load_def():
    with open('computers_data.pkl', 'rb') as file:
        return pickle.load(file)

computer1 = Computer("HP", "Intel Core i5", "8GB")
computer2 = Computer("Dell", "AMD Ryzen 7", "16GB")
computer3 = Computer("Apple", "Apple M1", "32GB")

computers_list = [computer1, computer2, computer3]
save_def(computers_list)

loaded_computers = load_def()

for computer in loaded_computers:
    print(computer.get_info())