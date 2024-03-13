from tkinter import *
import pandas as pd
import random
## Read file
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/portugues_ingles.csv")
finally:
    data_dict = data.to_dict(orient="records")
card = {}

##Functions declaration:
def next_card():
    global card, timer, data_dict
    window.after_cancel(timer)
    card = random.choice(data_dict)
    flash_card.itemconfig(card_image, image=portuguese_image)
    flash_card.itemconfig(card_lang, text="Português")
    flash_card.itemconfig(card_word, text=card["Português"])
    timer = window.after(3000,func=change_idiom)

def change_idiom():
    flash_card.itemconfig(card_image, image=english_image)
    flash_card.itemconfig(card_lang, text="Inglês")
    flash_card.itemconfig(card_word, text=card["Inglês"])
def correct():
    data_dict.remove(card)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
##Constants
BACKGROUND_COLOR = "#B1DDC6"


##Start program:
window = Tk()
window.config(padx = 50, pady= 50, bg = BACKGROUND_COLOR)
english_image = PhotoImage(file='images/card_back.png')
portuguese_image = PhotoImage(file ="images/card_front.png")
timer = window.after(3000, func=change_idiom)
wrong = PhotoImage(file="images/wrong.png")
wrong_b = Button(image = wrong, highlightthickness=0, command=next_card)
right = PhotoImage(file="images/right.png")
right_b = Button(image = right, highlightthickness=0, command=correct)
flash_card = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_image = flash_card.create_image(400, 263, image=portuguese_image)
card_lang = flash_card.create_text(400, 150, text = "Title", font=("Arial", 40, "italic"))
card_word = flash_card.create_text(400,263, text= "word", font=("Arial", 60, "bold"))

flash_card.grid(row=0, column=0, columnspan=2)
wrong_b.grid(row = 1, column = 0)
right_b.grid(row = 1, column = 1)

next_card()
window.mainloop()