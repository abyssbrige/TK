import Tkinter as tk 
window = tk.Tk()
f = tk.Frame(window)
f.pack()
but = tk.Button(f,text='one',command=f.quit)
but.pack()

window.mainloop()
