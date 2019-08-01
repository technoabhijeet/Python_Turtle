# Python_Turtle
Basic Python Turtle Programming

Basic Commands for Turtle in Python

Library From Python Sample

## Usage

```python
import turtle                 # allows us to use the turtles library

window = turtle.Screen()     # creates a graphics window
window.setup(400,440)      # set window dimension

circle_rad=50              # set the radius
rectangle_width=150   # set the width
rectangle_height=80   # set the height

alex = turtle.Turtle()   # create a turtle named alex   //Name Your Turtle 
alex.shape("turtle")    # alex looks like a turtle      // Shape of It
alex.color('red')         # alex has a color             // Pen Color
```


## Circle Drawing Usage
```python
alex.circle(radius)
```
## Navigation
```pyhton
alex.forward(steps) // Walks Forward

alex.backward(steps) //Walks Backward

alex.right(degree) // Rotate Right

alex.left(degree) //Rotate Left

```
