import time
from tkinter import *
from math import sin, cos,radians



def mov_sec():
    def move():
        t=time.localtime()
        angle=radians((t.tm_sec)*6)
        x1=400+250*sin(angle)
        y1=400-250*cos(angle)
        canvas.coords(seconds,400,400,x1,y1)
        if 0<t.tm_sec<=9:
            canvas.itemconfig(show_sec,text=f"0{t.tm_sec}")
        else:
            canvas.itemconfig(show_sec,text=f"{t.tm_sec}")

        canvas.after(1000,move)

    t=time.localtime()
    sec=t.tm_sec
    sec_angle=radians(sec*6)
    x= 400+250*sin(sec_angle)
    y= 400-250*cos(sec_angle)
    canvas.coords(seconds,400,400,x,y)
    canvas.after(100,move)

def mov_min():
    def move():
        t=time.localtime()
        angle=radians((t.tm_min)*6)
        x1=400+175*sin(angle)
        y1=400-175*cos(angle)
        canvas.coords(minutes,400,400,x1,y1)
        if 0<t.tm_min<=9:
            canvas.itemconfig(show_min,text=f" 0{t.tm_min} :")
        else:
            canvas.itemconfig(show_min,text=f" {t.tm_min} :")

        canvas.after(100,move)

    t=time.localtime()        
    min=t.tm_min
    min_angle=radians(min*6)
    x=400+175*sin(min_angle)
    y=400-175*cos(min_angle)
    canvas.coords(minutes,400,400,x,y)
    move()
    
def mov_hour():
    def move():
        t=time.localtime()
        angle=radians((t.tm_hour)*30+(t.tm_min)*0.5)
        x1=400+125*sin(angle)
        y1=400-125*cos(angle)
        canvas.coords(hours,400,400,x1,y1)

        if t.tm_hour==0:
            canvas.itemconfig(am_pm,text="AM")
        elif 0<t.tm_hour<=12:
            if t.tm_hour==12:
                canvas.itemconfig(am_pm,text="PM")
            else:
                canvas.itemconfig(am_pm,text="AM")
        else:
            canvas.itemconfig(am_pm,text="PM")
    


        if t.tm_hour==0:
            canvas.itemconfig(show_hour,text=f"12 :")
        elif 0<t.tm_hour<=12:
            if t.tm_hour<10:
                canvas.itemconfig(show_hour,text=f"0{t.tm_hour} :")
            else:
                canvas.itemconfig(show_hour,text=f"{t.tm_hour} :")
        else:
            if (t.tm_hour-12)<10:
                canvas.itemconfig(show_hour,text=f"0{t.tm_hour-12} :")
            else:
                canvas.itemconfig(show_hour,text=f"{t.tm_hour-12} :")
        
        
        canvas.after(100,move)

    t=time.localtime()
    if t.tm_hour==0:
        hour=12
    elif 0<t.tm_hour<=12:
        hour=t.tm_hour
    else:
        hour=(t.tm_hour)-12
    
    hour_angle=radians(hour*30+(t.tm_min)*0.5)
    x=400+125*sin(hour_angle)
    y=400-125*cos(hour_angle)
    canvas.coords(hours,400,400,x,y)
    move()



root=Tk()
root.title("Clock")
canvas=Canvas(root,height=800,width=800,bg="Black")
canvas.pack(expand=True)
canvas.create_oval(60,80,740,740,fill="#bd9663",outline="#42220B",width=20)

box=canvas.create_oval(400,450,650,550,width=3,fill="#8c5d3b")
show_hour=canvas.create_text(450,500,text="H",font=("Helvetica",20),fill="black")
show_min=canvas.create_text(500,500,text="M",font=("Helvetica",20),fill="Black")
show_sec=canvas.create_text(550,500,text="S",font=("Helvetica",20),fill="black")
am_pm=canvas.create_text(600,500,text="am_pm",font=("Helvetica",20),fill="black")


seconds=canvas.create_line(400,400,400,250,width=1)
minutes=canvas.create_line(400,400,400,200,width=3)
hours=canvas.create_line(400,400,400,275,width=5)

one=canvas.create_text(550,150,text="1",font=("Georgia",40))
two=canvas.create_text(650,250,text="2",font=("Georgia",40))
three=canvas.create_text(700,400,text="3",font=("Georgia",40))
four=canvas.create_text(650,550,text="4",font=("Georgia",40))
five=canvas.create_text(550,650,text="5",font=("Georgia",40))
six=canvas.create_text(400,700,text="6",font=("Georgia",40))
seven=canvas.create_text(250,650,text="7",font=("Georgia",40))
eight=canvas.create_text(150,550,text="8",font=("Georgia",40))
nine=canvas.create_text(100,400,text="9",font=("Georgia",40))
ten=canvas.create_text(150,250,text="10",font=("Georgia",40))
eleven=canvas.create_text(250,150,text="11",font=("Georgia",40))
twelve=canvas.create_text(400,100,text="12",font=("Georgia",40))

canvas.create_oval(390,390,410,410,fill="Black")

mov_sec()
mov_min()
mov_hour()

root.mainloop()


