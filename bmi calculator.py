from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

window=Tk()
window.title('BMI Calculator')
icon_image=PhotoImage(file='image/icon.png')
window.iconphoto(False,icon_image)
window.geometry('470x580+10+10')
window.resizable(False,False)
window.configure(bg='lightgreen')


#### top ###
top=PhotoImage(file='image/top.png')
Label(window,image=top,bg='lightgreen').place(x=-10,y=-10)


###  Bottom Box ###
Label(window,bg='lightblue',width=72,height=18).pack(side=BOTTOM)

#### two box ###
box=PhotoImage(file='image/box.png')
box1=Label(window,image=box,bg='lightgreen')
box1.place(x=20,y=100)

box2=Label(window,image=box,bg='lightgreen')
box2.place(x=240,y=100)

### scale ##

scale=PhotoImage(file='image/scale.png')
Label(window,image=scale,bg='lightblue').place(x=15,y=310)

##### Height & weight Label ####
height=Label(window,text='Height(cm)',font='arial 13',bg='#fff',fg='grey')
height.place(x=95,y=120)

weight=Label(window,text='Weight(kg)',font='arial 13',bg='#fff',fg='grey')
weight.place(x=315,y=120)

##### get slider 1 valu ###

def get_valu():
    return '{: .2f}'.format(current_valu.get())
def slider_change(e):
    Height.set(get_valu())
    size=int(float(get_valu()))
    man_image=Image.open('image/standingman.png')
    resize_image=man_image.resize((100,10+size))
    photo=ImageTk.PhotoImage(resize_image)
    second_image.config(image=photo)
    second_image.place(x=50,y=550-size)
    second_image.image=photo

##### get slider 1 valu ###
def get_value2():
    return '{: .2f}'.format(current_valu2.get())
def slider_change2(e):
    Weight.set(get_value2())


def BMI():
    try:
        h=float(Height.get())
        w=float(Weight.get())
        h_to_m=h/100
        bmi=round(w/(h_to_m**2),1)
        main_label.config(text=bmi)
        if bmi==0:
            label2.config(text='')
            label3.config(text='')
        elif bmi<18.5 :
            label2.config(text='Underweight')
            label3.config(text='your weight is too low eat healthy food \nand do exercise regularly ')
        elif 18.5<bmi and bmi<24.9:
            label2.config(text='Normal weight')
            label3.config(text="Your weight is parfect never\n eat extra food ")
        elif bmi>25 and bmi<29.9:
            label2.config(text='Over weight')
            label3.config(text='Your weight is high maintain food \nand exercise regular')
        elif bmi>30:
            label2.config(text='Obesity')
            label3.config(text='Your weight is too high.\nConsult a specialist doctor and \nfollow his instructions')


    except:
        main_label.config(text='0')
        label2.config(text='')
        label3.config(text='')


###### slider 1  ######

current_valu=DoubleVar()
current_valu2=DoubleVar()

scale_style=ttk.Style()
scale_style.configure("TScale",background='#fff')


slider1=ttk.Scale(window,from_=0,to=240,orient='horizontal',style="TScale",
                  variable=current_valu,command=slider_change)
slider1.place(x=80,y=250)

###### slider 2 ######
slider2=ttk.Scale(window,from_=0,to=200,orient='horizontal',style="TScale",
                  variable=current_valu2,command=slider_change2)
slider2.place(x=300,y=250)

###### entry ####

Weight=StringVar()
Height=StringVar()

height_entry=Entry(window,textvariable=Height,width=5,bg='#fff',fg='#000',bd=0,
                   font='arial 50',justify=CENTER)
height_entry.place(x=35,y=160)
Height.set(get_valu())

weight_entry=Entry(window,textvariable=Weight,width=5,bg='#fff',fg='#000',bd=0,
                   font='arial 50',justify=CENTER)
weight_entry.place(x=255,y=160)
Weight.set(get_value2())

#### second image ###

second_image=Label(window,bg='lightblue')
second_image.place(x=70,y=530)

###### Button #######
Button(window,text='View Result',width=15,height=2,bg='#1f6e68',fg='white',command=BMI).place(x=280,y=340)

###### display label ######
main_label=Label(window,font='arial 50 bold',bg='lightblue',fg='Red')
main_label.place(x=120,y=320)

label2=Label(window,font='arial 20 bold',bg='lightblue',fg='#3a3b3a')
label2.place(x=270,y=400)

label3=Label(window,font='arial 10 bold',bg='lightblue',fg='#3a3b3a')
label3.place(x=140,y=480)






window.mainloop()
