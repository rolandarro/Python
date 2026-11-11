#Roland Arro IT-26 11.11.2026
#Ülesanne 02
import turtle


##aken
aken = turtle.Screen()
aken.setup(width=500, height=400)
aken.title("Roland Arro - olümpiarõngad")
#liigutan õigesse kohta
turtle.speed(0)
turtle.up()
turtle.goto(-150,50)
turtle.down()
#Ring 1
turtle.pensize(6)
turtle.pencolor("blue")
turtle.circle(50)

turtle.up()
turtle.goto(-40,50)
turtle.down()
#Ring 2

turtle.pensize(6)
turtle.pencolor("black")
turtle.circle(50)


turtle.done()