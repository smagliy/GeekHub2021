# Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
class Count_attribute:
    counter = 0

    def __init__(self):
        Count_attribute.counter += 1
        self.id = Count_attribute.counter


p = Count_attribute()
a = Count_attribute()
print(a.counter)


