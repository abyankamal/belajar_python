# from turtle import Turtle, Screen

# timmy = Turtle()

# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# screen = Screen()
# print(screen.canvheight)
# screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])

table.align = "l"

print(table)

