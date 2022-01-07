# Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white
# і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для
# завдання початкових розмірів об'єктів при їх створенні.
class Figure(object):
    color = 'white'

    def change_color(self, change):
        self.color = change
        return self.color


class Oval(Figure):
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2


class Square(Figure):
    def __init__(self, a):
        self.a = a


figure1 = Square(10).change_color('blue')
print(figure1)