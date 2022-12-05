from universe import Universe

my_object = Universe()

# Print map
for row in range(my_object.rows):
    for column in range(my_object.columns):
        print(my_object.universe[row][column].system_type, end=" ")
    print()

my_object.initialize_ship()

print(my_object.current_ship.get_location())

while True:
    direction = input("Where would you like to go?  Enter N, S, W, E, NW, NE, SW, SE ").capitalize()

    my_object.move_ship(direction)

    print(my_object.current_ship.get_location())