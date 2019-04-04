from Tkinter  import *
class App(object):
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()
		self.button1 = Button(frame,text='QUIT',command=frame.quit)
		self.button1.pack(side=LEFT)
		self.button2 = Button(frame,text='Hello',command=self.print_text)
		self.button2.pack(side=LEFT)
	def print_text(self):
		print 'hello world'
window = Tk()
root = App(window)
window.mainloop()

