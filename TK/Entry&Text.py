#coding=utf-8
import Tkinter as tk 
window = tk.Tk()
window.title('My window')
window.geometry('200x200')
en = tk.Entry(window,show=None,font=('楷体',14))  #show='*'
en.pack()
def insert_point():
	var = en.get() #获取entry的内容
	t.insert('insert',var)  #将获取内容插入文本框

def insert_end():
	var = en.get()
	t.insert('end', var)
b1 = tk.Button(window,text='insert_point',command=insert_point)
b1.pack()
b2 = tk.Button(window,text='insert_end',command=insert_end)
b2.pack()
t = tk.Text(window,height=2)
t.pack()
window.mainloop()
