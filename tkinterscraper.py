#! program_to_use
import svgwrite
from tkinter import *
import requests
from bs4 import BeautifulSoup

 

def str_to_sort_list(event):
	s1 = ent1.get()
	s2 = ent2.get()
	s3 = ent3.get()
	s4 = ent4.get()

	page = requests.get(s1, verify=False) # get-запрос
	soup = BeautifulSoup(page.text, 'html.parser')
	raw = soup.find(s2, class_=s3).text

	f = open(s4,"w+")
	f.write(raw)
	f.close()


root = Tk()


lbl1 = Label(text="url сайта", width=35)
ent1 = Entry(width=35)
lbl2 = Label(text="тег", width=35)
ent2 = Entry(width=35)
lbl3 = Label(text="класс", width=35)
ent3 = Entry(width=35)
lbl4 = Label(text="как сохранить.txt", width=35)
ent4 = Entry(width=35)
lbl5 = Label(text="", width=35)

but = Button(text="спарсить")
 
but.bind('<Button-1>', str_to_sort_list) 

lbl1.pack()
ent1.pack()
lbl2.pack()
ent2.pack()
lbl3.pack()
ent3.pack()
lbl4.pack()
ent4.pack()
lbl5.pack()
but.pack()
root.mainloop()



#'https://liraltd.com/semconf-2018'
#'div'
#'blogpost'
#"werwer.txt"
