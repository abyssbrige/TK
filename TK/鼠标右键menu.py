#coding=utf-8
import Tkinter as tk 
win = tk.Tk()
win.title('My window')
win.geometry('200x200')
menubar = tk.Menu(win)
# menu = tk.Menu(menubar,tearoff=0)
for item in ['python','ruby']:
	menubar.add_command(label=item)
menubar.add_separator()
menubar.add_command(label='cut')
# menubar.add_cascade(label='语言',menu=menubar)
def showmenu(event):
	menubar.post(event.x_root,event.y_root) #鼠标跟随
#绑定事件
win.bind('<Button-3>',showmenu) #鼠标右击
win.mainloop()