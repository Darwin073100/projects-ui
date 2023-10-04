from turtle import *
import colorsys
import math
import turtle as tur


speed(0.25)
bgcolor("black")

# Genera los petalos
goto(0, -40)
h = 0

for i in range(16):
    for j in range(18):
        c= colorsys.hsv_to_rgb(0.125 , 1, 1)
        color(c)
        rt(90)
        circle(150-j*6, 90)
        lt(90)
        circle(150-j*6, 90)
        rt(180)
    circle(40, 24)

# Genera la parte centrall de la flor
color("black") 
shape("turtle")
fillcolor("brown")
phi = 137.508 * (math.pi/ 180.0)

for i in range (200):
    r = 4 * math.sqrt(i)
    theta = i*phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()
# Agregar texto
tur.penup()
tur.goto(0,300) 
tur.pendown()
tur.color("yellow") # Color del texto
tur.write("A YELLOW FLAWER FOR YOU", align="center", font=("Stencil", 15,"italic"))
# Agregar texto
tur.penup()
tur.goto(0,250) # Posición donde deseas agregar el texto
tur.pendown()
tur.color("gold") # Color del texto
tur.write("MY GIRL !!THIS IS YOUR YELLOW FLAWER(Claudia)¡¡", align="center", font=("Stencil", 15, "italic"))
done()