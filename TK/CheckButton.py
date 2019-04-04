#coding=utf-8
import Tkinter as tk 
window = tk.Tk()
window.title('My window')
window.geometry('200x200')
lab = tk.Label(window,text='',bg='green',width=20,height=2)
lab.pack()
var1 = tk.IntVar()
var2 = tk.IntVar()
def print_selection():
	if (var1.get()==1)&(var2.get()==0):
		lab.config(text='I only love python')
	elif (var1.get()==0)&(var2.get()==1):
		lab.config(text='I only love c++')
	elif (var1.get()==1)&(var2.get()==1):
		lab.config(text='I love both')
	else:
		lab.config(text='I do not love either')
c1 = tk.Checkbutton(window,text='python',variable=var1,command=print_selection)
c2 = tk.Checkbutton(window,text='c++',variable=var2,command=print_selection)
c1.pack()
c2.pack()
window.mainloop()