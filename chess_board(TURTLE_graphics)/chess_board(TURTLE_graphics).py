import turtle as t
t.speed(0)
t.color('black')
for i in range(8):
    for j in range(8):
        if((i+j)%2 == 0):
            t.begin_fill()
        for k in range(4):
            t.fd(40)
            t.lt(90)
        t.end_fill()
        t.fd(40)
    t.pu()
    t.goto(0,-(i+1)*40) 
    t.pd()
t.done()
t.exitonclick()
