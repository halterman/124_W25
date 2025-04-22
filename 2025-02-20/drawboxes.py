from turtletools import box
from turtle import penup, pendown, setposition, \
     done, title, fillcolor, begin_fill, end_fill

title('Boxes')

penup()
setposition(100, 200)
pendown()
box(100)
penup()

fillcolor('red')
setposition(-100, -50)
pendown()
begin_fill()
box(150)
end_fill()
penup()

fillcolor('blue')
setposition(-100, -50)
pendown()
begin_fill()
box(150)
end_fill()
penup()

setposition(300, 25)
pendown()
begin_fill()
box(50)
end_fill()
penup()

done()