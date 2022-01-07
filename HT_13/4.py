# Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури при
# створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.
class Figure(object):
    def __init__(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, r1, r2, color):
        super(Oval, self).__init__(color)
        self.r1 = r1
        self.r2 = r2


class Square(Figure):
    def __init__(self, a, color):
        super(Square, self).__init__(color)
        self.a = a


figure_1 = Figure('white')
figure_2 = Oval(10, 2, 'blue')
print(figure_2.color)
