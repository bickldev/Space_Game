from universe import Universe

my_object = Universe()

for row in range(my_object.rows):
    for column in range(my_object.columns):
        print(my_object.universe[row][column].system_type, end=" ")
    print()

my_object.initialize_ship()