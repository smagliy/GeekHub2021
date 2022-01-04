# Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів,
# які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
#    - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
class Person(object):
    def __init__(self, *args):
        self.dict_elements = {
                'name': [el for el in args if type(el) == str],
                'age': [el for el in args if type(el) == int]
            }

    def print_name(self):
        print(self.dict_elements['name'])

    def show_age(self):
        print(self.dict_elements['age'])

    def show_all_information(self):
        print(self.dict_elements)


person1 = Person('anna', 20)
person1.show_all_information()
person2 = Person('vasya', 30)
person2.print_name()
person1.professional = 'developer'
person2.professional = 'designer'
print(person1.professional)
print(person2.professional)