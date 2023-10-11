import turtle
import random
leo = turtle.Turtle()
colors = ('violet' , 'blue' , 'green', 'red')

for i in range(12):
    for u in range(2):
        leo.color(random.choice(colors))
        leo.forward(60)
        leo.right(30)
        leo.forward(60)
        leo.right(150)
    leo.right(30)