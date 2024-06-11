from tkinter import * 
import pandas
from random import choice

try:
    file = pandas.read_csv("data/words_to_learn.csv")
except:
    file = pandas.read_csv("data/french_words.csv")
finally:
    dict = file.to_dict(orient= "records")
current_card = {}

def read_data():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image= front_card)
    canvas.itemconfig(title, text= "French", fill= "black")
    current_card = choice(dict)
    canvas.itemconfig(word, text= current_card.get("French"), fill= "black")
    flip_timer = window.after(5000, flip_card)
  
def flip_card():
    canvas.itemconfig(canvas_image, image= back_card)
    canvas.itemconfig(title, text= "English", fill= "white")
    canvas.itemconfig(word, text= current_card.get("English"), fill= "white")
    
def right():
    global current_card
    dict.remove(current_card)
    data = pandas.DataFrame(dict)
    data.to_csv("data/words_to_learn.csv")
    read_data()
    
window = Tk()
window.title("Flash Cards")
window.config(padx= 50, pady= 50, bg= "#B1DDC6")

flip_timer = window.after(5000, flip_card)

canvas = Canvas(width= 800, height= 526, highlightthickness= 0, bg= "#B1DDC6")
front_card = PhotoImage(file= "data/card_front.png")
back_card = PhotoImage(file= "data/card_back.png")
canvas_image = canvas.create_image(400, 263, image = front_card)
title = canvas.create_text(400, 150, text = "Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text = "Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row= 0, columnspan= 2)

right_image = PhotoImage(file= "data/right.png")
right_button = Button(image= right_image, highlightthickness= 0, command= right)
right_button.grid(column= 1, row= 1)

wrong_image = PhotoImage(file= "data/wrong.png")
wrong_button = Button(image= wrong_image, highlightthickness= 0, command= read_data)
wrong_button.grid(column= 0, row= 1)

read_data()

window.mainloop()