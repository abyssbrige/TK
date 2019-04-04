#coding=utf-8
import Tkinter as tk 
window = tk.Tk()
window.title('My window')
window.geometry('300x200')
var1 = tk.StringVar()
lab = tk.Label(window,textvariable=var1,bg='yellow',width=5,height=2)
lab.pack()
def print_selection():
	var1.set(li.get(li.curselection()))
but = tk.Button(window,text='print selection',command=print_selection)
but.pack()
var2 = tk.StringVar()
var2.set((11,22,33,44,55))
li = tk.Listbox(window,listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
	li.insert('end',item)
li.insert(1,'first')
li.pack()
window.mainloop()