import tkinter as tk
import time
from datetime import datetime
import pandas
import requests
from bs4 import BeautifulSoup
import CharismaCollector
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd

# global variable
global box

# initiate tkinter
window = tk.Tk()
window.title("<< IBS Calculator >>")
window.geometry("500x500")

# read detail csv file and get industry list and asset list
detail_csv = pd.read_csv('code-name-industry.csv')
industry_list = list(set(detail_csv["Industry"].values))
asset_list = list(set(detail_csv["Asset_Name"].values))


# label function
def labeler(message, mcolor="green"):
    return tk.Label(window, text=message, fg=mcolor).pack()


# read input
def read_input():
    result = box.get()  # I should call the Chart with the result.
    return result


# create a function for buttons
def mean_all():
    labeler("Your choice is average of all.", "green")
    # I should call the Chart directly.


def industry():
    labeler("Your choice is average of industry.", "green")
    labeler("Which industry are you looking for?", "black")
    global box
    box = tk.Entry(window)
    box.pack()
    box.focus_set()
    ok_button = tk.Button(window, text='OK', command=read_input)
    ok_button.pack()


def one_asset():
    labeler("Your choice is having only one asset.", "green")
    labeler("Which industry are you looking for?", "black")
    global box
    box = tk.Entry(window)
    box.pack()
    box.focus_set()
    ok_button = tk.Button(window, text='OK', command=read_input)
    ok_button.pack()
    labeler("words will be displayed backward, tkinter is not optimized for Farsi.", "red")


# pack is used to show the object in the window
labeler("Do you want an average of all, one industry or only one asset?\n", "black")

# add a button
button_all = tk.Button(window, text="All", fg="blue", command=mean_all).pack()
button_industry = tk.Button(window, text="One Industry", fg="blue", command=industry).pack()
button_one_asset = tk.Button(window, text="One Asset", fg="blue", command=one_asset).pack()

# let's begin
window.mainloop()
