#Kaylen Nyhuis and Emily Rusch
import turtle

mood = input("How are you feeling? \n ")
pam = turtle.Turtle()
pam.width(8)
pam.speed(2)

def draw_star(color):
    for side in range(5):
        pam.color(color)
        pam.forward(100)
        pam.right(144)
if mood == "happy":
    draw_star("pink")
elif mood == "sad":
    draw_star("blue")
elif mood == "sleepy":
    draw_star("green")
else:
    draw_star("red")

