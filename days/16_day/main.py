# from turtle import Turtle,Screen
import prettytable

# big = Turtle()
#
# big.shape("turtle")
# big.color("blue2","chartreuse2")


table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander"])
table.add_column("Type",["Eletric","Fire"])
table.align = "l"
print(table)