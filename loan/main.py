from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from customtkinter import *

#Opening page after the splash
root =Tk()
image =PhotoImage(file="unsplash1.png")
height =240
width =400
x= (root.winfo_screenwidth()/2)-(width//2)
y=(root.winfo_screenheight()//2)-(height//2)
root.geometry("%dx%d+%d+%d" % (width,height,x,y))
root.overrideredirect(True)
root.config(bg='#272727')
big_label=Label(root,image=image,bg="#272727",width=390,height=200)
big_label.place(x=3,y=4)
progress_label=Label(root,text="loading.",bg="#272727",fg="white",font=("Trebuchet Ms",10))
progress_label.place(x=365,y=210)

progress=ttk.Style()
progress.theme_use("clam")
progress.configure("red.Horizontal.TProgressbar",background="#108cff")
progress=Progressbar(root,orient=HORIZONTAL,length=360,mode="determinate",style="red.Horizontal.TProgressbar")
progress.place(x=4.5,y=214)

def top():
    root.withdraw()
    os.system("python bike_park.py")
    root.destroy()

i=0
def load():
    global i
    if i <=100:
        txt=''+(str(i))+'%'
        progress_label.config(text=txt)
        progress_label.after(300,load)
        progress['value']=1*i
        i+=1
    else:
          top()

load()

root.resizable(False,False)
root.mainloop()