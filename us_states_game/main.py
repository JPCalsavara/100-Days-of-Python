import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

is_game_on = True

while is_game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What´s the State Name?")
    answer_state.capitalize()
    data = pd.read_csv("50_states.csv")
    data[data.state == answer_state]

screen.exitonclick()