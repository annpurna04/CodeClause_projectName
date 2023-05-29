import pyshorteners
from tkinter import*

window =Tk()
window.geometry("400x720")
window.config(bg="violet")

def short():
    url = E1.get()
    S = pyshorteners.Shortener().tinyurl.short(url)
    E2.insert(END,S)

Label(window,text="Enter your URL Link",font="impack 40",bg="purple",fg="white").pack(fill='x')
E1 = Entry(window,font="Ariel 20",bd=3,width=40)
E1.pack(pady=30)

Button(window,text="CLICK",font="bold 18",bg="darkorchid",fg="white",command = short).pack()

E2=Entry(window,font="impact 16 bold",bg="violet",width=24,bd=0)
E2.pack(pady=30)
mainloop()