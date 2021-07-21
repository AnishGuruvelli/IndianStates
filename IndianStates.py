# states = [Andhra Pradesh, Assam, Arunachal Pradesh, Bihar, Goa, Gujarat, Jammu and Kashmir, Jharkhand, West Bengal,
# Karnataka, Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Orissa, Punjab, Rajasthan,
# Sikkim, Tamil Nadu, Tripura, Uttaranchal, Uttar Pradesh, Haryana, Himachal Pradesh, and Chhattisgarh, Andaman and
# Nicobar, Pondicherry, Dadra and Nagar Haveli, Daman and Diu, Delhi, Chandigarh, Lakshadweep]

import pandas
import turtle

screen = turtle.Screen()
screen.title("Indian States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click)

# this is to get the x and y coordinates of the indian map

data = pandas.read_csv("29states.csv")
all_states = data.state.to_list()
print(all_states)
guessed_states = []

answer_state = screen.textinput(title="Guess the state", prompt="What's the next state's name?")
print(answer_state)


while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 States Correct",
                                    prompt="Next state's name? Type exit to quit the game.").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # if answer state is one of the 29 states in the csv file then
    #   if they got it right
    #       create a turtle to write in the respective x and y coordinate

    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        # data[data.state == answer_state] this is to get the row
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)


screen.exitonclick()



