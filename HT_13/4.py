# Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури при
# створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.
class Figure(object):
    def __init__(self, color):
        self.color = color

    class Oval(object):
        def __init__(self, r1, r2, color):
            self.r1 = r1
            self.r2 = r2
            self.color = Figure(color)

    class Square(object):
        def __init__(self, a, color):
            self.a = a
            self.color = Figure(color)


figure_1 = Figure('white')
figure_1.Oval(1, 2, Figure('blue'))
