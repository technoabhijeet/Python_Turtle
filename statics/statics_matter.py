#My Charts Challenge - www.101computing.net/my-charts/
import turtle

screen = turtle.Screen()
myPen=turtle.Turtle()
myPen.speed(0)
myPen.shape('turtle')
myPen.width(3)


def drawColumnChart(value1,value2,value3,value4,value5):
  global myPen
  zoom = 3
  #Start adding a title to our chart
  myPen.color("#000000")
  myPen.penup()
  myPen.goto(-30,120)
  myPen.write("Browser Statistics", None, "center", "20pt bold")
  myPen.fillcolor("#DB148E")
  
  #Then draw the x and y axis
  myPen.goto(-160,-100)
  myPen.pendown()  
  myPen.goto(-160,100)
  myPen.penup()
  myPen.goto(-160,-100)
  myPen.pendown()  
  myPen.goto(100,-100)
  
  #draw the first column
  myPen.color("#DB148E")
  myPen.penup()
  myPen.goto(-120,-100)
  myPen.begin_fill()
  myPen.left(90)
  myPen.forward(value1*zoom)
  myPen.left(90)
  myPen.forward(30)
  myPen.left(90)
  myPen.forward(value1*zoom)
  myPen.left(90)
  myPen.forward(30)
  myPen.end_fill()  
  
  #Add data label:
  myPen.goto(-130, value1*zoom -100 +10)
  myPen.write(str(value1)+"%", None, "center", "16pt bold")
  myPen.goto(-100,-100)
  
  #Complete the code for drawing the other 4 columns


#Main Progran Starts Here
ie = 14
firefox = 12
other = 10
chrome = 44
safari = 20


drawColumnChart(chrome,safari,ie,firefox,other)
screen.tracer(0)
