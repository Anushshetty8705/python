from tkinter import *
def calcu():
    try:
        out.set(eval(out.get()))
    except:
        out.set("wrong input")

def dis(val):
    x=out.get()
    out.set(x+val)
calci=Tk()
calci.title("calculator".upper())
calci.geometry("300x450")
calci.config(bg="purple")
for i in range(6):
    calci.rowconfigure(i,weight=1)

for i in range(4):
    calci.columnconfigure(i,weight=1)
out=StringVar()

screen=Entry(font=("Palatino",20,"bold"),bg="purple",fg='yellow',justify="right",textvariable=out)
screen.grid(row=0,column=0,columnspan=4,sticky="ewns",padx=5,pady=5)

button_clear=Button(text='AC',font=("Palatino",30,"italic"),bg="purple",fg='white',command =lambda :out.set(" "))
button_clear.grid(row=1,column=0,sticky="ewns",padx=5,pady=5)

button_mod=Button(text='R',font=("Palatino",30,"italic"),bg="purple",fg='white',command=lambda : dis("%"))
button_mod.grid(row=1,column=1,sticky="ewns",padx=5,pady=5)
y=out.get()
button_back=Button(text='C',font=("Palatino",30,"italic"),bg="purple",fg='white',command = lambda :   out.set(out.get()[:-1]))
button_back.grid(row=1,column=2,sticky="ewns",padx=5,pady=5)

button_div=Button(text='/',font=("Palatino",30,"italic"),bg="purple",fg='white',command=lambda : dis("/"))
button_div.grid(row=1,column=3,sticky="ewns",padx=5,pady=5)

button_7=Button(text='7',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("7"))
button_7.grid(row=2,column=0,sticky="ewns",padx=5,pady=5)

button_8=Button(text='8',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("8"))
button_8.grid(row=2,column=1,sticky="ewns",padx=5,pady=5)

button_9=Button(text='9',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("9"))
button_9.grid(row=2,column=2,sticky="ewns",padx=5,pady=5)

button_MUL=Button(text='*',font=("Palatino",30,"bold"),bg="purple",fg='white',command=lambda : dis("*"))
button_MUL.grid(row=2,column=3,sticky="ewns",padx=5,pady=5)

button_4=Button(text='4',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("4"))
button_4.grid(row=3,column=0,sticky="ewns",padx=5,pady=5)

button_5=Button(text='5',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("5"))
button_5.grid(row=3,column=1,sticky="ewns",padx=5,pady=5)

button_6=Button(text='6',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("6"))
button_6.grid(row=3,column=2,sticky="ewns",padx=5,pady=5)

button_SUB=Button(text='-',font=("Palatino",30,"bold"),bg="purple",fg='white',command=lambda : dis("-"))
button_SUB.grid(row=3,column=3,sticky="ewns",padx=5,pady=5)

button_1=Button(text='1',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("1"))
button_1.grid(row=4,column=0,sticky="ewns",padx=5,pady=5)

button_2=Button(text='2',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("2"))
button_2.grid(row=4,column=1,sticky="ewns",padx=5,pady=5)

button_3=Button(text='3',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("3"))
button_3.grid(row=4,column=2,sticky="ewns",padx=5,pady=5)

button_ADD=Button(text='+',font=("Palatino",30,"italic"),bg="purple",fg='white',command=lambda : dis("+"))
button_ADD.grid(row=4,column=3,sticky="ewns",padx=5,pady=5)


button_00=Button(text='00',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("00"))
button_00.grid(row=5,column=0,sticky="ewns",padx=5,pady=5)

button_0=Button(text='0',font=("Palatino",30,"italic"),bg="purple",fg='yellow',command=lambda : dis("0"))
button_0.grid(row=5,column=1,sticky="ewns",padx=5,pady=5)

button_DOT=Button(text='.',font=("Palatino",30,"bold"),bg="purple",fg='white',command=lambda : dis("."))
button_DOT.grid(row=5,column=2,sticky="ewns",padx=5,pady=5)

button_EQ=Button(text='=',font=("Palatino",30,"bold"),bg="purple",fg='white',command=calcu)
button_EQ.grid(row=5,column=3,sticky="ewns",padx=5,pady=5)

calci.mainloop()