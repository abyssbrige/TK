#coding=utf-8
import Tkinter as tk 
import ttk
win = tk.Tk()
win.title('表格')
win.geometry('600x400+200+20')
tree = ttk.Treeview(win,columns=['1','2','3','4'],show='headings')
#定义列
# tree['columns'] = ('域名','ip解析','开放端口','网站指纹信息')
tree.pack()
#设置列
tree.column('1',width=100,anchor='center')
tree.column('2',width=100,anchor='center')
tree.column('3',width=100,anchor='center')
tree.column('4',width=100,anchor='center')
#设置头
tree.heading('1',text='域名')
tree.heading('2',text='ip解析')
tree.heading('3',text='开放端口')
tree.heading('4',text='网站指纹信息')
#添加数据
port = ['80','50','60']
tree.insert('',0,values=('www.baidu.com','192.168.10.2',port,'CMS'))
def onclick(event):
	# for item in tree.selection():
	# 	item_text = tree.item(item,'values')
	# 	print item_text[0]
	for item in tree.item(tree.selection())['values']:
		print item
tree.bind('<ButtonRelease-1>',onclick)
win.mainloop()
