import os
from zoo import *


def create_zoo():  # Создаем зоопарк
    add_zoo = Zoo('"Африка"')

    print("Создан зоопарк", add_zoo.name)
    add_zoo.add_animal(Bird("Павлин", 2, "он"))
    add_zoo.add_animal(Mammal("Лев", 3, "он"))
    add_zoo.add_animal(Reptile("Черепашка", 4, "она"))
    print(f"\nВ зоопарке {add_zoo.name} {len(add_zoo._animals)} животных:")
    add_zoo.get_animals_date()

    add_zoo.add_employee(ZooKeeper("Андрей Б. П.", "рабочий"))
    add_zoo.add_employee(Veterinarian("Ольга В. С.", "ветеринар"))
    add_zoo.add_employee(ZooKeeper("Елена А.Ф.", "бухгалтер"))
    employees = add_zoo.get_employees()
    print(f"\nВ зоопарке {add_zoo.name} {len(employees)} сотрудника.")
    add_zoo.get_employees_date()
    return add_zoo


def save_zoo(zoo):
    # Записываем данные в файл
    with open('date.txt', 'w') as f:
        f.write(zoo.name)
        f.write('\n' + str(len(zoo._animals)))
        for animal in zoo._animals:
            f.write('\n' + type(animal).__name__)
            f.write('\n' + animal.name)
            f.write('\n' + str(animal.age))
            f.write('\n' + animal.sex)
        f.write('\n' + str(len(zoo._employees)))
        for employee in zoo._employees:
            f.write('\n' + type(employee).__name__)
            f.write('\n' + employee.name)
            f.write('\n' + employee.post)


def load_zoo():  # Читаем данные из файла
    with open('date.txt', 'r') as f:
        new_zoo = Zoo(f.readline().strip())
        i = int(f.readline())
        for _ in range(i):
            class_name = f.readline().strip()
            if class_name == 'Bird':
                new_zoo.add_animal(Bird(
                    f.readline().strip(),
                    int(f.readline()),
                    f.readline().strip()))
            elif class_name == 'Mammal':
                new_zoo.add_animal(Mammal(
                    f.readline().strip(),
                    int(f.readline()),
                    f.readline().strip()))
            elif class_name == 'Reptile':
                new_zoo.add_animal(Reptile(
                    f.readline().strip(),
                    int(f.readline()),
                    f.readline().strip()))

        i = int(f.readline())
        for _ in range(i):
            class_name = f.readline().strip()
            if class_name == 'ZooKeeper':
                new_zoo.add_employee(ZooKeeper(
                    f.readline().strip(),
                    f.readline().strip()))
            elif class_name == 'Veterinarian':
                new_zoo.add_employee(Veterinarian(
                    f.readline().strip(),
                    f.readline().strip()))
    os.remove('date.txt')
    return new_zoo


# Запускаем программу
if os.path.isfile('date.txt'):
    my_zoo = load_zoo()
    print(f"\nВ зоопарке {my_zoo.name} {len(my_zoo._animals)} животных:")
    my_zoo.get_animals_date()
    print(f"\nВ зоопарке {my_zoo.name} {len(my_zoo._employees)} сотрудников:")
    my_zoo.get_employees_date()
else:
    my_zoo = create_zoo()
    print(f"\nВ зоопарке {my_zoo.name} {len(my_zoo._employees)} сотрудников:")
    my_zoo.get_employees_date()
    print(f"\nВ зоопарке {my_zoo.name} {len(my_zoo._animals)} животных:")
    my_zoo.get_animals_date()

employees = my_zoo.get_employees()
animals = my_zoo.get_animals()
print("\nГолоса животных:")
animal_sound(animals)

print("\nСотрудники:")
workers_work(employees)

print("\nДобавляем нового сотрудника")
my_zoo.add_employee(ZooKeeper(input('Введите имя нового рабочего:'), "рабочий"))
my_zoo.add_employee(Veterinarian(input('Введите имя нового ветеринара:'), "ветеринар"))

print("\nДобавляем животное")
my_zoo.add_animal(Bird(input('Введите имя птицы:'), 1, 'он'))

save_zoo(my_zoo)
