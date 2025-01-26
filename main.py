import imagegen as ig
import configgen as cg
import tkinter as tk
from tkinter import filedialog

# IDEA: PLAY GAME OF LIFE WITH SIMPLESQUARE

# general purpose function to ask user for a file
def openFileDialog():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt")])
    return file_path 

cg.generateConfig(1, [[255, 255, 255], [0, 0, 0]])
ig.simpleSquare()

"""
root = tk.Tk()
root.title("File Dialog Example")

root.mainloop()
"""



