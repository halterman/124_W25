import turtle as t

def draw_square(x: float, y: float, side: float, color: str) -> None:
    """
    Draws a square centered at (x, y) with a side of length 'side' 
    and color of 'color'.
    """
    t.penup()
    half_side = side /2
    t.setposition(x - half_side, y - half_side)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(side)
        t.left(90)
    t.end_fill()
    t.update()


def mouse_click(x: float, y: float) -> None:
    #print(f'x = {x} and y = {y}')
    draw_square(x, y, 50, 'red')


t.hideturtle()
t.tracer(0)

draw_square(0, 51, 100, 'green')

t.onscreenclick(mouse_click)

t.mainloop()