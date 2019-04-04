#coding=utf-8
import Tkinter as tk 
import ttk
win = tk.Tk()
win.title('My window')
win.geometry('200x200')
cv = tk.StringVar()
def show(event):
	print com.get()
com = ttk.Combobox(win,textvariable=cv)
com.pack()
com['value'] = ['山东','jiangsu','jiangxi','dongbei']
com.current(0)
com.bind('<<ComboboxSelected>>',show)
win.mainloop()



