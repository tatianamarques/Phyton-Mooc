import turtle

turtle.up()
turtle.goto(-150, -150)
turtle.down()
turtle.color("blue")
turtle.begin_fill()
turtle.goto(150, -150)
turtle.goto(150, 150)
turtle.goto(-150, 150)
turtle.goto(-150, -150)
turtle.end_fill()
#turtle.mainloop #O camando da inha 13 e 14 tem o mesmo resultado de fechamento. 
turtle.done() 