import turtle
wn=turtle.Screen()
wn.bgcolor("light green")
wn.turtle=("Turtle")
skk=turtle.Turtle()
skk.color("blue")
def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size-=5
sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)
def sqrfunc1(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size+=5
sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)
turtle.done()