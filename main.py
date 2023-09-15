from tkinter import *
import random

#global variable
count = 0

# create root window
root = Tk()

# root window title and dimension
root.title("Pokemon Shiny Number Generator Sim")

# Set geometry(widthxheight)
root.geometry('500x400')

# Title label
lbl = Label(root, text="Did Shiny Appear? (Currently only 1/8192 will add variables later)")
lbl.grid(row = 0, column = 0)

# Counter for number of tries
counter = Label(root, text="Number of Tries: 0")
counter.grid(row =5, column = 0, sticky = W)

#Label that tells us if we got shiny or not
answer = Label(root, text="-----")
answer.grid(row=3, column = 0, sticky = W)

def generate(chance):
    #Base gen 1 - 4
    poke = random.randint(0, chance)
    return poke

def button_press():
    global count
    #Generate Numb, We'll add more functionality in getting varaibles to change the chance of shiny
    poke = generate(8191)

    if poke == 0:
        answer.configure(text = "Yes, It's Shiny")
    else:
        answer.configure(text="Nope, It's Not Shiny")

    count += 1
    counter.configure(text = "Number of tries: " + str(count))

#Button
btn = Button(root, text="Generate", fg = "blue", command = button_press)
btn.grid(row=2, column = 0)


# Execute Tkinter
root.mainloop()

