# Lesson-OB03.1 Композиция и полиморфизм
## Постановка задачи
1. Создайте базовый класс `Animal`, который будет содержать 
общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) 
для всех животных.
2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, 
и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические 
атрибуты и переопределите методы, если требуется (например, различный звук 
для `make_sound()`).
3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, 
которая принимает список животных и вызывает метод `make_sound()` для каждого 
животного.
4. Используйте композицию для создания класса `Zoo`, который будет содержать 
информацию о животных и сотрудниках. Должны быть методы для добавления животных 
и сотрудников в зоопарк.
5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, 
которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

Дополнительно:

Попробуйте добавить дополнительные функции в вашу программу, такие как 
сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у 
вашего зоопарка было "постоянное состояние" между запусками программы.

## Реализация задачи

Основное решение задачи находится в модуле [zoo](zoo.py)</br>
Реализована и дополнительная часть задачи. Она находится в модуле [main](main.py)

## Пример вывода в консоль отладочной информации
### Модуля ZOO
В зоопарке "Азия" 3 животных:</br>
Павлин, возраст 2 лет, пол он</br>
Лев, возраст 4 лет, пол он</br>
Черепашка, возраст 1 лет, пол она</br>
</br>
Сотрудники зоопарка:</br>
В зоопарке "Азия" 3 сотрудников.</br>
Андрей Б. П. рабочий</br>
Ольга В. С. ветеринар</br>
Елена А.Ф. бухгалтер</br>
</br>
Голоса животных:</br>
Павлин: Кло-кло-кло.</br>
Лев: Грррр</br>
Черепашка: Шшшшш</br>
Meня завут Андрей Б. П. рабочий. Я кормлю животных.</br>
Meня завут Ольга В. С. ветеринар. Я лечу животных.</br>
Meня завут Елена А.Ф. бухгалтер. Я работаю бухгалтером.</br>
</br>
Проверка работы сотрудников</br>
Павлин: Клюет корм.</br>
Андрей Б. П.: Павлин, покормлен</br>
Лев: Ест мясо.</br>
Андрей Б. П.: Лев, покормлен</br>
Черепашка: Ест траву.</br>
Андрей Б. П.: Черепашка, покормлена</br>
Павлин: Кло-кло-кло.</br>
Ольга В. С.: Павлин, вылечен</br>
Лев: Грррр</br>
Ольга В. С.: Лев, вылечен</br>
Черепашка: Шшшшш</br>
Ольга В. С.: Черепашка, вылечена</br>
Павлин: Клюет корм.</br>
Елена А.Ф.: Павлин, покормлен</br>
Лев: Ест мясо.</br>
Елена А.Ф.: Лев, покормлен</br>
Черепашка: Ест траву.</br>
Елена А.Ф.: Черепашка, покормлена</br>
</br>
### Модуль MAIN
Создан зоопарк "Африка"</br>
</br>
В зоопарке "Африка" 3 животных:</br>
Павлин, возраст 2 лет, пол он</br>
Лев, возраст 3 лет, пол он</br>
Черепашка, возраст 4 лет, пол она</br>
</br>
В зоопарке "Африка" 3 сотрудника.</br>
Андрей Б. П. рабочий</br>
Ольга В. С. ветеринар</br>
Елена А.Ф. бухгалтер</br>
</br>
В зоопарке "Африка" 3 сотрудников:</br>
Андрей Б. П. рабочий</br>
Ольга В. С. ветеринар</br>
Елена А.Ф. бухгалтер</br>
</br>
В зоопарке "Африка" 3 животных:</br>
Павлин, возраст 2 лет, пол он</br>
Лев, возраст 3 лет, пол он</br>
Черепашка, возраст 4 лет, пол она</br>
</br>
Голоса животных:</br>
Павлин: Кло-кло-кло.</br>
Лев: Грррр</br>
Черепашка: Шшшшш</br>
</br>
Сотрудники:</br>
Meня завут Андрей Б. П. рабочий. Я кормлю животных.</br>
Meня завут Ольга В. С. ветеринар. Я лечу животных.</br>
Meня завут Елена А.Ф. бухгалтер. Я работаю бухгалтером.</br>
</br>
Добавляем нового сотрудника</br>
Введите имя нового рабочего:</br>