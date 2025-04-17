from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    tran= Translator()
    trans1=tran.translate(text=text1,src=src1,dest=dest1)  
    return trans1
def data():
    s=cb1.get()
    d=cb2.get()
    txt=inpvar.get()
    txtget=change(text=txt,src=s,dest=d)
    out.set(txtget)





trans=Tk()
trans.geometry('800x800')
trans.title("translator".upper())
f1=Frame(bg="grey")
l1=Label(master=f1,text="~~>",font=("Times New Roman",40,"bold"),bg="grey",fg='black')
cb1=ttk.Combobox(f1,values=list(LANGUAGES.values()),font=("Times New Roman",20,"italic"))
cb2=ttk.Combobox(f1,values=list(LANGUAGES.values()),font=("Times New Roman",20,"italic"))
cb1.set("english")
cb2.set("kannada")
cb1.pack(side=LEFT,padx=20)
cb2.pack(side=RIGHT,padx=20)
l1.pack(expand=True,fill="both")
f1.pack(expand=True,fill="both")


inpvar=StringVar()
f2=Frame(bg="grey")
inp=Entry(f2,textvariable=inpvar,font=("Times New Roman",20,"italic"),fg='black')
but=Button(f2,text="translate",font=("Times New Roman",20,"italic"),fg='black',command=data)
inp.pack(expand=True,fill="both",padx=20,pady=20)
but.pack()

f2.pack(expand=True,fill="both")

f3=Frame(bg="grey")
out=StringVar()
outp=Entry(f2,text="input",textvariable=out,font=("Times New Roman",20,"italic"),fg='black')
outp.pack(expand=True,fill="both",padx=20,pady=10)
f3.pack(expand=True,fill="both")





trans.mainloop()
