import turtle
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

from based_projects.brazil_states_game.main import missing_states, guess_states

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50"
                                    , prompt="What´s the State Name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        # missing_states = []
        # for state in all_states:
        #     if state in guess_states:
        #         pass
        #     else:
        #         missing_states.append(state)
        df_final = pd.DataFrame(missing_states)
        df_final.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state.item())


