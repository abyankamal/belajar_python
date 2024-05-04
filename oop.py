# from turtle import Turtle, Screen

# timmy = Turtle()

# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# screen = Screen()
# print(screen.canvheight)
# screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon", ["Pikachu", "Charmander", "Squirtle"])
# table.add_column("Type", ["Electric", "Fire", "Water"])

# table.align = "l"

# print(table)

# create our class
class User :
    # create constructor
    def __init__(self, id, username) :
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    # create method
    def follow(self, user) :
        user.followers += 1
        self.following += 1

user_1 = User("001", "Angela")
user_2 = User("002", "Budi")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

