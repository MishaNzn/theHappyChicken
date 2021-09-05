from tkinter import *
import time
from tkinter import Canvas

tk = Tk()
tk.title('Happy Chicken')
tk.resizable(0, 0)
WIDTH = 500
HEIGHT = 500
c = Canvas(tk, width=WIDTH, height=HEIGHT, highlightthickness=0, bg='blue')
c.pack()
tk.update()
sprites = []
STAND = 0
GO = 1
action = STAND
images_left = [PhotoImage(file='ChickenLeft1.png'), PhotoImage(file='chickenLeft2.png')]
images_right = [PhotoImage(file='Chicken1.png'), PhotoImage(file='chicken2.png')]
chicken = c.create_image(WIDTH / 2, HEIGHT / 2, image=images_left[0], anchor='nw')


def change(image):
    global action
    if action == STAND:
        action = GO
    else:
        action = STAND
    c.itemconfig(chicken, image=image[action])
    c.update_idletasks()


def move_chicken(event):
    if event.keysym == 'a':
        change(images_left)
        c.move(chicken, -5, 0)
        time.sleep(0.2)
        change(images_left)
        time.sleep(0.2)
    elif event.keysym == 's':
        c.move(chicken, 0, 5)
        time.sleep(0.2)
    elif event.keysym == 'w':
        c.move(chicken, 0, -5)
        time.sleep(0.2)
    elif event.keysym == 'd':
        change(images_right)
        c.move(chicken, 5, 0)
        time.sleep(0.2)
        change(images_right)
        time.sleep(0.2)


c.bind_all('<Key>', move_chicken)
while 1:
    c.update_idletasks()
    c.update()
    time.sleep(0.01)
