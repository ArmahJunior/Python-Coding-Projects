from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("My Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

is_on = True
while is_on:
    for segment in segments:
        segment.























screen.exitonclick()