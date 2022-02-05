import colorgram
import random 
from turtle import Turtle,Screen,colormode

def find_colors():
    colors = colorgram.extract('E:\\Udemy_Training\\Hirst_lead.jpg',15)
    
    color_list=[]
    for i in range(0,15):
        first_color = colors[i]
        rgb = first_color.rgb 
        color = (rgb.r,rgb.g,rgb.b)
        color_list.append(color)

    return color_list    
    
def random_color(color_list):
         random_color=random.choice(color_list)    
         return random_color


def Hist_painting(color_list):
    
    for l in range (1,11):
        for j in range(0,10):
                random=random_color(color_list)
                timmy.pencolor(random)
                timmy.penup()
                timmy.forward(50)
                timmy.pendown()
                timmy.pencolor()
                timmy.forward(1)
            
        timmy.penup()
        timmy.setpos(0,l*20)
        timmy.pendown()

timmy=Turtle()
timmy.shape('turtle')
timmy.setpos(0,0)
colormode(255)
timmy.pensize(20)
color_list=find_colors()
Hist_painting(color_list)


screen=Screen()
screen.exitonclick()