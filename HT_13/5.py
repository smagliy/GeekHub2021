# Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію)
class Library(object):
    dict_books = {
        'poems': {1: 'WE SANG YOU HOME BY RICHARD VAN CAMP',
                  2: 'FULL, FULL, FULL OF LOVE BY TRISH COOKE',
                  3: 'LITTLE POEMS FOR TINY EARS BY LIN OLIVER'},
        'stories': {1: 'The Tiger Who Came to Tea by Judith Kerr',
                    2: 'Pippi Longstocking by Astrid Lindgren',
                    3: 'Dog Man by Dav Pilkey'},
        'novels': {1: 'The Absolutely True Diary of a Part-Time Indian by Sherman Alexie',
                   2: 'The Birchbark House by Louise Erdrich'},
        'tales': {1: 'Goldilocks and the Three Bears by Jan Brett'},
        'mysteries': {1: 'The Deductive Detective. by Brian Rock',
                      2: 'Enigma: A Magical Mystery by Graeme Base'},
        'comics': {1: ' OWLY', 2: 'TINY TITANS', 3: 'SCOOBY-DOO TEAM-UP'},
        'educational_books': {1: 'geometry book', 2: 'money book'},
    }

    def show_list_books(self):
        print(self.dict_books)

    def take_the_book(self, genres):
        print(self.dict_books[genres])
        number = int(input("Write book's index: "))
        print(self.dict_books[genres][number])
        self.dict_books[genres].pop(number)

    def show_one_categ(self, genres):
        print(self.dict_books[genres])

    def return_book(self, genres, index, book):
        self.dict_books[genres][int(index)] = book


children_1 = Library()
children_1.show_list_books()
children_1.take_the_book('tales')
children_1.show_one_categ('tales')
children_1.return_book('tales', 1, 'Goldilocks and the Three Bears by Jan Brett')
children_1.show_one_categ('tales')