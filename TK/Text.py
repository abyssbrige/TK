#coding=utf-8
import Tkinter as tk 
import time
window = tk.Tk()
window.title('Text 文本框')
text = tk.Text(window,width=20,height=2)
text.pack(side='left',fill=tk.Y) #充满Y轴
s = tk.Scrollbar() #滚动条
s.pack(side='right',fill='y')
text_str = '''sadasdasdadadsaddddddddddddddddddddddddddddddddddddddddddddddddddddddddasdasdas '''
text.insert('insert',text_str)
#关联
text.config(yscrollcommand=s.set,state="disabled")  #state=normal
s.config(command=text.yview)
# text.delete(0.0,tk.END) #清空text

# text.insert('insert', 'I love\n')
# text.insert('end', 'Study')
# text.insert('insert', 'I love Study !')
# print text.get('1.2','1.6')
#获取第一行第三列到第七列
# print text.get('1.2','1.end')
#获取第一行第三列到最后一个字符
window.mainloop()
