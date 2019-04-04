#coding=utf-8
import Tkinter as tk 
window = tk.Tk()  #创建窗体
window.title('My window') #窗体名字
window.geometry('400x300') #设置窗体大小
var = tk.StringVar()  #tk内置字符串型变量
lab = tk.Label(window,textvariable=var,bg='red',font=('楷体',14),width=20,height=2)
# textvariable表示Label值为变量
lab.pack() #放置
hit_me = False
def onclick():
	global hit_me
	if hit_me == False:
		hit_me = True
		var.set('I will hit you')
	else:
		hit_me = False
		var.set('')
but = tk.Button(window,command=onclick,text='hit_me',width=10,height=1)
but.pack()
window.mainloop()

