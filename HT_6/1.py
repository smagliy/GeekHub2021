import time
list_for_cars = ('Red', 'Red', 'Red', 'Yellow', 'Yellow', 'Green', 'Green', 'Green', 'Yellow', 'Yellow')
list_for_people = ('Green', 'Green', 'Green', 'Green', 'Green', 'Red', 'Red', 'Red', 'Red', 'Red')

while True:
    for i in range(len(list_for_cars)):
        time.sleep(1)
        print(list_for_cars[i] + "        " + list_for_people[i])