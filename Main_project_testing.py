from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter as s
from tkinter.ttk import Combobox

import pymysql
from PIL import ImageTk, Image
import time as t
import calendar
from datetime import datetime
import pymysql as m

# Window
window = Tk()
window.geometry("1500x1500")
window.title("TICKET HUB")
window.config(bg="#94DEA5")


# Functions
def home_to_sign():
    home_page.pack_forget()
    frame_of_sign.pack(fill=BOTH, expand=True)


def sing_to_home():
    frame_of_sign.pack_forget()
    home_page.pack(fill=BOTH, expand=TRUE)

def sing_to_login():
    frame_of_sign.pack_forget()
    frame_of_login.pack(fill=BOTH, expand=TRUE)

def login_to_home():
    frame_of_login.pack_forget()
    home_page.pack(fill=BOTH, expand=TRUE)

def sing_to_welcome():
    frame_of_login.pack_forget()
    frame_of_welcome.pack(fill=BOTH, expand=True)

def login_to_welcome():
    frame_of_sign.pack_forget()
    frame_of_welcome.pack(fill=BOTH, expand=True)

def welcome_to_home():
    frame_of_welcome.pack_forget()
    home_page.pack(fill=BOTH, expand=TRUE)


def welcome_to_airway():
    frame_of_welcome.pack_forget()
    frame_of_airway.pack(fill=BOTH, expand=True)


def airway_to_welcome():
    frame_of_airway.pack_forget()
    frame_of_welcome.pack(fill=BOTH, expand=TRUE)


def airway_to_berlin():
    frame_of_airway.pack_forget()
    frame_of_berlin.pack(fill=BOTH, expand=TRUE)


def berlin_to_airway():
    frame_of_berlin.pack_forget()
    frame_of_airway.pack(fill=BOTH, expand=True)


def airway_to_france():
    frame_of_airway.pack_forget()
    frame_of_france.pack(fill=BOTH, expand=TRUE)


def france_to_airway():
    frame_of_france.pack_forget()
    frame_of_airway.pack(fill=BOTH, expand=True)


def airway_to_qatar():
    frame_of_airway.pack_forget()
    frame_of_qatar.pack(fill=BOTH, expand=TRUE)


def qatar_to_airway():
    frame_of_qatar.pack_forget()
    frame_of_airway.pack(fill=BOTH, expand=True)


def airway_to_moscow_and_malyasia():
    frame_of_airway.pack_forget()
    frame_of_moscow_and_malaysia.pack(fill=BOTH, expand=TRUE)


def moscow_and_malaysia_to_airway():
    frame_of_moscow_and_malaysia.pack_forget()
    frame_of_airway.pack(fill=BOTH, expand=True)


def mo_mal_to_moscow():
    frame_of_moscow_and_malaysia.pack_forget()
    frame_of_moscow.pack(fill=BOTH, expand=TRUE)


def moscow_to_mo_mal():
    frame_of_moscow.pack_forget()
    frame_of_moscow_and_malaysia.pack(fill=BOTH, expand=True)


def mo_mal_to_malaysia():
    frame_of_moscow_and_malaysia.pack_forget()
    frame_of_malaysia.pack(fill=BOTH, expand=TRUE)


def malaysia_to_mo_mal():
    frame_of_malaysia.pack_forget()
    frame_of_moscow_and_malaysia.pack(fill=BOTH, expand=True)


def qatar_to_airway():
    frame_of_qatar.pack_forget()
    frame_of_airway.pack(fill=BOTH, expand=True)



def welcome_to_roadway():
    frame_of_welcome.pack_forget()
    frame_of_roadway.pack(fill=BOTH, expand=True)


def roadway_to_welcome():
    frame_of_roadway.pack_forget()
    frame_of_welcome.pack(fill=BOTH, expand=TRUE)


def roadway_to_amarnath():
    frame_of_roadway.pack_forget()
    frame_of_amarnath.pack(fill=BOTH, expand=True)


def amarnath_to_roadway():
    frame_of_amarnath.pack_forget()
    frame_of_roadway.pack(fill=BOTH, expand=TRUE)


def roadway_to_jammu():
    frame_of_roadway.pack_forget()
    frame_of_jammu.pack(fill=BOTH, expand=True)


def jammu_to_roadway():
    frame_of_jammu.pack_forget()
    frame_of_roadway.pack(fill=BOTH, expand=TRUE)


def roadway_to_darjelling():
    frame_of_roadway.pack_forget()
    frame_of_darjelling.pack(fill=BOTH, expand=True)


def darjelling_to_roadway():
    frame_of_darjelling.pack_forget()
    frame_of_roadway.pack(fill=BOTH, expand=TRUE)


def roadway_to_roadway2():
    frame_of_roadway.pack_forget()
    frame_of_roadway2.pack(fill=BOTH, expand=TRUE)


def roadway2_to_roadway():
    frame_of_roadway2.pack_forget()
    frame_of_roadway.pack(fill=BOTH, expand=True)


def roadway2_to_kerala():
    frame_of_roadway2.pack_forget()
    frame_of_kerala.pack(fill=BOTH, expand=TRUE)


def kerala_to_roadway2():
    frame_of_kerala.pack_forget()
    frame_of_roadway2.pack(fill=BOTH, expand=True)


def roadway2_to_ladak():
    frame_of_roadway2.pack_forget()
    frame_of_ladak.pack(fill=BOTH, expand=TRUE)


def ladak_to_roadway2():
    frame_of_ladak.pack_forget()
    frame_of_roadway2.pack(fill=BOTH, expand=True)


def welcome_to_railway():
    frame_of_welcome.pack_forget()
    frame_of_railway.pack(fill=BOTH, expand=True)


def railway_to_welcome():
    frame_of_railway.pack_forget()
    frame_of_welcome.pack(fill=BOTH, expand=TRUE)


def railway_to_russia():
    frame_of_railway.pack_forget()
    frame_of_russia.pack(fill=BOTH, expand=True)


def russia_to_railway():
    frame_of_russia.pack_forget()
    frame_of_railway.pack(fill=BOTH, expand=TRUE)


def railway_to_tokyo():
    frame_of_railway.pack_forget()
    frame_of_tokyo.pack(fill=BOTH, expand=True)


def tokyo_to_railway():
    frame_of_tokyo.pack_forget()
    frame_of_railway.pack(fill=BOTH, expand=TRUE)


def railway_to_swizerland():
    frame_of_railway.pack_forget()
    frame_of_swizerland.pack(fill=BOTH, expand=True)


def swizerland_to_railway():
    frame_of_swizerland.pack_forget()
    frame_of_railway.pack(fill=BOTH, expand=TRUE)


def railway_to_railway2():
    frame_of_railway.pack_forget()
    frame_of_railway2.pack(fill=BOTH, expand=TRUE)


def railway2_to_railway():
    frame_of_railway2.pack_forget()
    frame_of_railway.pack(fill=BOTH, expand=True)


def railway2_to_barcelona():
    frame_of_railway2.pack_forget()
    frame_of_barcelona.pack(fill=BOTH, expand=TRUE)


def barcelona_to_railway2():
    frame_of_barcelona.pack_forget()
    frame_of_railway2.pack(fill=BOTH, expand=True)


def railway2_to_portugal():
    frame_of_railway2.pack_forget()
    frame_of_portugal.pack(fill=BOTH, expand=TRUE)


def portugal_to_railway2():
    frame_of_portugal.pack_forget()
    frame_of_railway2.pack(fill=BOTH, expand=True)


def railway2_to_england():
    frame_of_railway2.pack_forget()
    frame_of_england.pack(fill=BOTH, expand=TRUE)


def england_to_railway2():
    frame_of_england.pack_forget()
    frame_of_railway2.pack(fill=BOTH, expand=True)


def back_to_airway():
    booking_frame.pack_forget()
    frame_of_airway.pack(fill=BOTH, expand=True)


def back_to_roadway():
    booking_frame.pack_forget()
    frame_of_roadway.pack(fill=BOTH, expand=True)


def back_to_railway():
    booking_frame.pack_forget()
    frame_of_railway.pack(fill=BOTH, expand=True)


def berlin_to_book():
    frame_of_berlin.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def france_to_book():
    frame_of_france.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def qatar_to_book():
    frame_of_qatar.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def moscow_to_book():
    frame_of_moscow.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def malaysia_to_book():
    frame_of_malaysia.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def amarnath_to_book():
    frame_of_amarnath.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def jammu_to_book():
    frame_of_jammu.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def darjelling_to_book():
    frame_of_darjelling.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def leh_ladakh_to_book():
    frame_of_ladak.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def kerala_to_book():
    frame_of_kerala.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def russia_to_book():
    frame_of_russia.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def tokyo_to_book():
    frame_of_tokyo.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def swizerland_to_book():
    frame_of_swizerland.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def barcelona_to_book():
    frame_of_barcelona.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def portugal_to_book():
    frame_of_portugal.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def england_to_book():
    frame_of_england.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def book_to_payment():
    booking_frame.pack_forget()
    payment_frame.pack(fill=BOTH, expand=True)


def payment_to_book():
    payment_frame.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)


def payment_to_welcome():
    booking_frame.pack_forget()
    frame_of_welcome.pack(fill=BOTH, expand=True)


def payment_to_debit():
    payment_frame.pack_forget()
    debit_frame.pack(fill=BOTH, expand=True)


def payment_to_upi():
    payment_frame.pack_forget()
    upi_frame.pack(fill=BOTH, expand=True)


def payment_to_net():
    payment_frame.pack_forget()
    net_frame.pack(fill=BOTH, expand=True)


def debit_to_last():
    debit_frame.pack_forget()
    last_frame.pack(fill=BOTH, expand=True)


def upi_to_last():
    upi_frame.pack_forget()
    last_frame.pack(fill=BOTH, expand=True)


def net_to_last():
    net_frame.pack_forget()
    last_frame.pack(fill=BOTH, expand=True)


# Main Page Start------------------------------------------------------------------------------------------------------------
# Frame page
home_page = Frame(window, bg="#023D54")

image_of_homepage = "D:\\Pics\\Frontpage1.png"
image = Image.open(image_of_homepage)
photo = ImageTk.PhotoImage(image)
label = Label(home_page, image=photo)
label.image = photo
label.place(x=150, y=40)

login = Button(home_page, text="ENTER", font="Timesnewroman", width=8, height=2,command=lambda: [home_to_sign(), sing_to_home])
login.place(x=670, y=638)
home_page.pack(fill=BOTH, expand=True)

# Main page Ends----------------------------------------------------------------------------------------------------------------

# Login Page Starts---------------------------------------------------------------------------------------------------------------

frame_of_sign = Frame(window, bg="#023D54")

lo = Label(frame_of_sign, text="LOGIN IN", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lo.place(x=600, y=100)

l1 = Label(frame_of_sign, text="USER NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=450, y=195)


user_name_login = Entry(frame_of_sign, width=20, font=("Comic Sans MS", 20))
user_name_login.insert(0,"Enter Your Name")
user_name_login.place(x=650, y=200)

l2 = Label(frame_of_sign, text="PASSWORD", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=300)

user_password_login= Entry(frame_of_sign, show="*",font=("Comic Sans MS", 20))
user_password_login.place(x=650, y=305)


def submit():
        if user_name_login.get() == '' or user_password_login.get() == '':
            messagebox.showinfo("!", "Please fill the details")
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password="K@rthi16", database="python")
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error', 'Connection is not estabished try again')
                return

            query = 'select * from sign_in where name_1=%s and password_1=%s'
            mycursor.execute(query, (user_name_login.get(), user_password_login.get()))
            row = mycursor.fetchone()

            if row == None:
                messagebox.showerror('Error', 'Invalid username or Password')

            else:
                messagebox.showinfo('Congrats', 'Login is Successful')
                clear()
                frame_of_sign.pack_forget()
                frame_of_welcome.pack(fill=BOTH, expand=True)

def clear():
    user_name_login.delete(0,END)
    user_password_login.delete(0,END)

b2 = Button(frame_of_sign, text="LOGIN IN ", font="Timesnewroman", width=8, height=2,command=lambda:[submit()])
b2.place(x=650, y=370)

b3 = Button(frame_of_sign, text="SIGN IN ", font="Timesnewroman", width=8, height=2, command=lambda:[sing_to_login()])
b3.place(x=1200, y=600)

b3 = Button(frame_of_sign, text="BACK", font="Timesnewroman", width=8, height=2, command=lambda: [sing_to_home()])
b3.place(x=50, y=600)

# Login page Ends---------------------------------------------------------------------------------------------------------------------

# SignIn page Start-------------------------------------------------------------------------------------------------------------------

frame_of_login = Frame(window, bg="#023D54")

lo = Label(frame_of_login, text="SIGN IN", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lo.place(x=600, y=100)

name_1 = Label(frame_of_login, text="ENTER YOUR NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
name_1.place(x=370, y=175)

user_name = Entry(frame_of_login, width=20, font=("Comic Sans MS", 20))
user_name.place(x=750, y=180)

name_2 = Label(frame_of_login, text="CREATE YOUR PASSWORD", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
name_2.place(x=370, y=275)

pass_word = Entry(frame_of_login, width=20, font=("Comic Sans MS", 20))
pass_word.place(x=750, y=280)

name_3 = Label(frame_of_login, text="ENTER YOUR PHONE NO", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
name_3.place(x=370, y=375)

phone_no= Entry(frame_of_login, width=20, font=("Comic Sans MS", 20))
phone_no.place(x=750, y=380)


def submit_1():
    name_1= user_name.get()
    password_1 = pass_word.get()
    phone_1 =phone_no.get()
    if name_1=="" or password_1=="" or phone_1=="":
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        clear_1()
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into sign_in values('" + name_1 + "','" + password_1 + "','" + phone_1 + "')")
        db.commit()
        frame_of_login.pack_forget()
        frame_of_welcome.pack(fill=BOTH, expand=True)

def clear_1():
    user_name.delete(0,END)
    pass_word.delete(0,END)
    phone_no.delete(0, END)

b3 = Button(frame_of_login, text="BACK", font="Timesnewroman", width=8, height=2, command=lambda: [login_to_home()])
b3.place(x=50, y=600)

b1 = Button(frame_of_login, text="SIGN IN", font="Timesnewroman", width=8, height=2,command=lambda: [submit_1()])
b1.place(x=650, y=498)

# SignIn page Ends--------------------------------------------------------------------------------------------------------------------------

# Welcome page Starts----------------------------------------------------------------------------------------------------------------------

frame_of_welcome = Frame(window, bg="#023D54")

lo = s.Label(frame_of_welcome, text="WELCOME TO OUR APPLICATION", bg="#023D54", fg="white", font=("Comic Sans MS", 40))
lo.place(x=290, y=50)
image_path = "D:\\Pics\\Travelling Modes 2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_welcome, image=photo)
label.image = photo
label.place(x=100, y=200)
b1 = s.Button(frame_of_welcome, text="RAILWAYS", font="Timesnewroman", width=9, height=2,
              command=lambda: [welcome_to_railway()])
b1.place(x=1100, y=530)
image_path = "D:\\Pics\\Travelling Modes 1.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_welcome, image=photo)
label.image = photo
label.place(x=550, y=200)
b2 = s.Button(frame_of_welcome, text="AIRWAYS", font="Timesnewroman", width=9, height=2,
              command=lambda: [welcome_to_airway()])
b2.place(x=209, y=530)
image_path = "D:\\Pics\\Travelling Modes 3.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_welcome, image=photo)
label.image = photo
label.place(x=980, y=200)
b3 = s.Button(frame_of_welcome, text="ROADWAYS", font="Timesnewroman", width=10, height=2,
              command=lambda: [welcome_to_roadway()])
b3.place(x=670, y=530)

welcome_to_home_b = Button(frame_of_welcome, text="BACK", font="Timesnewroman", width=8, height=2,
                           command=lambda: [welcome_to_home()])
welcome_to_home_b.place(x=50, y=600)

# Welcome Ends--------------------------------------------------------------------------------------------------------------------------

# Airway Starts--------------------------------------------------------------------------------------------------------------------------

frame_of_airway = Frame(window, bg="#023D54")

lo = s.Label(frame_of_airway, text="WELCOME TO OUR AIRLINE BOOKING SECTION", bg="#023D54", fg="white",
             font=("Comic Sans MS", 25))
lo.place(x=290, y=50)

image_path = "D:\\Pics\\berlin2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_airway, image=photo)
label.image = photo
label.place(x=100, y=200)
b1 = s.Button(frame_of_airway, text="BERLIN", font="Timesnewromen", width=9, height=2,
              command=lambda: [airway_to_berlin()])
b1.place(x=209, y=530)

image_path = "D:\\Pics\\france2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_airway, image=photo)
label.image = photo
label.place(x=550, y=200)
b2 = s.Button(frame_of_airway, text="FRANCE", font="Timesnewromen", width=9, height=2,
              command=lambda: [airway_to_france()])
b2.place(x=665, y=530)

image_path = "D:\\Pics\\qatar2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_airway, image=photo)
label.image = photo
label.place(x=980, y=200)
b3 = s.Button(frame_of_airway, text="QATAR", font="Timesnewromen", width=10, height=2,
              command=lambda: [airway_to_qatar()])
b3.place(x=1110, y=530)

b4 = s.Button(frame_of_airway, text="NEXT", font="Timesnewromen", width=8, height=2,
              command=lambda: [airway_to_moscow_and_malyasia()])
b4.place(x=1250, y=600)

airway_to_home = Button(frame_of_airway, text="BACK", font="Timesnewroman", width=8, height=2,
                        command=lambda: [airway_to_welcome()])
airway_to_home.place(x=50, y=600)

# Airway Ends------------------------------------------------------------------------------------------------------------------------------------

# Airway2 Starts-------------------------------------------------------------------------------------------------------------------------------------

frame_of_moscow_and_malaysia = Frame(window, bg="#023D54")

image_path = "D:\\Pics\\moscow2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_moscow_and_malaysia, image=photo)
label.image = photo
label.place(x=300, y=200)
b1 = s.Button(frame_of_moscow_and_malaysia, text="MOSCOW", font="Timesnewromen", width=10, height=2,
              command=lambda: [mo_mal_to_moscow()])
b1.place(x=410, y=530)

image_path = "D:\\Pics\\Malaysia2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_moscow_and_malaysia, image=photo)
label.image = photo
label.place(x=900, y=200)
b2 = s.Button(frame_of_moscow_and_malaysia, text="MALAYSIA", font="Timesnewromen", width=10, height=2,
              command=lambda: [mo_mal_to_malaysia()])
b2.place(x=1010, y=530)

qatar_to_airway_button = Button(frame_of_moscow_and_malaysia, text="BACK", font="Timesnewroman", width=8, height=2,
                                command=lambda: [moscow_and_malaysia_to_airway()])
qatar_to_airway_button.place(x=50, y=600)

# Airway2 Ends----------------------------------------------------------------------------------------------------------------------------------------

# Berlin Starts---------------------------------------------------------------------------------------------------------------------------

frame_of_berlin = Frame(window, bg="#023D54")

lo = s.Label(frame_of_berlin, text="BERLIN:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\berlin 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_berlin, image=photo)
label.image = photo
label.place(x=100, y=100)
image_path = "D:\\bg pics\\berlin 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_berlin, image=photo)
label.image = photo
label.place(x=550, y=100)
image_path = "D:\\bg pics\\berlin 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_berlin, image=photo)
label.image = photo
label.place(x=980, y=100)
l2 = s.Label(frame_of_berlin, text='''The Travel App Booking is a comprehensive solution designed to make travel planning seamless, efficient, and enjoyable.\nWith real-time availability, secure payments, and personalised recommendations, FlyBook ensures that your travel experience is hassle-free from start to finish.
\nKey Features:
\nReal-Time Availability & Pricing\n24/7 Customer Support\nBooking Management\nCost Savings\nPersonalisation\nSecurity''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)
b2 = s.Button(frame_of_berlin, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [berlin_to_book()])
b2.place(x=1250, y=600)

berlin_to_airway_button = Button(frame_of_berlin, text="BACK", font="Timesnewroman", width=8, height=2,
                                 command=lambda: [berlin_to_airway()])
berlin_to_airway_button.place(x=50, y=600)

# Berlin Ends----------------------------------------------------------------------------------------------------------------------------

# France Starts--------------------------------------------------------------------------------------------------------------------------

frame_of_france = Frame(window, bg="#023D54")

lo = s.Label(frame_of_france, text="FRANCE", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\france 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_france, image=photo)
label.image = photo
label.place(x=100, y=100)
image_path = "D:\\bg pics\\france 2.jpeg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_france, image=photo)
label.image = photo
label.place(x=550, y=100)
image_path = "D:\\bg pics\\france 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_france, image=photo)
label.image = photo
label.place(x=980, y=100)
l2 = s.Label(frame_of_france, text='''The Travel App Booking is a comprehensive solution designed to make travel planning seamless, efficient, and enjoyable.\nWith real-time availability, secure payments, and personalised recommendations, FlyBook ensures that your travel experience is hassle-free from start to finish.
\nKey Features:
\nReal-Time Availability & Pricing\n24/7 Customer Support\nBooking Management\nCost Savings\nPersonalisation\nSecurity''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)
b2 = s.Button(frame_of_france, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [france_to_book()])
b2.place(x=1250, y=600)

france_to_airway_button = Button(frame_of_france, text="BACK", font="Timesnewroman", width=8, height=2,
                                 command=lambda: [france_to_airway()])
france_to_airway_button.place(x=50, y=600)

# France Ends-----------------------------------------------------------------------------------------------------------------------------

# Qatar Starts--------------------------------------------------------------------------------------------------------------------------------------

frame_of_qatar = Frame(window, bg="#023D54")

lo = s.Label(frame_of_qatar, text="QATAR:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\qatar 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_qatar, image=photo)
label.image = photo
label.place(x=100, y=100)
image_path = "D:\\bg pics\\qatar 2.jpeg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_qatar, image=photo)
label.image = photo
label.place(x=550, y=100)
image_path = "D:\\bg pics\\qatar 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_qatar, image=photo)
label.image = photo
label.place(x=980, y=100)
l2 = s.Label(frame_of_qatar, text='''The Travel App Booking is a comprehensive solution designed to make travel planning seamless, efficient, and enjoyable.\nWith real-time availability, secure payments, and personalised recommendations, FlyBook ensures that your travel experience is hassle-free from start to finish.
   \nKey Features:
   \nReal-Time Availability & Pricing\n24/7 Customer Support\nBooking Management\nCost Savings\nPersonalisation\nSecurity''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)
b2 = s.Button(frame_of_qatar, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [qatar_to_book()])
b2.place(x=1250, y=600)

qatar_to_airway_button = Button(frame_of_qatar, text="BACK", font="Timesnewroman", width=8, height=2,
                                command=lambda: [qatar_to_airway()])
qatar_to_airway_button.place(x=50, y=600)

# Qatar Ends---------------------------------------------------------------------------------------------------------------------------------------

# Moscow Starts-------------------------------------------------------------------------------------------------------------------------------------

frame_of_moscow = Frame(window, bg="#023D54")

lo = s.Label(frame_of_moscow, text="MOSCOW:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\moscow 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_moscow, image=photo)
label.image = photo
label.place(x=100, y=100)
image_path = "D:\\bg pics\\moscow 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_moscow, image=photo)
label.image = photo
label.place(x=550, y=100)
image_path = "D:\\bg pics\\moscow 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_moscow, image=photo)
label.image = photo
label.place(x=980, y=100)
l2 = s.Label(frame_of_moscow, text='''The Travel App Booking is a comprehensive solution designed to make travel planning seamless, efficient, and enjoyable.\nWith real-time availability, secure payments, and personalised recommendations, FlyBook ensures that your travel experience is hassle-free from start to finish.
   \nKey Features:
   \nReal-Time Availability & Pricing\n24/7 Customer Support\nBooking Management\nCost Savings\nPersonalisation\nSecurity''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)

b2 = s.Button(frame_of_moscow, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [moscow_to_book()])
b2.place(x=1250, y=600)

moscow_to_airway_button = Button(frame_of_moscow, text="BACK", font="Timesnewroman", width=8, height=2,
                                 command=lambda: [moscow_to_mo_mal()])
moscow_to_airway_button.place(x=50, y=600)

# Moscow Ends----------------------------------------------------------------------------------------------------------------------------------------

# Malyasia Starts-------------------------------------------------------------------------------------------------------------------------------------

frame_of_malaysia = Frame(window, bg="#023D54")

lo = s.Label(frame_of_malaysia, text="MALAYSIA:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\malaysia 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_malaysia, image=photo)
label.image = photo
label.place(x=100, y=100)
image_path = "D:\\bg pics\\malaysia 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_malaysia, image=photo)
label.image = photo
label.place(x=550, y=100)
image_path = "D:\\bg pics\\malaysia 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_malaysia, image=photo)
label.image = photo
label.place(x=980, y=100)
l2 = s.Label(frame_of_malaysia, text='''The Travel App Booking is a comprehensive solution designed to make travel planning seamless, efficient, and enjoyable.\nWith real-time availability, secure payments, and personalised recommendations, FlyBook ensures that your travel experience is hassle-free from start to finish.
   \nKey Features:
   \nReal-Time Availability & Pricing\n24/7 Customer Support\nBooking Management\nCost Savings\nPersonalisation\nSecurity''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)
b2 = s.Button(frame_of_malaysia, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [malaysia_to_book()])
b2.place(x=1250, y=600)

malaysia_to_airway_button = Button(frame_of_malaysia, text="BACK", font="Timesnewroman", width=8, height=2,
                                   command=lambda: [malaysia_to_mo_mal()])
malaysia_to_airway_button.place(x=50, y=600)

# Malaysia Ends---------------------------------------------------------------------------------------------------------------------------------------

# Roadway Starts--------------------------------------------------------------------------------------------------------------------------------------

frame_of_roadway = Frame(window, bg="#023D54")

lo = s.Label(frame_of_roadway, text="WELCOME TO OUR ROADWAYS BOOKING SECTION", bg="#023D54", fg="white",
             font=("Comic Sans MS", 25))
lo.place(x=290, y=50)
image_path = "D:\\Pics\\Amarnath.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_roadway, image=photo)
label.image = photo
label.place(x=100, y=200)
b1 = s.Button(frame_of_roadway, text="AMARNATH", font="Timesnewromen", width=10, height=2,
              command=lambda: [roadway_to_amarnath()])
b1.place(x=209, y=530)

image_path = "D:\\Pics\\Jammu.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_roadway, image=photo)
label.image = photo
label.place(x=550, y=200)
b2 = s.Button(frame_of_roadway, text="JAMMU & KASHMIR", font="Timesnewromen", width=17, height=2,
              command=lambda: [roadway_to_jammu()])
b2.place(x=625, y=530)

image_path = "D:\\Pics\\Darjeeling.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_roadway, image=photo)
label.image = photo
label.place(x=980, y=200)
b3 = s.Button(frame_of_roadway, text="DARJEELING", font="Timesnewromen", width=11, height=2,
              command=lambda: [roadway_to_darjelling()])
b3.place(x=1080, y=530)
b4 = s.Button(frame_of_roadway, text="NEXT", font="Timesnewromen", width=8, height=2,
              command=lambda: [roadway_to_roadway2()])
b4.place(x=1250, y=600)

roadway_to_home = Button(frame_of_roadway, text="BACK", font="Timesnewroman", width=8, height=2,
                         command=lambda: [roadway_to_welcome()])
roadway_to_home.place(x=50, y=600)

# Roadway Ends---------------------------------------------------------------------------------------------------------------------------------

# Roadway 2 Starts------------------------------------------------------------------------------------------------------------------------------

frame_of_roadway2 = Frame(window, bg="#023D54")

image_path = "D:\\Pics\\kerala.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_roadway2, image=photo)
label.image = photo
label.place(x=300, y=200)
b1 = s.Button(frame_of_roadway2, text="KERALA", font="Timesnewromen", width=10, height=2,
              command=lambda: [roadway2_to_kerala()])
b1.place(x=410, y=530)

image_path = "D:\\Pics\\Leh-Ladakh.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_roadway2, image=photo)
label.image = photo
label.place(x=900, y=200)
b2 = s.Button(frame_of_roadway2, text="LEH & LADAKH", font="Timesnewromen", width=15, height=2,
              command=lambda: [roadway2_to_ladak()])
b2.place(x=990, y=530)

roadway2_to_roadway1 = Button(frame_of_roadway2, text="BACK", font="Timesnewroman", width=8, height=2,
                              command=lambda: [roadway2_to_roadway()])
roadway2_to_roadway1.place(x=50, y=600)

# Roadway 2 Ends-----------------------------------------------------------------------------------------------------------------------------------

# Amarnath Starts----------------------------------------------------------------------------------------------------------------------------------

frame_of_amarnath = Frame(window, bg="#023D54")

lo = s.Label(frame_of_amarnath, text="AMARNATH:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\amarnath 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_amarnath, image=photo)
label.image = photo
label.place(x=100, y=100)

image_path = "D:\\bg pics\\amarnath 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_amarnath, image=photo)
label.image = photo
label.place(x=550, y=100)

image_path = "D:\\bg pics\\amarnath 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_amarnath, image=photo)
label.image = photo
label.place(x=980, y=100)

l2 = s.Label(frame_of_amarnath, text='''RoadWays is a comprehensive application designed to simplify road transport bookings, offering users the ability to plan trips, 
book bus tickets, and track routes with ease.Whether you are traveling across cities or within local areas, RoadWays ensures a smooth booking experience with 
multiple transport options available at your fingertips.
\nKey Features: \n1.Bus Ticket Booking\n2.Real-time Bus Tracking\n3.Discounts & Offers\n4.Reschedule\n5.Payment Flexibility''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)
b2 = s.Button(frame_of_amarnath, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [amarnath_to_book()])
b2.place(x=1250, y=600)

amarnath_to_roadway_button = Button(frame_of_amarnath, text="BACK", font="Timesnewroman", width=8, height=2,
                                    command=lambda: [amarnath_to_roadway()])
amarnath_to_roadway_button.place(x=50, y=600)

# Amarnath Ends---------------------------------------------------------------------------------------------------------------------------------------

# Jammukashmir Starts-------------------------------------------------------------------------------------------------------------------------------

frame_of_jammu = Frame(window, bg="#023D54")

lo = Label(frame_of_jammu, text="JAMMU & KASHMIR:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\jammu & kashmir 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = Label(frame_of_jammu, image=photo)
label.image = photo
label.place(x=100, y=100)
image_path = "D:\\bg pics\\jammu & kashmir 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = Label(frame_of_jammu, image=photo)
label.image = photo
label.place(x=550, y=100)
image_path = "D:\\bg pics\\jammu & kashmir 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = Label(frame_of_jammu, image=photo)
label.image = photo
label.place(x=980, y=100)
l2 = Label(frame_of_jammu, text='''RoadWays is a comprehensive application designed to simplify road transport bookings, offering users the ability to plan trips, 
book bus tickets, and track routes with ease.Whether you are traveling across cities or within local areas, RoadWays ensures a smooth booking experience with 
multiple transport options available at your fingertips.
\nKey Features: \n1.Bus Ticket Booking\n2.Real-time Bus Tracking\n3.Discounts & Offers\n4.Reschedule\n5.Payment Flexibility''',
           bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)
b2 = s.Button(frame_of_jammu, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [jammu_to_book()])

jammu_to_roadway_button = Button(frame_of_jammu, text="BACK", font="Timesnewroman", width=8, height=2,
                                 command=lambda: [jammu_to_roadway()])
jammu_to_roadway_button.place(x=50, y=600)

b2.place(x=1250, y=600)

# Jamukashimr Ends---------------------------------------------------------------------------------------------------------------------------------

# darjelling starts--------------------------------------------------------------------------------------------------------------------------------

frame_of_darjelling = Frame(window, bg="#023D54")

lo = s.Label(frame_of_darjelling, text="DARJEELING:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\darjeeling 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_darjelling, image=photo)
label.image = photo
label.place(x=100, y=100)

image_path = "D:\\bg pics\\darjeeling 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_darjelling, image=photo)
label.image = photo
label.place(x=550, y=100)

image_path = "D:\\bg pics\\darjeeling 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_darjelling, image=photo)
label.image = photo
label.place(x=980, y=100)

l2 = s.Label(frame_of_darjelling, text='''RoadWays is a comprehensive application designed to simplify road transport bookings, offering users the ability to plan trips, 
book bus tickets, and track routes with ease.Whether you are traveling across cities or within local areas, RoadWays ensures a smooth booking experience with 
multiple transport options available at your fingertips.
\nKey Features: \n1.Bus Ticket Booking\n2.Real-time Bus Tracking\n3.Discounts & Offers\n4.Reschedule\n5.Payment Flexibility''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)
b2 = s.Button(frame_of_darjelling, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [darjelling_to_book()])
b2.place(x=1250, y=600)

darjelling_to_roadway_button = Button(frame_of_darjelling, text="BACK", font="Timesnewroman", width=8, height=2,
                                      command=lambda: [darjelling_to_roadway()])
darjelling_to_roadway_button.place(x=50, y=600)

# darjelling stops---------------------------------------------------------------------------------------------------------------------------------

# Kerala Starts------------------------------------------------------------------------------------------------------------------------------------

frame_of_kerala = Frame(window, bg="#023D54")

lo = s.Label(frame_of_kerala, text="KERALA:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\kerala 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_kerala, image=photo)
label.image = photo
label.place(x=100, y=100)
image_path = "D:\\bg pics\\kerala 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_kerala, image=photo)
label.image = photo
label.place(x=550, y=100)
image_path = "D:\\bg pics\\kerala 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_kerala, image=photo)
label.image = photo
label.place(x=980, y=100)
l2 = s.Label(frame_of_kerala, text='''RoadWays is a comprehensive application designed to simplify road transport bookings, offering users the ability to plan trips, 
book bus tickets, and track routes with ease.Whether you are traveling across cities or within local areas, RoadWays ensures a smooth booking experience with 
multiple transport options available at your fingertips.
\nKey Features: \n1.Bus Ticket Booking\n2.Real-time Bus Tracking\n3.Discounts & Offers\n4.Reschedule\n5.Payment Flexibility''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)

b2 = s.Button(frame_of_kerala, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [kerala_to_book()])
b2.place(x=1250, y=600)

roadway2_to_kerala_button = Button(frame_of_kerala, text="BACK", font="Timesnewroman", width=8, height=2,
                                   command=lambda: [kerala_to_roadway2()])
roadway2_to_kerala_button.place(x=50, y=600)

# Kerala Ends--------------------------------------------------------------------------------------------------------------------------------------

# Ladakh Starts-------------------------------------------------------------------------------------------------------------------------------------

frame_of_ladak = Frame(window, bg="#023D54")

lo = s.Label(frame_of_ladak, text="LEH_LADAKH:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\leh & ladakh 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_ladak, image=photo)
label.image = photo
label.place(x=100, y=100)
image_path = "D:\\bg pics\\leh & ladakh 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_ladak, image=photo)
label.image = photo
label.place(x=550, y=100)
image_path = "D:\\bg pics\\leh & ladakh 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_ladak, image=photo)
label.image = photo
label.place(x=980, y=100)
l2 = s.Label(frame_of_ladak, text='''RoadWays is a comprehensive application designed to simplify road transport bookings, offering users the ability to plan trips, 
book bus tickets, and track routes with ease.Whether you are traveling across cities or within local areas, RoadWays ensures a smooth booking experience with 
multiple transport options available at your fingertips.
\nKey Features: \n1.Bus Ticket Booking\n2.Real-time Bus Tracking\n3.Discounts & Offers\n4.Reschedule\n5.Payment Flexibility''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)

b2 = s.Button(frame_of_ladak, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [leh_ladakh_to_book()])
b2.place(x=1250, y=600)

roadway2_to_ladak_button = Button(frame_of_ladak, text="BACK", font="Timesnewroman", width=8, height=2,
                                  command=lambda: [ladak_to_roadway2()])
roadway2_to_ladak_button.place(x=50, y=600)

# Ladak Ends---------------------------------------------------------------------------------------------------------------------------------------

# Railway Starts-------------------------------------------------------------------------------------------------------------------------------

frame_of_railway = Frame(window, bg="#023D54")

lo = s.Label(frame_of_railway, text="WELCOME TO OUR RAILWAYS BOOKING SECTION", bg="#023D54", fg="white",
             font=("Comic Sans MS", 25))
lo.place(x=290, y=50)
image_path = "D:\\Pics\\Russia.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway, image=photo)
label.image = photo
label.place(x=100, y=200)
b1 = s.Button(frame_of_railway, text="RUSSIA", font="Timesnewromen", width=10, height=2,
              command=lambda: [railway_to_russia()])
b1.place(x=209, y=530)

image_path = "D:\\Pics\\Tokyo.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway, image=photo)
label.image = photo
label.place(x=550, y=200)
b2 = s.Button(frame_of_railway, text="TOKYO", font="Timesnewromen", width=10, height=2,
              command=lambda: [railway_to_tokyo()])
b2.place(x=665, y=530)

image_path = "D:\\Pics\\Switzerland.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway, image=photo)
label.image = photo
label.place(x=980, y=200)
b3 = s.Button(frame_of_railway, text="SWITZERLAND", font="Timesnewromen", width=13, height=2,
              command=lambda: [railway_to_swizerland()])
b3.place(x=1080, y=530)

b4 = s.Button(frame_of_railway, text="NEXT", font="Timesnewromen", width=8, height=2,
              command=lambda: [railway_to_railway2()])
b4.place(x=1250, y=600)

b4 = s.Button(frame_of_railway, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [railway_to_welcome()])
b4.place(x=50, y=600)

# Railway Ends---------------------------------------------------------------------------------------------------------------------------------

# Railway2 Starts-------------------------------------------------------------------------------------------------------------------------------

frame_of_railway2 = Frame(window, bg="#023D54")

image_path = "D:\\Pics\\Barcelona.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway2, image=photo)
label.image = photo
label.place(x=100, y=200)
b1 = s.Button(frame_of_railway2, text="BARCELONA", font="Timesnewromen", width=12, height=2,
              command=lambda: [railway2_to_barcelona()])
b1.place(x=209, y=530)

image_path = "D:\\Pics\\Portugal.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway2, image=photo)
label.image = photo
label.place(x=550, y=200)
b2 = s.Button(frame_of_railway2, text="PORTUGAL", font="Timesnewromen", width=10, height=2,
              command=lambda: [railway2_to_portugal()])
b2.place(x=665, y=530)

image_path = "D:\\Pics\\England.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway2, image=photo)
label.image = photo
label.place(x=980, y=200)
b3 = s.Button(frame_of_railway2, text="ENGLAND", font="Timesnewromen", width=10, height=2,
              command=lambda: [railway2_to_england()])
b3.place(x=1080, y=530)

b4 = s.Button(frame_of_railway2, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [railway2_to_railway()])
b4.place(x=50, y=600)

# Railway2 Ends---------------------------------------------------------------------------------------------------------------------------------

# russia starts--------------------------------------------------------------------------------------------------------------------------------

frame_of_russia = Frame(window, bg="#023D54")

lo = s.Label(frame_of_russia, text="RUSSIA:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\russia 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_russia, image=photo)
label.image = photo
label.place(x=100, y=100)

image_path = "D:\\bg pics\\russia 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_russia, image=photo)
label.image = photo
label.place(x=550, y=100)
image_path = "D:\\bg pics\\russia 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_russia, image=photo)
label.image = photo
label.place(x=980, y=100)

l2 = s.Label(frame_of_russia, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features:
   \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)

b2 = s.Button(frame_of_russia, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [russia_to_book()])
b2.place(x=1250, y=600)

b4 = s.Button(frame_of_russia, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [russia_to_railway()])
b4.place(x=50, y=600)

# russia stops--------------------------------------------------------------------------------------------------------------------------------

# tokyo starts--------------------------------------------------------------------------------------------------------------------------------

frame_of_tokyo = Frame(window, bg="#023D54")

lo = s.Label(frame_of_tokyo, text="TOKYO:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\tokyo 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_tokyo, image=photo)
label.image = photo
label.place(x=100, y=100)

image_path = "D:\\bg pics\\tokyo 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_tokyo, image=photo)
label.image = photo
label.place(x=550, y=100)

image_path = "D:\\bg pics\\tokyo 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_tokyo, image=photo)
label.image = photo
label.place(x=980, y=100)

l2 = s.Label(frame_of_tokyo, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features:
   \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)
b2 = s.Button(frame_of_tokyo, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [tokyo_to_book()])
b2.place(x=1250, y=600)

b4 = s.Button(frame_of_tokyo, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [tokyo_to_railway()])
b4.place(x=50, y=600)

# tokyo stops--------------------------------------------------------------------------------------------------------------------------------

# swizerland starts----------------------------------------------------------------------------------------------------------------------------------

frame_of_swizerland = Frame(window, bg="#023D54")

lo = s.Label(frame_of_swizerland, text="SWIZERLAND:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)

image_path = "D:\\bg pics\\swizerland 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_swizerland, image=photo)
label.image = photo
label.place(x=100, y=100)

image_path = "D:\\bg pics\\swizerland 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_swizerland, image=photo)
label.image = photo
label.place(x=550, y=100)

image_path = "D:\\bg pics\\swizerland 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_swizerland, image=photo)
label.image = photo
label.place(x=980, y=100)
l2 = s.Label(frame_of_swizerland, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features:
   \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)

b2 = s.Button(frame_of_swizerland, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [swizerland_to_book()])
b2.place(x=1250, y=600)

b4 = s.Button(frame_of_swizerland, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [swizerland_to_railway()])
b4.place(x=50, y=600)

# swizerland stops-----------------------------------------------------------------------------------------------------------------------------------

# barcelona starts--------------------------------------------------------------------------------------------------------------------

frame_of_barcelona = Frame(window, bg="#023D54")

lo = s.Label(frame_of_barcelona, text="BARCELONA:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\barcelona 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_barcelona, image=photo)
label.image = photo
label.place(x=100, y=100)

image_path = "D:\\bg pics\\barcelona 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_barcelona, image=photo)
label.image = photo
label.place(x=550, y=100)

image_path = "D:\\bg pics\\barcelona 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_barcelona, image=photo)
label.image = photo
label.place(x=980, y=100)

l2 = s.Label(frame_of_barcelona, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features:
   \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)
b2 = s.Button(frame_of_barcelona, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [barcelona_to_book()])
b2.place(x=1250, y=600)

b4 = s.Button(frame_of_barcelona, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [barcelona_to_railway2()])
b4.place(x=50, y=600)

# portugal starts--------------------------------------------------------------------------------------------------------------------------

frame_of_portugal = Frame(window, bg="#023D54")

lo = s.Label(frame_of_portugal, text="PORTUGAL:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\portugal 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_portugal, image=photo)
label.image = photo
label.place(x=100, y=100)

image_path = "D:\\bg pics\\portugal 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_portugal, image=photo)
label.image = photo
label.place(x=550, y=100)

image_path = "D:\\bg pics\\portugal 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_portugal, image=photo)
label.image = photo
label.place(x=980, y=100)

l2 = s.Label(frame_of_portugal, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features:
   \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)
b2 = s.Button(frame_of_portugal, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [portugal_to_book()])
b2.place(x=1250, y=600)

b4 = s.Button(frame_of_portugal, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [portugal_to_railway2()])
b4.place(x=50, y=600)

# portugal stops--------------------------------------------------------------------------------------------------------------------------

# england starts---------------------------------------------------------------------------------------------------------------------------

frame_of_england = Frame(window, bg="#023D54")

lo = s.Label(frame_of_england, text="ENGLAND:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "D:\\bg pics\\england 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_england, image=photo)
label.image = photo
label.place(x=100, y=100)

image_path = "D:\\bg pics\\england 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_england, image=photo)
label.image = photo
label.place(x=550, y=100)

image_path = "D:\\bg pics\\england 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_england, image=photo)
label.image = photo
label.place(x=980, y=100)
l2 = s.Label(frame_of_england, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features
       \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=100, y=400)

b2 = s.Button(frame_of_england, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [england_to_book()])
b2.place(x=1250, y=600)

b4 = s.Button(frame_of_england, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [england_to_railway2()])
b4.place(x=50, y=600)

# england stops-------------------------------------------------------------------------------------------------------------------------

# Booking pageStarts 1 ---------------------------------------------------------------------------------------------------------------------------------

booking_frame = Frame(window, bg="#023D54")

lo = s.Label(booking_frame, text="BOOKING DETAILS", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lo.place(x=550, y=30)
l1 = s.Label(booking_frame, text="ENTER YOUR NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=150, y=125)
i1 = s.Entry(booking_frame, width=20, font=("Comic Sans MS", 20))
i1.place(x=750, y=125)
l2 = s.Label(booking_frame, text="ENTER YOUR DOB", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=150, y=210)
i2 = s.Entry(booking_frame, font=("Comic Sans MS", 20))
i2.place(x=750, y=210)
l3 = s.Label(booking_frame, text="ENTER YOUR NO OF PASSENGERS", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=150, y=300)

def calculate():
    try:
        value = float(entry.get())
        result = value * 65000
        l.config(text=f"Amount: {result}")
    except ValueError:
        l.config(text="Invalid Passengers")


entry = s.Entry(booking_frame, font=("Comic Sans MS", 15))
entry.place(x=750, y=310)

# Create a button to trigger the calculation
l3 = s.Button(booking_frame, text="Submit",font="Timesnewroman", width=8, height=1, command=calculate)
l3.place(x=1050, y=312)

air=Combobox(booking_frame,font=("Comic Sans MS", 10))
air["values"]=("Select","First Class","Premium Class","Economy","Business class","Luxurious")
air.current(0)
air.place(x=1150,y=315)

# Create a label to display the result
l = s.Label(booking_frame, text="Amount: ", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l.place(x=750, y=600)

l4 = s.Label(booking_frame, text="PASSPORT NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l4.place(x=150, y=400)
i4 = s.Entry(booking_frame, font=("Comic Sans MS", 20))
i4.place(x=750, y=400)
l5 = s.Label(booking_frame, text="PHONE NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l5.place(x=150, y=500)
i5 = s.Entry(booking_frame, font=("Comic Sans MS", 20))
i5.place(x=750, y=500)

b2 = s.Button(booking_frame, text="PAYMENT METHOD", font="Timesnewroman", width=17, height=2,command=lambda: [book_to_payment()])
b2.place(x=1150, y=600)

b3 = s.Button(booking_frame, text="BACK", font="Timesnewromen", width=8, height=2,command=lambda: [payment_to_welcome()])
b3.place(x=50, y=600)

# Booking Ends-1----------------------------------------------------------------------------------------------------------------------------------

# Payment page Starts-----------------------------------------------------------------------------------------------------------------------------

payment_frame = Frame(window, bg="#023D54")

lo = s.Label(payment_frame, text="PAYMENT METHOD", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lo.place(x=550, y=30)

# DEBIT CARD PIC

image_path = "D:\\bg pics\\debit card.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame, image=photo)
label.image = photo
label.place(x=175, y=330)
l1 = s.Label(payment_frame, text="1.Debit Card", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=580, y=125)
b1 = s.Button(payment_frame, text="DEBIT CARD", font="Timesnewroman", width=17, height=2,command=lambda: [payment_to_debit()])
b1.place(x=200, y=555)

debit_frame = Frame(window, bg="#023D54")

l1 = s.Label(debit_frame, text="DEBIT CARD", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=600, y=70)

l1 = s.Label(debit_frame, text="ENTER CARD NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=350, y=200)

debit_card_1 = s.Entry(debit_frame, width=20, font=("Comic Sans MS", 20))
debit_card_1.place(x=750, y=200)

l2 = s.Label(debit_frame, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=350, y=300)

debit_amount= s.Entry(debit_frame, font=("Comic Sans MS", 20))
debit_amount.place(x=750, y=300)

def debit_1():
    debit_card_no_1 = debit_card_1.get()
    debit_amount_1 = debit_amount.get()

    if debit_card_no_1 == "" or debit_amount== "":
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into airways values('" + debit_card_no_1 + "','" + debit_amount_1 + "')")
        db.commit()
        debit_to_last()

b2 = s.Button(debit_frame, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [debit_1()])
b2.place(x=620, y=400)
now = str(datetime.now())
l2 = s.Label(debit_frame, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=445, y=500)

last_frame = Frame(window, bg="#023D54")
image_path = "D:\\bg pics\\z last page.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(last_frame, image=photo)
label.image = photo
label.place(x=170, y=70)

# #UPI PAYMENT PIC

image_path = "D:\\bg pics\\upi payment.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame, image=photo)
label.image = photo
label.place(x=575, y=330)
l2 = s.Label(payment_frame, text="2.UPI Payment", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=580, y=175)
b2 = s.Button(payment_frame, text="UPI", font="Timesnewroman", width=17, height=2, command=lambda: [payment_to_upi()])
b2.place(x=600, y=555)

upi_frame = Frame(window, bg="#023D54")

l1 = s.Label(upi_frame, text="UPI PAYMENT", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=600, y=70)

l1 = s.Label(upi_frame, text="ENTER CARD NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=350, y=200)

upi_no_1= s.Entry(upi_frame, width=20, font=("Comic Sans MS", 20))
upi_no_1.place(x=750, y=200)

l2 = s.Label(upi_frame, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=350, y=300)

upi_amount = s.Entry(upi_frame, font=("Comic Sans MS", 20))
upi_amount.place(x=750, y=300)

def upi_1():
    upino = upi_no_1.get()
    amt_1 = upi_amount.get()

    if upino == "" or amt_1== "":
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into airways values('" + upino + "','" + amt_1 + "')")
        db.commit()
        upi_to_last()

b2 = s.Button(upi_frame, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [upi_1()])
b2.place(x=620, y=400)

now = str(datetime.now())

l2 = s.Label(upi_frame, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=445, y=500)

last_frame = Frame(window, bg="#023D54")
image_path = "D:\\bg pics\\z last page.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(last_frame, image=photo)
label.image = photo
label.place(x=170, y=70)

# NET BANKING
image_path = "D:\\bg pics\\net banking.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame, image=photo)
label.image = photo
label.place(x=975, y=330)
l3 = s.Label(payment_frame, text="3.Net Banking", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=580, y=225)
b2 = s.Button(payment_frame, text="NET BANK", font="Timesnewroman", width=17, height=2,command=lambda: [payment_to_net()])
b2.place(x=1000, y=555)

net_frame = Frame(window, bg="#023D54")

l1 = s.Label(net_frame, text="NET BANKING", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=600, y=70)

l1 = s.Label(net_frame, text="ENTER YOUR BANK NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=300, y=200)

upibank_1 = s.Entry(net_frame, width=20, font=("Comic Sans MS", 20))
upibank_1.place(x=750, y=200)

l2 = s.Label(net_frame, text="ENTER THE ACCOUNT NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=300, y=300)

upibank_account_no_1 = s.Entry(net_frame, font=("Comic Sans MS", 20))
upibank_account_no_1.place(x=750, y=300)

l3 = s.Label(net_frame, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=300, y=400)

net_bank_amt_1 = s.Entry(net_frame, font=("Comic Sans MS", 20))
net_bank_amt_1.place(x=750, y=400)


def netbank_1():
    netbank_name_1 = upibank_1.get()
    netbank_account_no_1= upibank_account_no_1.get()
    netbank_amount_1=net_bank_amt_1.get()

    if netbank_name_1 == "" or netbank_account_no_1== "" or netbank_amount_1=="":
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into airways values('" + netbank_name_1 + "','" + netbank_account_no_1 + "','" + netbank_amount_1 + "')")
        db.commit()
        net_to_last()

b2 = s.Button(net_frame, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [netbank_1])
b2.place(x=620, y=500)

now = str(datetime.now())
l2 = s.Label(net_frame, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=445, y=600)

last_frame = Frame(window, bg="#023D54")
image_path = "D:\\bg pics\\z last page.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(last_frame, image=photo)
label.image = photo
label.place(x=170, y=70)

b4 = s.Button(payment_frame, text="BACK", font="Timesnewromen", width=8, height=2, command=lambda: [payment_to_book()])
b4.place(x=50, y=600)
b4 = s.Button(payment_frame, text="BACK", font="Timesnewromen", width=8, height=2, command=lambda: [payment_to_book()])
b4.place(x=50, y=600)

window.mainloop()
