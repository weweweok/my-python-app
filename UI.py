from tkinter import *
from tkinter import ttk

# Ui model 

window = Tk()
window.geometry("630x360")
window.title("SCRAPING")



top = ttk.Frame(window)
label_size = 28
ttk.Label(top,
		  text= "Enter parametor for scraping",
		  font=("Arial", label_size, "bold")).grid(sticky= N)
top.pack(side="top")


left = ttk.Frame(window)
font_size = 20
ttk.Label(left,
		  text= "URL:",
		  font=("Arial", font_size, "bold"),
		  ).pack()

ttk.Label(left,
		  text= "element:",
		  font=("Arial", font_size, "bold"),
		  ).pack()

ttk.Label(left,
		  text= "class:",
		  font=("Arial", font_size, "bold"),
		  ).pack()

left.place(x=100,y=80)

frame2= ttk.Frame(window)
text_width = 20
URL = Entry(frame2,
	 		bg="white",
	 		font=("Arial",font_size),
	 		width=text_width,
	 		).pack()

element = Entry(frame2,
	 		bg="white",
	 		font=("Arial",font_size),
	 		width=text_width
	 		).pack()

class_name = Entry(frame2,
	 		bg="white",
	 		font=("Arial",font_size),
	 		width=text_width
	 		).pack()

frame2.place(x=250,y=80)


Button(window,
		text="O K",
		font=(300),
		compound="bottom").place(x=270,y=200)

window.mainloop()