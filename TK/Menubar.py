#coding=utf-8
import Tkinter as tk 
window = tk.Tk()
window.title('My window')
window.geometry('200x200')
lab = tk.Label(window,text='',bg='green',width=20,height=2)
lab.pack()
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff=0)
count = 0
def do_it():
	global count
	count += 1
	lab.config(text=count)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=do_it)
filemenu.add_command(label='Open',command=do_it)
filemenu.add_separator()
filemenu.add_command(label='exit',command=window.quit)
window.config(menu=menubar)
window.mainloop()