# Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white
# і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для
# завдання початкових розмірів об'єктів при їх створенні.
class Figure(object):
    color = 'white'

    class Oval(object):
        def __init__(self, r1, r2):
            self.r1 = r1
            self.r2 = r2

    class Square(object):
        def __init__(self, a):
            self.a = a

    def change_color(self, change):
        self.color = change
        return self.color


figure_1 = Figure().change_color('blue')
print(figure_1)
figure_2 = Figure().Square(10)
print(figure_2)