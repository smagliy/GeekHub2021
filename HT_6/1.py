list_for_cars = ('Red', 'Red', 'Red', 'Yellow', 'Yellow', 'Green', 'Green', 'Green')
list_for_people = ('Green', 'Green', 'Green', 'Green', 'Red', 'Red', 'Red', 'Red')

while True:
    for i in range(len(list_for_cars)):
        print(list_for_people[i] + " " + list_for_cars[i])
