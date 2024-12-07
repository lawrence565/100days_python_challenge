import turtle, pandas

class StateName(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def show_state(self, state, coor):
        self.goto(coor)
        self.write(state)



screen = turtle.Screen()
screen.title("USA Game")

# Set the background of the screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

state_data = pandas.read_csv("50_states.csv")
game_is_on = True
guessed_state = []
state_list = state_data["state"].to_list()

while game_is_on:
    answer_state = screen.textinput(title="Guess a state", prompt="What's another state's name?")
    if answer_state in state_list:
        state_name = StateName()
        guessed_state.append(answer_state)
        screen.title(f"{len(guessed_state)}/50 state correct")

        # Use .item() to get the value only and avoid bug.
        x = state_data[state_data.state == answer_state].x.item()
        y = state_data[state_data.state == answer_state].y.item()
        state_name.show_state(answer_state, (x, y))
    game_is_on = False


turtle.onscreenclick(get_mouse_click_coor)
screen.mainloop()
# screen.exitonclick()