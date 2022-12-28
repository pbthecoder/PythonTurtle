import turtle as t
s = t.Screen()
t.bgcolor("white")
s.setup(600,600)
s.tracer(0)
t.pensize(5)

def draw_rays():
  for i in range(12):
    t.pencolor('orange')
    t.pu()
    t.goto(0,0)
    t.pd()
    t.pu()
    t.fd(70)
    t.pd()
    t.fd(50)
    t.pu()
    t.bk(120)
    t.lt(30)
    t.pd()

draw_rays()
for i in range(1000):
  s.tracer(0)
  t.pencolor('yellow')
  t.fillcolor('yellow')
  t.begin_fill()
  t.pu()
  t.rt(90)
  t.fd(60)
  t.lt(90)
  t.pd()
  t.circle(60)
  t.end_fill()
  draw_rays()
  t.rt(1)
  s.update()
  t.clear()
  t.hideturtle()