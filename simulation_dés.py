#coding:utf-8
import matplotlib.pyplot as plt
import random
import tkinter

number = 0#valeur par défaut

def sim():
    nombre_de_départ = number
    liste = []
    while nombre_de_départ > 0:
        for i in range(nombre_de_départ):
            i = random.randint(1,6)
            if i == 6: 
                nombre_de_départ -= 1
        liste.append(nombre_de_départ)
    graph(len(liste), liste)

def graph(x, y):
    X=range(0,x)
    Y=y
    plt.axis([0,x,0,Y[0]+10])
    plt.plot(X,Y,'+', color='black')
    plt.grid()
    plt.show()

def collect_entry(*args):
    global number
    number = var_entry.get()

#programme principale
win = tkinter.Tk()
win.geometry('600x400')
win.title('Simulation de dés')

label = tkinter.Label(text='Entrer le nombre de dés présents au départ', font=('Ariel', 15), width=40, height=2)
label.place(x=80, y=10)

var_entry = tkinter.IntVar()
var_entry.trace("w", collect_entry)
entry = tkinter.Entry(win, textvariable=var_entry ,width=50)
entry.place(x=150, y=60)

button = tkinter.Button(win, text='Effectuer la modélisation', width=30, height=5, command=sim)
button.place(x=190, y=90)

win.mainloop()
