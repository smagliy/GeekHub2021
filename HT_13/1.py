# Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з 2-ма числами,
# а саме додавання, віднімання, множення, ділення.
#    - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
#    - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
#    - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )
class Calc(object):
    last_result = None

    def sum(self, number_a, number_b):
        self.last_result = number_b + number_a
        return self.last_result

    def difference(self, number_a, number_b):
        self.last_result = number_b - number_a
        return self.last_result

    def multiplication(self, number_a, number_b):
        self.last_result = number_b * number_a
        return self.last_result

    def divide(self, number_a, number_b):
        self.last_result = number_b / number_a
        return self.last_result


a_last_result = Calc().last_result
sum_numbers = Calc().sum(10, 2)
diff_numbers = Calc().difference(2, 10)
print(sum_numbers, diff_numbers, a_last_result)
