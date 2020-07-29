import tkinter as tk
import load_data
from random import randint

rand_data = load_data.LoadData()
vocab = rand_data.rand_vocab
vocab_true_def = rand_data.rand_vocab_def
vocab_def_1 = load_data.LoadData().rand_vocab_def
vocab_def_2 = load_data.LoadData().rand_vocab_def
vocab_def_3 = load_data.LoadData().rand_vocab_def
vocab_def_4 = load_data.LoadData().rand_vocab_def

definitions = [vocab_def_1, vocab_def_2, vocab_def_3, vocab_def_4, "i don't know"]
rand_int = randint(0,3)
definitions[rand_int] = vocab_true_def

root = tk.Tk()

v = tk.IntVar()
v.set(5)

def ShowChoice():
    if v.get() == rand_int:
        print("Correct")
    else:
        print("False")

tk.Label(root,
         text = "What is the definition of " + vocab,
         justify = tk.LEFT,
         padx = 20).pack()

for val, definition in enumerate(definitions):
    tk.Radiobutton(root,
                   text = definition,
                   indicatoron = 0,
                   width = 40,
                   padx = 10,
                   variable = v,
                   command = ShowChoice,
                   value = val).pack(anchor = tk.W)

root.mainloop()