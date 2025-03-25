from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame

color = 'red'

def do_button_press() -> None:
    global color
    if color == 'red':
        color = 'green'
        canvas.itemconfigure(red_lamp, fill='black')
        canvas.itemconfigure(green_lamp, fill='green')
    elif color == 'green':
        color = 'yellow'
        canvas.itemconfigure(green_lamp, fill='black')
        canvas.itemconfigure(yellow_lamp, fill='yellow')
    else:
        color = 'red'
        canvas.itemconfigure(yellow_lamp, fill='black')
        canvas.itemconfigure(red_lamp, fill='red')


root = Tk()
frame = Frame(root) # Create a frame to hold all the widgets
frame.pack() # Make the frame fill the whole window

# Create a drawing surface within the frame
canvas = Canvas(frame, width=400, height=300)

# Draw the light frame
canvas.create_rectangle(150, 20, 250, 280, fill='orange')

# Add the red lamp
red_lamp = canvas.create_oval(170, 40, 230, 100, fill='red')
# Add the yellow lamp
yellow_lamp = canvas.create_oval(170, 120, 230, 180, fill='black')
# Add the green lamp
green_lamp = canvas.create_oval(170, 200, 230, 260, fill='black')

# Create a user-clickable button
button = Button(frame, text='Change', command=do_button_press)

button.grid(row=0, column=0)
canvas.grid(row=0, column=1)

root.mainloop()

