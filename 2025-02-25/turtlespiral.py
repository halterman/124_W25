# Turtle spiral

import turtle as t

# Version A
#t.tracer(0)
#t.hideturtle()
# t.left(120)
# t.speed(8)
# t.penup()
# t.setposition(-200, -200)
# t.pendown()
# increment = 0
# for i in range(1000):
#     increment += 0.05
#     t.forward(8)
#     t.right(increment)
# t.update()
# t.done()

# Version B
# fw = 4
# turn = 60
# for i in range(500):
#     t.forward(fw)
#     t.left(turn)
#     turn /= 1.03
#     fw += 0.5
# t.update()
# t.done()

# Version C
for i in range(100):
    t.forward(i * i/100)
    t.left(i)
