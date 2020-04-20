from turtle import *
from math import *
pencolor("#f00")
ht()
speed(8)
side_len = 200
side = 3
angle = 360 / side
r = side_len * sqrt(3) / 3
for i in range(side):
    fd(side_len)
    right(2 * angle)
pu()
goto(0, r)
pd()
for i in range(side):
    fd(side_len)
    left(2 * angle)
pu()
goto(side_len / 2, -r/2)
pd()

circle(r)
pu()
right(90)
fd(side_len / 20)
left(90)
pd()
circle(r + side_len / 20)

pu()
goto(side_len / 2, r / 2 - side_len / 100)
pd()
begin_fill()
fillcolor("#f00")
circle(side_len / 100)
end_fill()



