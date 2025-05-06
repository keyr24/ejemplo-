import turtle

# Crear una ventana para el dibujo
ventana = turtle.Screen()
ventana.bgcolor("white")  # Color de fondo

# Crear una tortuga para dibujar
mi_tortuga = turtle.Turtle()
mi_tortuga.color("blue")  # Color del lápiz
mi_tortuga.pensize(3)     # Grosor de la línea

# Dibujar un círculo con radio de 100 píxeles
mi_tortuga.circle(100)

# Evitar que la ventana se cierre inmediatamente
ventana.mainloop()
