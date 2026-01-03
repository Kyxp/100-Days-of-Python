# Day 19 - Turtle Race
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour: ")
while user_bet.lower() not in colours:
    user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour: ")
turtles = []


# create the turtles
for i in range(len(colours)):
    a = Turtle(shape="turtle")
    a.color(colours[i])
    a.penup()
    a.goto(x=-230,y=(-150+i*60))
    turtles.append(a)

# move the turtles
winner = False
bet = False

while winner == False:
    for turtle in turtles:
        # generate random
        num = random.randint(1,6)
        # move
        turtle.forward(num)
        # check for winner
        if turtle.xcor() >= 170:
            # reset xcor incase too far
            turtle.setx(170)
            # display winner
            turtle_winner = str(turtle.color()[0]).capitalize()
            print(turtle_winner, "wins!")
            winner = True

            # user bet
            if turtle_winner.lower() == user_bet.lower():
                bet = True

                

if bet == True:
    print("You won the bet!")
else:
    print("Sorry, you lost the bet.")

screen.exitonclick()