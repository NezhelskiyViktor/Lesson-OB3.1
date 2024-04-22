"""
Создайте базовый класс `Animal`, который будет содержать общие
атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`)
для всех животных.
"""


class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def make_sound(self):
        pass

    def eat(self):
        pass


"""
Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, 
которые наследуют от класса `Animal`. Добавьте специфические атрибуты и 
переопределите методы, если требуется (например, различный звук для `make_sound()`).
"""


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name}: Кло-кло-кло.")

    def eat(self):
        print(f"{self.name}: Клюет корм.")


class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name}: Грррр")

    def eat(self):
        print(f"{self.name}: Ест мясо.")


class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name}: Шшшшш")

    def eat(self):
        print(f"{self.name}: Ест траву.")


"""
Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, 
которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
"""


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


"""
Используйте композицию для создания класса `Zoo`, который будет содержать 
информацию о животных и сотрудниках. Должны быть методы для добавления 
животных и сотрудников в зоопарк.
"""


class Employee:
    def __init__(self, name, post):
        self.name = name
        self.post = post

    def work(self):
        print(f"Meня завут {self.name} {self.post}", end=".")
        if self.post == "бухгалтер":
            print(" Я работаю бухгалтером.")
        elif self.post == "рабочий":
            print(" Я кормлю животных.")
        elif self.post == "ветеринар":
            print(" Я лечу животных.")
        else:
            print(" Я не работаю в этом зоопарке.")


def workers_work(employees):
    for employee in employees:
        employee.work()


class Zoo:
    def __init__(self, name):
        self.name = name
        self._animals = []
        self._employees = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def add_employee(self, employee):
        if len(employee.post) > 0:
            self._employees.append(employee)

    def get_animals(self):
        return self._animals

    def get_employees(self):
        return self._employees

    def get_animals_date(self):
        for animal in self._animals:
            print(f"{animal.name}, возраст {animal.age} лет, пол {animal.sex}")

    def get_employees_date(self):
        for employee in self._employees:
            print(employee.name, employee.post)


"""
Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, 
которые могут иметь специфические методы (например, `feed_animal()` для 
`ZooKeeper` и `heal_animal()` для `Veterinarian`).
"""


class ZooKeeper(Employee):
    def feed_animal(self, animal):
        animal.eat()
        phrase = "покормлен" if animal.sex in "он" else "покормлена"
        print(f"{self.name}: {animal.name}, {phrase}")


class Veterinarian(Employee):
    def heal_animal(self, animal):
        animal.make_sound()
        phrase = "вылечен" if animal.sex in "он" else "вылечена"
        print(f"{self.name}: {animal.name}, {phrase}")


if __name__ == "__main__":
    # Запустите код ниже для проверки работы вашего кода
    zoo = Zoo('"Азия"')

# Животные для зоопарка
    zoo.add_animal(Bird("Павлин", 2, "он"))
    zoo.add_animal(Mammal("Лев", 4, "он"))
    zoo.add_animal(Reptile("Черепашка", 1, "она"))

    animals = zoo.get_animals()
    print(f"В зоопарке {zoo.name} {len(animals)} животных:")
    zoo.get_animals_date()

# Сотрудники для зоопарка
    print('\nСотрудники зоопарка:')
    zoo.add_employee(Employee("Вася", ""))
    zoo.add_employee(ZooKeeper("Андрей Б. П.", "рабочий"))
    zoo.add_employee(Veterinarian("Ольга В. С.", "ветеринар"))
    zoo.add_employee(ZooKeeper("Елена А.Ф.", "бухгалтер"))
    employees = zoo.get_employees()
    print(f"В зоопарке {zoo.name} {len(employees)} сотрудников.")
    zoo.get_employees_date()

    print("\nГолоса животных:")
    animal_sound(animals)
    workers_work(employees)

    print('\nПроверка работы сотрудников')
    for employee in employees:
        if isinstance(employee, ZooKeeper):
            for animal in animals:
                employee.feed_animal(animal)
        elif isinstance(employee, Veterinarian):
            for animal in animals:
                employee.heal_animal(animal)
