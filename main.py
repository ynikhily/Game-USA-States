import turtle
import pandas as pd

ALIGN = 'center'
FONT = ('Arial', 12, 'normal')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv('50_states.csv')

state_list = data['state'].to_list()


tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

game_is_on = True
guessed_state = 0
while game_is_on:
    state_name = screen.textinput(title=f"{guessed_state}/50 Guess the State", prompt="Guess another state name.")
    if state_name:
        state_name = state_name.title()
        if state_name in state_list:
            tim.goto(int(data[data['state'] == state_name].x), int(data[data['state'] == state_name].y))
            tim.write(state_name, align=ALIGN, font=FONT)
            guessed_state += 1
            state_list.remove(state_name)

        if state_name == 'Q':
            game_is_on = False
        if guessed_state == 50:
            game_is_on = False
    else:
        print("No name provided!!")

screen.exitonclick()

missed_states = {'states': [state for state in state_list]}


data_for_csv = pd.DataFrame(missed_states)
data_for_csv.to_csv('States_to_Learn.csv')