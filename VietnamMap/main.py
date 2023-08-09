import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Vietnam game")
img = "vn.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("vn.csv")
all_states = data.city.to_list()
input_state = []
while len(input_state) < 30:
    answer = screen.textinput(title=f"{len(input_state)} correct", prompt="what's state name ?").title()
    print(answer)
    if answer == "x":
        missing_states = []
        for state in all_states:
            if state not in input_state:
                missing_states.append(state)
        print(missing_states)
        break
# print(data.admin_name)
#
#
# def get_mouse_click_cor(x, y):
#     print(x, y)
    if answer in all_states:
        input_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.city == answer]
        t.goto(int(state_data.lat), int(state_data.lng))
        t.write(answer)
# turtle.onscreenclick(get_mouse_click_cor)
screen.mainloop()
