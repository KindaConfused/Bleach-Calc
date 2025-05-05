from tkinter import *

ounces = 0.0

def display_oz():
    global ounces
    ounce_label.config(text=f"Bleach oz: {ounces}")


def sphere():
    global ounces
    
    try:
        height = int(heightC_entry.get())
        diameter = int(diameter_entry.get())
    except:
        pass
    
    radius = diameter/2
    
    gallons = round( 3.14159*radius**2*height/231, 2 )
    gallons = gallons* .80
    
    ounces = round( 2*gallons/150, 2 )
    display_oz()

def rect():
    global ounces
    
    try:
        width = int(width_entry.get())
        height = int(heightR_entry.get())
        depth = int(length_entry.get())
    except:
        pass
    
    area = width*height*depth
    
    gallons = round( area*0.00433, 2 )
    gallons = gallons* .80
    
    ounces = round( 2*gallons/150, 2 )
    display_oz()

mode = 'c'
def R_Buttons():
    global mode
    mode = 'r' if mode == 'c' else 'c'
    
    if mode == 'r':
        button_c.config(state=DISABLED)
    
        labelR1.grid(row=0,column=0)
        width_entry.grid(row=1,column=0)
    
        labelR2.grid(row=0,column=1)
        heightR_entry.grid(row=1,column=1)
    
        labelR3.grid(row=0,column=2)
        length_entry.grid(row=1,column=2)
    
        button_submit_r.grid(row=2,column=1)
    else:
        button_c.config(state=ACTIVE)
    
        labelR1.grid_forget()
        width_entry.grid_forget()
    
        labelR2.grid_forget()
        heightR_entry.grid_forget()
    
        labelR3.grid_forget()
        length_entry.grid_forget()
    
        button_submit_r.grid_forget()

def C_Buttons():
    global mode
    mode = 'r' if mode == 'c' else 'c'
    
    if mode == 'c':
        button_r.config(state=DISABLED)
    
        labelC1.grid(row=0,column=0)
        diameter_entry.grid(row=1,column=0)
    
        labelC2.grid(row=0,column=1)
        heightC_entry.grid(row=1,column=1)

        button_submit_c.pack()
    else:
        button_r.config(state=ACTIVE)
    
        labelC1.grid_forget()
        diameter_entry.grid_forget()
    
        labelC2.grid_forget()
        heightC_entry.grid_forget()

        button_submit_c.pack_forget()


window = Tk()
window.geometry("400x230")
window.config(bg='#f0fdff')
window.title("Bleach per Inch calc")

#Window widgets
ounce_label = Label(window, text=f"Bleach oz: 0.0", font=("", 30, "bold"), relief=RAISED, border=4, bg="#e4fcff", width=13)
ounce_label.pack()

Label(window,bg="#e4fcff",relief=RAISED,border=2,text="Choose a Shape!\nRectangle or Cylinder:",font=("",10,"bold")).pack()

frame1 = Frame(window)
frame1.pack()
frame1.config(bg='#f0fdff')

button_r = Button(frame1,width=9,bg="#e0f9f5",relief=SUNKEN,border=3,text="Rectangle",fg="#03cae1",font=("",10,"bold"),command=R_Buttons)
button_r.grid(row=0,column=0)
button_c = Button(frame1,width=9,bg="#e0f9f5",relief=SUNKEN,border=3,text="Cylinder",fg="#03cae1",font=("",10,"bold"),command=C_Buttons)
button_c.grid(row=0,column=1)

frame2 = Frame(window)
frame2.pack()
frame2.config(bg='#f0fdff')

#Rectangle Buttons/Labels:
labelR1 = Label(frame2,bg="#e4fcff",relief=RAISED,border=2,text="Width:",width=9,font=("",10,"bold"))
width_entry = Entry(frame2,width=9,bg="#e7f3f5",relief=SUNKEN,border=2,font=("",10,"bold"))

labelR2 = Label(frame2,bg="#e4fcff",relief=RAISED,border=2,text="Height:",width=9,font=("",10,"bold"))
heightR_entry = Entry(frame2,width=9,bg="#e7f3f5",relief=SUNKEN,border=2,font=("",10,"bold"))

labelR3 = Label(frame2,bg="#e4fcff",relief=RAISED,border=2,text="Length:",width=9,font=("",10,"bold"))
length_entry = Entry(frame2,width=9,bg="#e7f3f5",relief=SUNKEN,border=2,font=("",10,"bold"))

button_submit_r = Button(frame2,width=9,bg="#e0f9f5",relief=SUNKEN,border=3,text="Sumbit",fg="#03cae1",font=("",11,"bold"),command=rect)


#Cylinder Buttons/Labels:
labelC1 = Label(frame2,bg="#e4fcff",relief=RAISED,border=2,text="Diameter:",width=9,font=("",10,"bold"),padx=1)
diameter_entry = Entry(frame2,width=9,bg="#e7f3f5",relief=SUNKEN,border=2,font=("",10,"bold"))

labelC2 = Label(frame2,bg="#e4fcff",relief=RAISED,border=2,text="Height:",width=9,font=("",10,"bold"))
heightC_entry = Entry(frame2,width=9,bg="#e7f3f5",relief=SUNKEN,border=2,font=("",10,"bold"))

button_submit_c = Button(window,width=9,bg="#e0f9f5",relief=SUNKEN,border=3,text="Sumbit",fg="#03cae1",font=("",11,"bold"),command=sphere)

window.mainloop()