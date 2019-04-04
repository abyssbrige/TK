#coding=utf-8
import Tkinter as tk 
window = tk.Tk()
window.title('My window')
window.geometry('200x200')
lab = tk.Label(window,text='',bg='green',width=20,height=2)
lab.pack()
def print_selection(v):
	#v scale参数默认传入
	lab.config(text='当前刻度'+v)
scale = tk.Scale(window,label='try me',from_=5,to=11,orient=tk.HORIZONTAL,length=200,
	showvalue=0,tickinterval=3,resolution=0.01,command=print_selection)
#label标签名字 orient 方向  showvalue 是否显示 tickinterval 数字间隔 resolution 精确度 
scale.pack()
window.mainloop()