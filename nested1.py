from turtle import*

speed('fastest')
pencolor('black')

#hexagon
for i in range(6):
    pensize(5)
    fd(100)
    for i in range(6):
        pensize(3)
        fd(50)
        fillcolor('red')
        begin_fill()
        for i in range(6):
            pensize(1)
            fd(25)
            dot(10)
            lt(60)
        end_fill()    
        rt(60)
    lt(60)

hideturtle()
mainloop()        