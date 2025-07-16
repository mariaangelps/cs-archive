import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart Message Book")
screen.setup(width=800, height=700)

# Writer turtle for text
writer = turtle.Turtle()
writer.hideturtle()
writer.speed(0)
writer.color("white")


animator = turtle.Turtle()
animator.hideturtle()
animator.speed(8)

# Drawer turtle for heart
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(8)

# Global variable to track the current page
current_page = 1

# Function to display page turn animation
def page_turn_animation(direction):
    animator.clear()
    animator.penup()
    animator.goto(-400 if direction == "right" else 400, 0)
    animator.pendown()
    animator.color("gray")
    animator.begin_fill()
    for _ in range(2):
        animator.forward(800)
        animator.left(90)
        animator.forward(700)
        animator.left(90)
    animator.end_fill()
    time.sleep(0.5)
    animator.clear()


def page_1():
    writer.clear()
    writer.penup()
    writer.goto(0, 100)
    writer.write("Page 1", align="center", font=("Georgia", 24, "bold"))
    writer.goto(0, 0)
    writer.write("Ahora una historia de noche!\n\n"
                 "Use the Right Arrow → to turn the page.",
                 align="center", font=("Georgia", 16, "normal"))

# Page 2: 
def page_2():
    writer.clear()
    writer.penup()
    writer.goto(0, 100)
    writer.write("Page 2", align="center", font=("Georgia", 24, "bold"))
    writer.goto(0, 0)
    writer.write("Once upon a time... había un príncipe en un reino muy muy lejano.\n\n"
                 "Que encontró a su princesa y formaron un amor real\n"
                 "Keep turning the pages!\n"
                 "Press the Right Arrow → again.",
                 align="center", font=("Georgia", 16, "normal"))

# Page 3
def page_3():
    writer.clear()
    writer.penup()
    writer.goto(0, 100)
    writer.write("Page 3", align="center", font=("Georgia", 24, "bold"))
    writer.goto(0, 0)
    writer.write("Y de pronto... la princesa con el corazón roto tuvo que irse a su reino para seguir estudiando\n\n"
                 "Y el príncipe prometió esperarla, con la esperanza de que se volverían a encontrar.\n"
                 "Pasaron los meses y se extrañaban más y más..!\n"
                 "Press the Right Arrow → again.",
                 align="center", font=("Georgia", 16, "normal"))

# Page 4
def page_4():
    writer.clear()
    writer.penup()
    writer.goto(0, 100)
    writer.write("Page 4", align="center", font=("Georgia", 24, "bold"))
    writer.goto(0, 0)
    writer.write("Parecía que los días no pasaban, se iban a dormir con su corazoncito triste.\n\n"
                 "Hasta que un día se decidieron encontrar...\n"
                 "Y... !\n"
                 "Press the Right Arrow → again.",
                 align="center", font=("Georgia", 16, "normal"))

# Page 5
def page_5():
    writer.clear()
    writer.penup()
    writer.goto(0, 220)
    writer.write("Page 5", align="center", font=("Georgia", 24, "bold"))
    writer.goto(0, 0)
    writer.write("Ansiosos de su encuentro, decidieron pensar en qué manera sus días contar.\n\n"
                 "Y así fue como hicieron una cuenta especial en una app.\n"
                 "Ahora ya son solo 10 días de poder abrazarte y darte todo el amor\n"
                 "que tanta falta nos hace.\n\n"
                 "No quiero nunca más discutir contigo.\n"
                 "Simplemente gracias por no rendirte.\n\n"
                 "Te dejo un regalito que en su momento no te lo pude dar,\n"
                 "pero ahora que hice este libro, no podía desaprovechar.\n\n"
                 "Press the Right Arrow → again.",
                 align="center", font=("Georgia", 14, "normal"))

# Page 6: Draw heart and display message
def page_6():
    writer.clear()
    drawer.clear()

    # Draw heart shape
    drawer.penup()
    drawer.goto(0, -200)
    drawer.pendown()
    drawer.color("brown")
    drawer.begin_fill()
    drawer.left(140)
    drawer.forward(224)
    for _ in range(200):  # Left curve
        drawer.right(1)
        drawer.forward(2)
    drawer.left(120)
    for _ in range(200):  # Right curve
        drawer.right(1)
        drawer.forward(2)
    drawer.forward(224)
    drawer.end_fill()

    # Write the message
    writer.penup()
    writer.goto(0, -50)
    writer.color("white")
    writer.write(
        "\n"
        "Afortunada de llamarte mi novio,\n"
        "pero ahora más, de que seas el\n"
        "hombrecito de mi vida.\n\n"
        "Feliz día al hombrecito más\n"
        "importante en mi vida.\n"
        "Te adoro gordito 🤎️\n"
        "11-19-2024",
        align="center",
        font=("Georgia", 14, "bold")
    )

# Function to navigate forward
def next_page():
    global current_page
    if current_page < 6:
        page_turn_animation("right")
        current_page += 1
        if current_page == 2:
            page_2()
        elif current_page == 3:
            page_3()
        elif current_page == 4:
            page_4()
        elif current_page == 5:
            page_5()
        elif current_page == 6:
            page_6()

# Function to navigate backward
def prev_page():
    global current_page
    if current_page > 1:
        page_turn_animation("left")
        current_page -= 1
        if current_page == 5:
            page_5()
        elif current_page == 4:
            page_4()
        elif current_page == 3:
            page_3()
        elif current_page == 2:
            page_2()
        elif current_page == 1:
            page_1()

# Key bindings
screen.listen()
screen.onkey(next_page, "Right")
screen.onkey(prev_page, "Left")

# Start with Page 1
page_1()

# Keep the window open
screen.mainloop()
