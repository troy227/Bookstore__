

from tkinter import *
from backend import Database
database=Database()
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def scommand():
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),book_text.get(),isbn_text.get()):
        list1.insert(END,row)

def ecommand():

    database.insert(title_text.get(),author_text.get(),book_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),book_text.get(),isbn_text.get()))

def dcommand():
    database.delete(selected_tuple[0])


window=Tk("Book")
window.wm_title("BOOKSTORE")


l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

#TITLE ENTRY
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)
#AUTHOR ENTRY
author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)
#BOOK ENTRY
book_text=StringVar()
e3=Entry(window,textvariable=book_text)
e3.grid(row=1,column=1)
#ISBN ENTRY
isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)
#LISTBOX FOR RESULTS
list1=Listbox(window,height=6,width=40)
list1.grid(row=2,column=0,rowspan=7,columnspan=2)
#SCROLLBAR
s1=Scrollbar(window)
s1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=s1.set)
s1.configure(command=list1.yview())
list1.bind('<<ListboxSelect>>',get_selected_row)
#####

b1=Button(window,text="View All",width=12,height=1,command=view_command )
b1.grid(row=2,column=3)


b2=Button(window,text="Search Entry",width=12,command=scommand)
b2.grid(row=4,column=3)

b3=Button(window,text="Add Entry",width=12,command=ecommand)
b3.grid(row=5,column=3)



b5=Button(window,text="Delete",width=12,command=dcommand)
b5.grid(row=7,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=8,column=3)


window.mainloop()
