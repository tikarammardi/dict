from tkinter import *

import json
from difflib import get_close_matches

window = Tk(className=" Dictionary")

def translate(word) :

    data = json.load(open("data.json"))


    word = word.lower()
    if word in data :
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0 :
        yes_no ="Did you mean ", get_close_matches(word,data.keys())[0] ," instead? Click Yes Or NO "
        t1.insert(END, yes_no)
        if yes_no == "y" :
            return data[get_close_matches(word,data.keys())[0]]
        elif yes_no == "n" :
            return "The word doesn't exist. Please double check it."
        else :
            return "We didn't understand your entry"
    else :
        return "The word doesn't exist.Please double check it."

def operation() :

        word = e1_value.get()
        result = translate(word)

        if type(result) == list :
            for item in result :
                t1.insert(END,item)
        else :
            t1.insert(END,item)   

   

b1 = Button(window, text = "Search",command =  operation)
b1.grid(row = 0, column=0)

b2 = Button(window, text="Yes")
b2.grid(row=1,column=0)

b3 = Button(window, text="No")
b3.grid(row=1,column=1)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0,column=1)

e2_value = StringVar()


t1 = Text(window)
t1.grid(row=0,column=2)

window.mainloop()