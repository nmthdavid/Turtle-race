from turtle import Turtle, Screen
import random

colors = ["red","blue","orange","pink","green","purple"]
turtles = []
coords = [0, 30, -30, -60, 60, 90]
screen = Screen()
screen.screensize(500,400)

for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    turtles.append(new_turtle)

for i in range (0,6):
    turtles[i].setposition(-340,coords[i])

bet = screen.textinput("Bet","Who will win the race?")

game_on = True

while game_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 340:
            winner = turtle
            print(winner.color()[1])
            if winner.color()[1] == bet.lower():
                exit = screen.textinput("Exit", "You won, type 'Exit' to exit the game.")
                if exit == "Exit":
                    screen.bye()
            else:
                exit = screen.textinput("Exit", "You lost, type 'Exit' to exit the game.")
                if exit == "Exit":
                    screen.bye()
            game_on = False


screen.title("Turtle Race")
screen.exitonclick()