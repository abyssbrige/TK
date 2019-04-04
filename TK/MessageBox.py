#coding=utf-8
import Tkinter as tk 
import tkMessageBox
window = tk.Tk()
window.title('My window')
window.geometry('200x200')
# tk.Label(window,bg='green',text='hit me').pack()
def hit_me():
	# tkMessageBox.showinfo(title='hi',message='hahhahahahaha')
	# tkMessageBox.showwarning(title='hi',message='有警告！')
	# tkMessageBox.showerror(title='hi',message='有错误！')
	# tkMessageBox.askquestion(title='hi',message='yes or no')
	# tkMessageBox.askyesno(title='hi',message='yes or no ')

tk.Button(window,text='hit me',command=hit_me).pack()
window.mainloop()

