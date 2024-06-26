import turtle
import pandas as pd

# Set up the screen
screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the data
df = pd.read_csv("50_states.csv")

# Initialize the counter for correct guesses
correct_guesses = 0

# Main game loop
while True:
    # Get user input for the state name
    answer_state = screen.textinput(
        title=f"Guess the State ({correct_guesses}/50 correct)",
        prompt="What's the next state?"
    ).title()

    # Break the loop if the user clicks cancel
    if answer_state is None:
        break

    # Check if the guessed state is in the list of states
    if answer_state in df["state"].values:
        correct_guesses += 1

        # Get the row with the guessed state
        row = df[df["state"] == answer_state].iloc[0]
        state = row["state"]
        x = row["x"]
        y = row["y"]

        # Create a turtle to write the state name on the map
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(x, y)
        pen.write(state, align="center", font=("Arial", 12, "normal"))

# Exit the game on screen click
screen.exitonclick()
