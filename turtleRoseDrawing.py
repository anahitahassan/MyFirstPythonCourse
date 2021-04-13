import turtle
t=turtle.Pen()
turtle=turtle.Screen()
turtle.bgcolor("black")
t.speed(0.7)
sides = 4
colors = ["light pink", "light blue", "lavender"]
for x in range (50):
    t.pencolor(colors[x%3])
    t.forward(2*x)
    t.right(265/sides + 1)
    t.width(3)
print("It's a rose!")