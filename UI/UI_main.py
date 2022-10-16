from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from scraping_file import scraping

# Ui model 

class UI_main:
	def __init__(self, app):
		self.widgets(app)

	def widgets(self, app):
		#top label title
		self.label_size = 28
		self.top = ttk.Frame(window)
		self.top_label = ttk.Label(self.top,
		  							text= "Enter parametor for scraping",
		  							font=("Arial", self.label_size , "bold")).grid(sticky= N)
		self.top.pack(side="top")

		#label widget side left
		self.font_size = 18
		self.text_width = 20
		self.left_frame = ttk.Frame(app)
			
		self.URL_label = ttk.Label(self.left_frame,
									text= "URL:",
									font=("Arial", self.font_size, "bold") ).pack()

		self.element_label = ttk.Label(self.left_frame,
		  								text= "element:",
		  								font=("Arial", self.font_size, "bold") ).pack()

		self.class_label = ttk.Label(self.left_frame,
		  							 text= "class:",
		  							 font=("Arial", self.font_size, "bold") ).pack()

		self.left_frame.place(x=100,y=80)

		# entry widget right side
		self.right_frame = ttk.Frame(app)
			
		self.URL_str = StringVar()
		self.URL = ttk.Entry(self.right_frame,
							textvariable=self.URL_str ,
	 						font=("Arial",self.font_size),
	 						width=self.text_width ).pack()

		self.element_str = StringVar()
		self.element = ttk.Entry(self.right_frame,
								textvariable=self.element_str,
								font=("Arial",self.font_size),
	 							width=self.text_width ).pack()

		self.class_str = StringVar()
		self.class_name = ttk.Entry(self.right_frame,
									textvariable=self.class_str,
	 								font=("Arial",self.font_size),
	 								width=self.text_width ).pack()
		self.right_frame.place(x=250,y=80)


		# button (place bottom) 
		self.OK = ttk.Button(app,
					text="O K",
					compound="bottom",
					command= self.start,
					default="active").place(x=270,y=200)


	def start(self):
		# get string from any other entry widget
		URL = self.URL_str.get()
		print(URL)
		element = self.element_str.get()
		print(element)
		class_name = self.class_str.get()
		print(class_name)

		if (URL == ""):
			messagebox.showerror(message="you need any URL string !!\n entry again.", title="SCRAPING")
			return None

		get_info = scraping.Get_data(URL)
		data_contaner = []
		data_contaner.append(get_info.get_element_class(element, class_name))

		URL.delete(0,END)
		element.delete(0,END)
		class_name.delete(0,END)

		scraping.write_csv(data_contaner)

		messagebox.showinfo(message="scraping finished . :)")


if __name__ == "__main__":
	window = Tk()
	window.geometry("630x360")
	window.title("SCRAPING")

	top = UI_main(window)

	window.mainloop()














