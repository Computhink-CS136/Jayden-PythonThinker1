import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.seth(0)
t.speed(0)
t.color("green")
t.pendown()
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# for i in range(3):
#     t.left(120)
#     t.forward(100)
# for i in range(360):
#     t.forward(1)
#     t.left(1)
for i in range(200):
    for p in range(360):
        t.forward(2)
        t.left(1)
    t.forward(5)
# colours = ["#FF0000", "#ff9900", "#ddff00", "#00ff40", "#2f00ff"]
# length = 3
# for i in range(10000):
#     for colour in colours:
#         t.color(colour)
#         t.forward(length)
#         t.right(91)
#         length += 3

turtle.done()