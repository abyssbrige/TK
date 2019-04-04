#coding=utf-8
import Tkinter as tk 
window = tk.Tk()
window.title('My window')
window.geometry('300x200')
var = tk.StringVar()
# lab = tk.Label(window,text='empty',width=20,bg='green')
lab = tk.Label(window,textvariable=var,width=20,bg='green')
lab.pack()
def radio_buttion():
	# lab.config(text=var.get())
	pass
rad1 = tk.Radiobutton(window,text='OPTION A',variable=var,value='A',command=radio_buttion)
rad1.pack()
rad2 = tk.Radiobutton(window,text='OPTION B',variable=var,value='B',command=radio_buttion)
rad2.pack()
window.mainloop()