from turtle import Turtle,Screen
import random
my_screen=Screen()
my_screen.bgcolor('Black')
user_bet=my_screen.textinput("turtlr race","guess who will win")
colors=['red','blue','white','yellow','green']
y_cor=[250,125,0,-125,-250]
turtle_list=[]
for i in range(5):
    tim=Turtle()
    tim.shape('turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(-300,y_cor[i])
    turtle_list.append(tim)
turtle_list[2].goto(300,300)
turtle_list[2].pendown()
turtle_list[2].goto(300,-300)
turtle_list[2].penup()
turtle_list[2].goto(-300,0)
gameon=True
while gameon:
    for tim in turtle_list:
        distance=random.randint(2,10)
        tim.forward(distance)
        if tim.xcor()>280:
            winner=tim.pencolor()
            gameon=False
result=Turtle()
result.hideturtle()
result.penup()
result.color('Orange')
result.goto(0,280)
if user_bet==winner:
    result.write(f"you won!{winner} turtle is the winner! ",align='center',font=('Areal',25,'bold'))
else:
     result.write(f"you lost!{winner} is the winner!",align='center',font=('Areal',25,'bold'))
my_screen.exitonclick()