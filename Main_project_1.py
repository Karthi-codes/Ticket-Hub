import re
from tkinter import *
import tkinter as s
import pymysql
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
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
    frame_of_sign.pack_forget()
    frame_of_welcome.pack(fill=BOTH, expand=True)


def login_to_welcome():
    frame_of_login.pack_forget()
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
    booking_frame_2.pack(fill=BOTH, expand=True)


def jammu_to_book():
    frame_of_jammu.pack_forget()
    booking_frame_2.pack(fill=BOTH, expand=True)


def darjelling_to_book():
    frame_of_darjelling.pack_forget()
    booking_frame_2.pack(fill=BOTH, expand=True)


def leh_ladakh_to_book():
    frame_of_ladak.pack_forget()
    booking_frame_2.pack(fill=BOTH, expand=True)


def kerala_to_book():
    frame_of_kerala.pack_forget()
    booking_frame_2.pack(fill=BOTH, expand=True)


def russia_to_book():
    frame_of_russia.pack_forget()
    booking_frame_3.pack(fill=BOTH, expand=True)


def tokyo_to_book():
    frame_of_tokyo.pack_forget()
    booking_frame_3.pack(fill=BOTH, expand=True)


def swizerland_to_book():
    frame_of_swizerland.pack_forget()
    booking_frame_3.pack(fill=BOTH, expand=True)


def barcelona_to_book():
    frame_of_barcelona.pack_forget()
    booking_frame_3.pack(fill=BOTH, expand=True)


def portugal_to_book():
    frame_of_portugal.pack_forget()
    booking_frame_3.pack(fill=BOTH, expand=True)


def england_to_book():
    frame_of_england.pack_forget()
    booking_frame_3.pack(fill=BOTH, expand=True)


def book_to_payment():
    booking_frame.pack_forget()
    payment_frame.pack(fill=BOTH, expand=True)


def payment_to_book():
    payment_frame.pack_forget()
    booking_frame.pack(fill=BOTH, expand=True)

def book_to_payment_1():
    booking_frame_2.pack_forget()
    payment_frame_1.pack(fill=BOTH, expand=True)

def payment_to_book_1():
    payment_frame_1.pack_forget()
    booking_frame_2.pack(fill=BOTH, expand=True)

def book_to_payment_2():
    booking_frame_3.pack_forget()
    payment_frame_2.pack(fill=BOTH, expand=True)

def payment_to_book_2():
    payment_frame_2.pack_forget()
    booking_frame_3.pack(fill=BOTH, expand=True)

def payment_to_welcome():
    booking_frame.pack_forget()
    frame_of_welcome.pack(fill=BOTH, expand=True)

def payment_to_welcome_1():
    booking_frame_2.pack_forget()
    frame_of_welcome.pack(fill=BOTH, expand=True)

def payment_to_welcome_2():
    booking_frame_3.pack_forget()
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

#Payment 2 -------------------------------------------------------------------------------------------------------------------------------------------

def payment_to_debit_1():
    payment_frame_1.pack_forget()
    debit_frame_1.pack(fill=BOTH, expand=True)


def payment_to_upi_1():
    payment_frame_1.pack_forget()
    upi_frame_1.pack(fill=BOTH, expand=True)


def payment_to_net_1():
    payment_frame_1.pack_forget()
    net_frame_1.pack(fill=BOTH, expand=True)


def debit_to_last_1():
    debit_frame_1.pack_forget()
    last_frame.pack(fill=BOTH, expand=True)


def upi_to_last_1():
    upi_frame_1.pack_forget()
    last_frame.pack(fill=BOTH, expand=True)


def net_to_last_1():
    net_frame_1.pack_forget()
    last_frame.pack(fill=BOTH, expand=True)

#Payment 3 -------------------------------------------------------------------------------------------------------------------------------------------

def payment_to_debit_2():
    payment_frame_2.pack_forget()
    debit_frame_2.pack(fill=BOTH, expand=True)


def payment_to_upi_2():
    payment_frame_2.pack_forget()
    upi_frame_2.pack(fill=BOTH, expand=True)


def payment_to_net_2():
    payment_frame_2.pack_forget()
    net_frame_2.pack(fill=BOTH, expand=True)


def debit_to_last_2():
    debit_frame_2.pack_forget()
    last_frame.pack(fill=BOTH, expand=True)


def upi_to_last_2():
    upi_frame_2.pack_forget()
    last_frame.pack(fill=BOTH, expand=True)


def net_to_last_2():
    net_frame_2.pack_forget()
    last_frame.pack(fill=BOTH, expand=True)

# Main Page Start------------------------------------------------------------------------------------------------------------

# Frame page
home_page = Frame(window, bg="#023D54")

image_of_homepage ="Pics/Frontpage1.png"
image = Image.open(image_of_homepage)
photo = ImageTk.PhotoImage(image)
label = Label(home_page, image=photo)
label.image = photo
label.place(x=225, y=40)

login = Button(home_page, text="ENTER", font="Timesnewroman", width=8, height=2,command=lambda: [home_to_sign(), sing_to_home])
login.place(x=725, y=650)
home_page.pack(fill=BOTH, expand=True)

# Main page Ends-----------------------------------------------------------------------------------------------------------------

# Login Page Starts---------------------------------------------------------------------------------------------------------------

frame_of_sign = Frame(window, bg="#023D54")

lo = Label(frame_of_sign, text="LOGIN IN", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lo.place(x=675, y=100)

l1 = Label(frame_of_sign, text="USER NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=500, y=195)

user_name_login = Entry(frame_of_sign, width=20, font=("Comic Sans MS", 20))
user_name_login.insert(0,"Enter Your Name")
user_name_login.place(x=700, y=200)

l2 = Label(frame_of_sign, text="PASSWORD", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=500, y=300)

user_password_login= Entry(frame_of_sign, show="*",font=("Comic Sans MS", 20))
user_password_login.place(x=700, y=305)

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
b2.place(x=700, y=400)

b3 = Button(frame_of_sign, text="SIGN IN ", font="Timesnewroman", width=8, height=2, command=lambda:[sing_to_login()])
b3.place(x=1200, y=600)

b3 = Button(frame_of_sign, text="BACK", font="Timesnewroman", width=8, height=2, command=lambda: [sing_to_home()])
b3.place(x=50, y=600)

# Login page Ends---------------------------------------------------------------------------------------------------------------------

# SignIn page Start-------------------------------------------------------------------------------------------------------------------

frame_of_login = Frame(window, bg="#023D54")

lo = Label(frame_of_login, text="SIGN IN", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lo.place(x=675, y=100)

name_1 = Label(frame_of_login, text="ENTER YOUR NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
name_1.place(x=420, y=175)

user_name = Entry(frame_of_login, width=20, font=("Comic Sans MS", 20))
user_name.place(x=800, y=180)

name_2 = Label(frame_of_login, text="CREATE YOUR PASSWORD", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
name_2.place(x=420, y=275)

pass_word = Entry(frame_of_login, width=20, font=("Comic Sans MS", 20))
pass_word.place(x=800, y=280)

name_3 = Label(frame_of_login, text="ENTER YOUR PHONE NO", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
name_3.place(x=420, y=375)

phone_no= Entry(frame_of_login, width=20, font=("Comic Sans MS", 20))
phone_no.place(x=800, y=380)


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
b1.place(x=690, y=498)

# SignIn page Ends--------------------------------------------------------------------------------------------------------------------------

# Welcome page Starts----------------------------------------------------------------------------------------------------------------------

frame_of_welcome = Frame(window, bg="#023D54")

lo = s.Label(frame_of_welcome, text="WELCOME TO OUR APPLICATION", bg="#023D54", fg="white", font=("Comic Sans MS", 40))
lo.place(x=350, y=50)
image_path = "Pics/Travelling Modes 2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_welcome, image=photo)
label.image = photo
label.place(x=150, y=200)
b1 = s.Button(frame_of_welcome, text="RAILWAYS", font="Timesnewroman", width=9, height=2,command=lambda: [welcome_to_railway()])
b1.place(x=1140, y=530)

image_path = "Pics/Travelling Modes 1.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_welcome, image=photo)
label.image = photo
label.place(x=600, y=200)
b2 = s.Button(frame_of_welcome, text="AIRWAYS", font="Timesnewroman", width=9, height=2,command=lambda: [welcome_to_airway()])
b2.place(x=245, y=530)

image_path = "Pics/Travelling Modes 3.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_welcome, image=photo)
label.image = photo
label.place(x=1030, y=200)
b3 = s.Button(frame_of_welcome, text="ROADWAYS", font="Timesnewroman", width=10, height=2,command=lambda: [welcome_to_roadway()])
b3.place(x=700, y=530)

welcome_to_home_b = Button(frame_of_welcome, text="BACK", font="Timesnewroman", width=8, height=2,command=lambda: [welcome_to_home()])
welcome_to_home_b.place(x=50, y=650)

# Welcome Ends--------------------------------------------------------------------------------------------------------------------------

# Airway Starts--------------------------------------------------------------------------------------------------------------------------

frame_of_airway = Frame(window, bg="#023D54")

lo = s.Label(frame_of_airway, text="WELCOME TO OUR AIRLINE BOOKING SECTION", bg="#023D54", fg="white",
             font=("Comic Sans MS", 25))
lo.place(x=375, y=50)

image_path = "Pics/berlin2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_airway, image=photo)
label.image = photo
label.place(x=150, y=200)
b1 = s.Button(frame_of_airway, text="BERLIN", font="Timesnewromen", width=9, height=2, command=lambda: [airway_to_berlin()])
b1.place(x=259, y=530)

image_path = "Pics/france2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_airway, image=photo)
label.image = photo
label.place(x=600, y=200)
b2 = s.Button(frame_of_airway, text="FRANCE", font="Timesnewromen", width=9, height=2,command=lambda: [airway_to_france()])
b2.place(x=705, y=530)

image_path = "Pics/qatar2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_airway, image=photo)
label.image = photo
label.place(x=1030, y=200)
b3 = s.Button(frame_of_airway, text="QATAR", font="Timesnewromen", width=10, height=2,command=lambda: [airway_to_qatar()])
b3.place(x=1130, y=530)

b4 = s.Button(frame_of_airway, text="NEXT", font="Timesnewromen", width=8, height=2,command=lambda: [airway_to_moscow_and_malyasia()])
b4.place(x=1350, y=650)

airway_to_home = Button(frame_of_airway, text="BACK", font="Timesnewroman", width=8, height=2,command=lambda: [airway_to_welcome()])
airway_to_home.place(x=50, y=650)

# Airway Ends------------------------------------------------------------------------------------------------------------------------------------

# Airway2 Starts-------------------------------------------------------------------------------------------------------------------------------------

frame_of_moscow_and_malaysia = Frame(window, bg="#023D54")

image_path = "Pics/moscow2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_moscow_and_malaysia, image=photo)
label.image = photo
label.place(x=300, y=200)
b1 = s.Button(frame_of_moscow_and_malaysia, text="MOSCOW", font="Timesnewromen", width=10, height=2,command=lambda: [mo_mal_to_moscow()])
b1.place(x=400, y=530)

image_path = "Pics/Malaysia2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_moscow_and_malaysia, image=photo)
label.image = photo
label.place(x=900, y=200)
b2 = s.Button(frame_of_moscow_and_malaysia, text="MALAYSIA", font="Timesnewromen", width=10, height=2,command=lambda: [mo_mal_to_malaysia()])
b2.place(x=1000, y=530)

qatar_to_airway_button = Button(frame_of_moscow_and_malaysia, text="BACK", font="Timesnewroman", width=8, height=2,command=lambda: [moscow_and_malaysia_to_airway()])
qatar_to_airway_button.place(x=50, y=600)

# Airway2 Ends----------------------------------------------------------------------------------------------------------------------------------------

# Berlin Starts---------------------------------------------------------------------------------------------------------------------------

frame_of_berlin = Frame(window, bg="#023D54")

lo = s.Label(frame_of_berlin, text="BERLIN:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/berlin 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_berlin, image=photo)
label.image = photo
label.place(x=200, y=100)
image_path = "bg pics/berlin 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_berlin, image=photo)
label.image = photo
label.place(x=650, y=100)
image_path = "bg pics/berlin 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_berlin, image=photo)
label.image = photo
label.place(x=1080, y=100)
l2 = s.Label(frame_of_berlin, text='''The Travel App Booking is a comprehensive solution designed to make travel planning seamless, efficient, and enjoyable.\nWith real-time availability, secure payments, and personalised recommendations, FlyBook ensures that your travel experience is hassle-free from start to finish.
\nKey Features:
\nReal-Time Availability & Pricing\n24/7 Customer Support\nBooking Management\nCost Savings\nPersonalisation\nSecurity''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=200, y=400)
b2 = s.Button(frame_of_berlin, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [berlin_to_book()])
b2.place(x=1350, y=650)

berlin_to_airway_button = Button(frame_of_berlin, text="BACK", font="Timesnewroman", width=8, height=2,command=lambda: [berlin_to_airway()])
berlin_to_airway_button.place(x=50, y=650)

# Berlin Ends----------------------------------------------------------------------------------------------------------------------------

# France Starts--------------------------------------------------------------------------------------------------------------------------

frame_of_france = Frame(window, bg="#023D54")

lo = s.Label(frame_of_france, text="FRANCE:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/france 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_france, image=photo)
label.image = photo
label.place(x=200, y=100)
image_path = "bg pics/france 3.jpeg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_france, image=photo)
label.image = photo
label.place(x=650, y=100)
image_path ="bg pics/france 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_france, image=photo)
label.image = photo
label.place(x=1080, y=100)
l2 = s.Label(frame_of_france, text='''The Travel App Booking is a comprehensive solution designed to make travel planning seamless, efficient, and enjoyable.\nWith real-time availability, secure payments, and personalised recommendations, FlyBook ensures that your travel experience is hassle-free from start to finish.
\nKey Features:
\nReal-Time Availability & Pricing\n24/7 Customer Support\nBooking Management\nCost Savings\nPersonalisation\nSecurity''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=200, y=400)
b2 = s.Button(frame_of_france, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [france_to_book()])
b2.place(x=1350, y=650)

france_to_airway_button = Button(frame_of_france, text="BACK", font="Timesnewroman", width=8, height=2,
                                 command=lambda: [france_to_airway()])
france_to_airway_button.place(x=50, y=650)

# France Ends-----------------------------------------------------------------------------------------------------------------------------

# Qatar Starts--------------------------------------------------------------------------------------------------------------------------------------

frame_of_qatar = Frame(window, bg="#023D54")

lo = s.Label(frame_of_qatar, text="QATAR:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/qatar 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_qatar, image=photo)
label.image = photo
label.place(x=200, y=100)
image_path = "bg pics/qatar 2.jpeg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_qatar, image=photo)
label.image = photo
label.place(x=650, y=100)
image_path = "bg pics/qatar 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_qatar, image=photo)
label.image = photo
label.place(x=1080, y=100)
l2 = s.Label(frame_of_qatar, text='''The Travel App Booking is a comprehensive solution designed to make travel planning seamless, efficient, and enjoyable.\nWith real-time availability, secure payments, and personalised recommendations, FlyBook ensures that your travel experience is hassle-free from start to finish.
   \nKey Features:
   \nReal-Time Availability & Pricing\n24/7 Customer Support\nBooking Management\nCost Savings\nPersonalisation\nSecurity''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=200, y=400)
b2 = s.Button(frame_of_qatar, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [qatar_to_book()])
b2.place(x=1350, y=650)

qatar_to_airway_button = Button(frame_of_qatar, text="BACK", font="Timesnewroman", width=8, height=2,
                                command=lambda: [qatar_to_airway()])
qatar_to_airway_button.place(x=50, y=650)

# Qatar Ends---------------------------------------------------------------------------------------------------------------------------------------

# Moscow Starts-------------------------------------------------------------------------------------------------------------------------------------

frame_of_moscow = Frame(window, bg="#023D54")

lo = s.Label(frame_of_moscow, text="MOSCOW:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/moscow 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_moscow, image=photo)
label.image = photo
label.place(x=200, y=100)
image_path = "bg pics/moscow 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_moscow, image=photo)
label.image = photo
label.place(x=650, y=100)
image_path = "bg pics/moscow 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_moscow, image=photo)
label.image = photo
label.place(x=1080, y=100)
l2 = s.Label(frame_of_moscow, text='''The Travel App Booking is a comprehensive solution designed to make travel planning seamless, efficient, and enjoyable.\nWith real-time availability, secure payments, and personalised recommendations, FlyBook ensures that your travel experience is hassle-free from start to finish.
   \nKey Features:
   \nReal-Time Availability & Pricing\n24/7 Customer Support\nBooking Management\nCost Savings\nPersonalisation\nSecurity''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=200, y=400)

b2 = s.Button(frame_of_moscow, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [moscow_to_book()])
b2.place(x=1350, y=650)

moscow_to_airway_button = Button(frame_of_moscow, text="BACK", font="Timesnewroman", width=8, height=2,
                                 command=lambda: [moscow_to_mo_mal()])
moscow_to_airway_button.place(x=50, y=650)

# Moscow Ends----------------------------------------------------------------------------------------------------------------------------------------

# Malyasia Starts-------------------------------------------------------------------------------------------------------------------------------------

frame_of_malaysia = Frame(window, bg="#023D54")

lo = s.Label(frame_of_malaysia, text="MALAYSIA:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/malaysia 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_malaysia, image=photo)
label.image = photo
label.place(x=200, y=100)
image_path = "bg pics/malaysia 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_malaysia, image=photo)
label.image = photo
label.place(x=650, y=100)
image_path = "bg pics/malaysia 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_malaysia, image=photo)
label.image = photo
label.place(x=1080, y=100)
l2 = s.Label(frame_of_malaysia, text='''The Travel App Booking is a comprehensive solution designed to make travel planning seamless, efficient, and enjoyable.\nWith real-time availability, secure payments, and personalised recommendations, FlyBook ensures that your travel experience is hassle-free from start to finish.
   \nKey Features:
   \nReal-Time Availability & Pricing\n24/7 Customer Support\nBooking Management\nCost Savings\nPersonalisation\nSecurity''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=200, y=400)
b2 = s.Button(frame_of_malaysia, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [malaysia_to_book()])
b2.place(x=1350, y=650)

malaysia_to_airway_button = Button(frame_of_malaysia, text="BACK", font="Timesnewroman", width=8, height=2,
                                   command=lambda: [malaysia_to_mo_mal()])
malaysia_to_airway_button.place(x=50, y=650)

# Malaysia Ends---------------------------------------------------------------------------------------------------------------------------------------

# Roadway Starts--------------------------------------------------------------------------------------------------------------------------------------

frame_of_roadway = Frame(window, bg="#023D54")

lo = s.Label(frame_of_roadway, text="WELCOME TO OUR ROADWAYS BOOKING SECTION", bg="#023D54", fg="white",
             font=("Comic Sans MS", 25))
lo.place(x=375, y=50)
image_path = "Pics/Amarnath.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_roadway, image=photo)
label.image = photo
label.place(x=150, y=200)
b1 = s.Button(frame_of_roadway, text="AMARNATH", font="Timesnewromen", width=10, height=2,
              command=lambda: [roadway_to_amarnath()])
b1.place(x=250, y=530)

image_path = "Pics/Jammu.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_roadway, image=photo)
label.image = photo
label.place(x=600, y=200)
b2 = s.Button(frame_of_roadway, text="JAMMU & KASHMIR", font="Timesnewromen", width=17, height=2,
              command=lambda: [roadway_to_jammu()])
b2.place(x=655, y=530)

image_path = "Pics/Darjeeling.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_roadway, image=photo)
label.image = photo
label.place(x=1030, y=200)
b3 = s.Button(frame_of_roadway, text="DARJEELING", font="Timesnewromen", width=11, height=2,
              command=lambda: [roadway_to_darjelling()])
b3.place(x=1130, y=530)
b4 = s.Button(frame_of_roadway, text="NEXT", font="Timesnewromen", width=8, height=2,
              command=lambda: [roadway_to_roadway2()])
b4.place(x=1350, y=650)

roadway_to_home = Button(frame_of_roadway, text="BACK", font="Timesnewroman", width=8, height=2,
                         command=lambda: [roadway_to_welcome()])
roadway_to_home.place(x=50, y=650)

# Roadway Ends---------------------------------------------------------------------------------------------------------------------------------

# Roadway 2 Starts------------------------------------------------------------------------------------------------------------------------------

frame_of_roadway2 = Frame(window, bg="#023D54")

image_path = "Pics/kerala.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_roadway2, image=photo)
label.image = photo
label.place(x=300, y=200)
b1 = s.Button(frame_of_roadway2, text="KERALA", font="Timesnewromen", width=10, height=2,
              command=lambda: [roadway2_to_kerala()])
b1.place(x=400, y=530)

image_path = "Pics/Leh-Ladakh.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_roadway2, image=photo)
label.image = photo
label.place(x=950, y=200)
b2 = s.Button(frame_of_roadway2, text="LEH & LADAKH", font="Timesnewromen", width=15, height=2,
              command=lambda: [roadway2_to_ladak()])
b2.place(x=1015, y=530)

roadway2_to_roadway1 = Button(frame_of_roadway2, text="BACK", font="Timesnewroman", width=8, height=2,
                              command=lambda: [roadway2_to_roadway()])
roadway2_to_roadway1.place(x=50, y=650)

# Roadway 2 Ends-----------------------------------------------------------------------------------------------------------------------------------

# Amarnath Starts----------------------------------------------------------------------------------------------------------------------------------

frame_of_amarnath = Frame(window, bg="#023D54")

lo = s.Label(frame_of_amarnath, text="AMARNATH:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/amarnath 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_amarnath, image=photo)
label.image = photo
label.place(x=200, y=100)

image_path = "bg pics/amarnath 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_amarnath, image=photo)
label.image = photo
label.place(x=650, y=100)

image_path = "bg pics/amarnath 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_amarnath, image=photo)
label.image = photo
label.place(x=1080, y=100)

l2 = s.Label(frame_of_amarnath, text='''RoadWays is a comprehensive application designed to simplify road transport bookings, offering users the ability to plan trips, 
book bus tickets, and track routes with ease.Whether you are traveling across cities or within local areas, RoadWays ensures a smooth booking experience with 
multiple transport options available at your fingertips.
\nKey Features: \n1.Bus Ticket Booking\n2.Real-time Bus Tracking\n3.Discounts & Offers\n4.Reschedule\n5.Payment Flexibility''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=200, y=400)
b2 = s.Button(frame_of_amarnath, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [amarnath_to_book()])
b2.place(x=1350, y=650)

amarnath_to_roadway_button = Button(frame_of_amarnath, text="BACK", font="Timesnewroman", width=8, height=2,
                                    command=lambda: [amarnath_to_roadway()])
amarnath_to_roadway_button.place(x=50, y=650)

# Amarnath Ends---------------------------------------------------------------------------------------------------------------------------------------

# Jammukashmir Starts-------------------------------------------------------------------------------------------------------------------------------

frame_of_jammu = Frame(window, bg="#023D54")

lo = Label(frame_of_jammu, text="JAMMU & KASHMIR:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/jammu & kashmir 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = Label(frame_of_jammu, image=photo)
label.image = photo
label.place(x=200, y=100)
image_path = "bg pics/jammu & kashmir 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = Label(frame_of_jammu, image=photo)
label.image = photo
label.place(x=650, y=100)
image_path = "bg pics/jammu & kashmir 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = Label(frame_of_jammu, image=photo)
label.image = photo
label.place(x=1080, y=100)
l2 = Label(frame_of_jammu, text='''RoadWays is a comprehensive application designed to simplify road transport bookings, offering users the ability to plan trips, 
book bus tickets, and track routes with ease.Whether you are traveling across cities or within local areas, RoadWays ensures a smooth booking experience with 
multiple transport options available at your fingertips.
\nKey Features: \n1.Bus Ticket Booking\n2.Real-time Bus Tracking\n3.Discounts & Offers\n4.Reschedule\n5.Payment Flexibility''',
           bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=200, y=400)

b2 = s.Button(frame_of_jammu, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [jammu_to_book()])
b2.place(x=1350, y=650)

jammu_to_roadway_button = Button(frame_of_jammu, text="BACK", font="Timesnewroman", width=8, height=2,command=lambda: [jammu_to_roadway()])
jammu_to_roadway_button.place(x=50, y=650)


# Jamukashimr Ends---------------------------------------------------------------------------------------------------------------------------------

# darjelling starts--------------------------------------------------------------------------------------------------------------------------------

frame_of_darjelling = Frame(window, bg="#023D54")

lo = s.Label(frame_of_darjelling, text="DARJEELING:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/darjeeling 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_darjelling, image=photo)
label.image = photo
label.place(x=200, y=100)

image_path = "bg pics/darjeeling 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_darjelling, image=photo)
label.image = photo
label.place(x=650, y=100)

image_path = "bg pics/darjeeling 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_darjelling, image=photo)
label.image = photo
label.place(x=1080, y=100)

l2 = s.Label(frame_of_darjelling, text='''RoadWays is a comprehensive application designed to simplify road transport bookings, offering users the ability to plan trips, 
book bus tickets, and track routes with ease.Whether you are traveling across cities or within local areas, RoadWays ensures a smooth booking experience with 
multiple transport options available at your fingertips.
\nKey Features: \n1.Bus Ticket Booking\n2.Real-time Bus Tracking\n3.Discounts & Offers\n4.Reschedule\n5.Payment Flexibility''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=200, y=400)

b2 = s.Button(frame_of_darjelling, text="BOOK", font="Timesnewromen", width=9, height=2,command=lambda: [darjelling_to_book()])
b2.place(x=1350, y=650)

darjelling_to_roadway_button = Button(frame_of_darjelling, text="BACK", font="Timesnewroman", width=8, height=2,command=lambda: [darjelling_to_roadway()])
darjelling_to_roadway_button.place(x=50, y=650)

# darjelling stops---------------------------------------------------------------------------------------------------------------------------------

# Kerala Starts------------------------------------------------------------------------------------------------------------------------------------

frame_of_kerala = Frame(window, bg="#023D54")

lo = s.Label(frame_of_kerala, text="KERALA:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/kerala 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_kerala, image=photo)
label.image = photo
label.place(x=200, y=100)
image_path = "bg pics/kerala 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_kerala, image=photo)
label.image = photo
label.place(x=650, y=100)
image_path = "bg pics/kerala 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_kerala, image=photo)
label.image = photo
label.place(x=1080, y=100)
l2 = s.Label(frame_of_kerala, text='''RoadWays is a comprehensive application designed to simplify road transport bookings, offering users the ability to plan trips, 
book bus tickets, and track routes with ease.Whether you are traveling across cities or within local areas, RoadWays ensures a smooth booking experience with 
multiple transport options available at your fingertips.
\nKey Features: \n1.Bus Ticket Booking\n2.Real-time Bus Tracking\n3.Discounts & Offers\n4.Reschedule\n5.Payment Flexibility''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=200, y=400)

b2 = s.Button(frame_of_kerala, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [kerala_to_book()])
b2.place(x=1350, y=650)

roadway2_to_kerala_button = Button(frame_of_kerala, text="BACK", font="Timesnewroman", width=8, height=2,
                                   command=lambda: [kerala_to_roadway2()])
roadway2_to_kerala_button.place(x=50, y=650)

# Kerala Ends--------------------------------------------------------------------------------------------------------------------------------------

# Ladakh Starts-------------------------------------------------------------------------------------------------------------------------------------

frame_of_ladak = Frame(window, bg="#023D54")

lo = s.Label(frame_of_ladak, text="LEH_LADAKH:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/leh & ladakh 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_ladak, image=photo)
label.image = photo
label.place(x=200, y=100)
image_path = "bg pics/leh & ladakh 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_ladak, image=photo)
label.image = photo
label.place(x=650, y=100)
image_path = "bg pics/leh & ladakh 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_ladak, image=photo)
label.image = photo
label.place(x=1080, y=100)
l2 = s.Label(frame_of_ladak, text='''RoadWays is a comprehensive application designed to simplify road transport bookings, offering users the ability to plan trips, 
book bus tickets, and track routes with ease.Whether you are traveling across cities or within local areas, RoadWays ensures a smooth booking experience with 
multiple transport options available at your fingertips.
\nKey Features: \n1.Bus Ticket Booking\n2.Real-time Bus Tracking\n3.Discounts & Offers\n4.Reschedule\n5.Payment Flexibility''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=200, y=400)

b2 = s.Button(frame_of_ladak, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [leh_ladakh_to_book()])
b2.place(x=1350, y=650)

roadway2_to_ladak_button = Button(frame_of_ladak, text="BACK", font="Timesnewroman", width=8, height=2,
                                  command=lambda: [ladak_to_roadway2()])
roadway2_to_ladak_button.place(x=50, y=650)

# Ladak Ends---------------------------------------------------------------------------------------------------------------------------------------

# Railway Starts-------------------------------------------------------------------------------------------------------------------------------

frame_of_railway = Frame(window, bg="#023D54")

lo = s.Label(frame_of_railway, text="WELCOME TO OUR RAILWAYS BOOKING SECTION", bg="#023D54", fg="white",
             font=("Comic Sans MS", 25))
lo.place(x=375, y=50)
image_path = "Pics/Russia.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway, image=photo)
label.image = photo
label.place(x=200, y=200)
b1 = s.Button(frame_of_railway, text="RUSSIA", font="Timesnewromen", width=10, height=2,
              command=lambda: [railway_to_russia()])
b1.place(x=280, y=530)

image_path = "Pics/Tokyo.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway, image=photo)
label.image = photo
label.place(x=650, y=200)
b2 = s.Button(frame_of_railway, text="TOKYO", font="Timesnewromen", width=10, height=2,
              command=lambda: [railway_to_tokyo()])
b2.place(x=740, y=530)

image_path = "Pics/Switzerland.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway, image=photo)
label.image = photo
label.place(x=1080, y=200)
b3 = s.Button(frame_of_railway, text="SWITZERLAND", font="Timesnewromen", width=13, height=2,
              command=lambda: [railway_to_swizerland()])
b3.place(x=1155, y=530)

b4 = s.Button(frame_of_railway, text="NEXT", font="Timesnewromen", width=8, height=2,
              command=lambda: [railway_to_railway2()])
b4.place(x=1350, y=650)

b4 = s.Button(frame_of_railway, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [railway_to_welcome()])
b4.place(x=50, y=650)

# Railway Ends---------------------------------------------------------------------------------------------------------------------------------

# Railway2 Starts-------------------------------------------------------------------------------------------------------------------------------

frame_of_railway2 = Frame(window, bg="#023D54")

image_path = "Pics/Barcelona.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway2, image=photo)
label.image = photo
label.place(x=200, y=200)
b1 = s.Button(frame_of_railway2, text="BARCELONA", font="Timesnewromen", width=12, height=2,
              command=lambda: [railway2_to_barcelona()])
b1.place(x=280, y=530)

image_path = "Pics/Portugal.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway2, image=photo)
label.image = photo
label.place(x=650, y=200)
b2 = s.Button(frame_of_railway2, text="PORTUGAL", font="Timesnewromen", width=10, height=2,
              command=lambda: [railway2_to_portugal()])
b2.place(x=740, y=530)

image_path = "Pics/England.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_railway2, image=photo)
label.image = photo
label.place(x=1080, y=200)
b3 = s.Button(frame_of_railway2, text="ENGLAND", font="Timesnewromen", width=10, height=2,
              command=lambda: [railway2_to_england()])
b3.place(x=1170, y=530)

b4 = s.Button(frame_of_railway2, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [railway2_to_railway()])
b4.place(x=50, y=650)

# Railway2 Ends---------------------------------------------------------------------------------------------------------------------------------

# russia starts--------------------------------------------------------------------------------------------------------------------------------

frame_of_russia = Frame(window, bg="#023D54")

lo = s.Label(frame_of_russia, text="RUSSIA:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/russia 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_russia, image=photo)
label.image = photo
label.place(x=200, y=100)

image_path = "bg pics/russia 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_russia, image=photo)
label.image = photo
label.place(x=650, y=100)
image_path = "bg pics/russia 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_russia, image=photo)
label.image = photo
label.place(x=1080, y=100)

l2 = s.Label(frame_of_russia, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features:
   \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=300, y=400)

b2 = s.Button(frame_of_russia, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [russia_to_book()])
b2.place(x=1350, y=650)

b4 = s.Button(frame_of_russia, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [russia_to_railway()])
b4.place(x=50, y=650)

# russia stops--------------------------------------------------------------------------------------------------------------------------------

# tokyo starts--------------------------------------------------------------------------------------------------------------------------------

frame_of_tokyo = Frame(window, bg="#023D54")

lo = s.Label(frame_of_tokyo, text="TOKYO:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/tokyo 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_tokyo, image=photo)
label.image = photo
label.place(x=200, y=100)

image_path = "bg pics/tokyo 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_tokyo, image=photo)
label.image = photo
label.place(x=650, y=100)

image_path = "bg pics/tokyo 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_tokyo, image=photo)
label.image = photo
label.place(x=1080, y=100)

l2 = s.Label(frame_of_tokyo, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features:
   \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=300, y=400)
b2 = s.Button(frame_of_tokyo, text="BOOK", font="Timesnewromen", width=9, height=2, command=lambda: [tokyo_to_book()])
b2.place(x=1350, y=650)

b4 = s.Button(frame_of_tokyo, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [tokyo_to_railway()])
b4.place(x=50, y=650)

# tokyo stops--------------------------------------------------------------------------------------------------------------------------------

# swizerland starts----------------------------------------------------------------------------------------------------------------------------------

frame_of_swizerland = Frame(window, bg="#023D54")

lo = s.Label(frame_of_swizerland, text="SWIZERLAND:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)

image_path = "bg pics/swizerland 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_swizerland, image=photo)
label.image = photo
label.place(x=200, y=100)

image_path = "bg pics/swizerland 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_swizerland, image=photo)
label.image = photo
label.place(x=650, y=100)

image_path = "bg pics/swizerland 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_swizerland, image=photo)
label.image = photo
label.place(x=1080, y=100)
l2 = s.Label(frame_of_swizerland, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features:
   \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=300, y=400)

b2 = s.Button(frame_of_swizerland, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [swizerland_to_book()])
b2.place(x=1350, y=650)

b4 = s.Button(frame_of_swizerland, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [swizerland_to_railway()])
b4.place(x=50, y=650)

# swizerland stops--------------------------------------------------------------------------------------------------------------------

# barcelona starts--------------------------------------------------------------------------------------------------------------------

frame_of_barcelona = Frame(window, bg="#023D54")

lo = s.Label(frame_of_barcelona, text="BARCELONA:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/barcelona 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_barcelona, image=photo)
label.image = photo
label.place(x=200, y=100)

image_path = "bg pics/barcelona 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_barcelona, image=photo)
label.image = photo
label.place(x=650, y=100)

image_path = "bg pics/barcelona 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_barcelona, image=photo)
label.image = photo
label.place(x=1080, y=100)

l2 = s.Label(frame_of_barcelona, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features:
   \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=300, y=400)
b2 = s.Button(frame_of_barcelona, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [barcelona_to_book()])
b2.place(x=1350, y=650)

b4 = s.Button(frame_of_barcelona, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [barcelona_to_railway2()])
b4.place(x=50, y=650)

# portugal starts--------------------------------------------------------------------------------------------------------------------------

frame_of_portugal = Frame(window, bg="#023D54")

lo = s.Label(frame_of_portugal, text="PORTUGAL:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/portugal 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_portugal, image=photo)
label.image = photo
label.place(x=200, y=100)

image_path = "bg pics/portugal 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_portugal, image=photo)
label.image = photo
label.place(x=650, y=100)

image_path = "bg pics/portugal 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_portugal, image=photo)
label.image = photo
label.place(x=1080, y=100)

l2 = s.Label(frame_of_portugal, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features:
   \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=300, y=400)
b2 = s.Button(frame_of_portugal, text="BOOK", font="Timesnewromen", width=9, height=2,
              command=lambda: [portugal_to_book()])
b2.place(x=1350, y=650)

b4 = s.Button(frame_of_portugal, text="BACK", font="Timesnewromen", width=8, height=2,
              command=lambda: [portugal_to_railway2()])
b4.place(x=50, y=650)

# portugal stops--------------------------------------------------------------------------------------------------------------------------

# england starts---------------------------------------------------------------------------------------------------------------------------

frame_of_england = Frame(window, bg="#023D54")

lo = s.Label(frame_of_england, text="ENGLAND:", bg="#023D54", fg="white", font=("Comic Sans MS", 25))
lo.place(x=100, y=25)
image_path = "bg pics/england 1.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_england, image=photo)
label.image = photo
label.place(x=200, y=100)

image_path = "bg pics/england 3.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_england, image=photo)
label.image = photo
label.place(x=650, y=100)

image_path = "bg pics/england 2.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(frame_of_england, image=photo)
label.image = photo
label.place(x=1080, y=100)
l2 = s.Label(frame_of_england, text='''EasyRail is an intuitive and user-friendly mobile application designed to simplify the process of booking railway tickets.\nWhether you’re planning a long-distance trip or a short commute, our app allows you to search, book, and manage your tickets seamlessly.
   \nKey Features
       \n1.Real-time Train Search\n2.Instant Ticket Booking\n3.PNR Status Updates\n4.Journey Management\n5.Multiple Payment ''',
             bg="#023D54", fg="white", font=("Comic Sans MS", 12))
l2.place(x=300, y=400)

b2 = s.Button(frame_of_england, text="BOOK", font="Timesnewromen", width=9, height=2,command=lambda: [england_to_book()])
b2.place(x=1350, y=650)

b4 = s.Button(frame_of_england, text="BACK", font="Timesnewromen", width=8, height=2,command=lambda: [england_to_railway2()])
b4.place(x=50, y=650)

# england stops-----------------------------------------------------------------------------------------------------------------------------------------

# Booking Starts 1 ---------------------------------------------------------------------------------------------------------------------------------

booking_frame = Frame(window, bg="#023D54")

lo = s.Label(booking_frame, text="AIRWAY BOOKING DETAILS", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lo.place(x=650, y=30)

l1 = s.Label(booking_frame, text="ENTER YOUR NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=250, y=125)

user_1 = s.Entry(booking_frame, width=20, font=("Comic Sans MS", 20))
user_1.place(x=850, y=125)

l2 = s.Label(booking_frame, text="ENTER YOUR DOB", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=250, y=210)

dob_1 = s.Entry(booking_frame, font=("Comic Sans MS", 20))
dob_1.place(x=850, y=210)

l3 = s.Label(booking_frame, text="ENTER YOUR NO OF PASSENGERS", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=250, y=300)

air= Combobox(booking_frame, font=("Comic Sans MS", 10))
air["values"]=("Select","First Class","Premium Class","Economy","Business class","Luxurious")
air.current(0)
air.place(x=1250,y=315)

l = s.Label(booking_frame, text="Amount: ", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l.place(x=850, y=600)

l4 = s.Label(booking_frame, text="PASSPORT NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l4.place(x=250, y=400)

passport_no_1 = s.Entry(booking_frame, font=("Comic Sans MS", 20))
passport_no_1.place(x=850, y=400)

l5 = s.Label(booking_frame, text="PHONE NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l5.place(x=250, y=500)

phone_no_1 = s.Entry(booking_frame, font=("Comic Sans MS", 20))
phone_no_1.place(x=850, y=500)

def airway_db():
    user_name_1 = user_1.get()
    DOB_1 = dob_1.get()
    passangers_Airway = entry.get()
    passport_No = passport_no_1.get()
    PhoneNo_1 = phone_no_1.get()
    selected_class = air.get()

    if user_name_1 == "" or DOB_1 == "" or passangers_Airway == "" or passport_No == "" or PhoneNo_1 == "" or selected_class == "":
        messagebox.showerror("Error", "Fill all the details")
        return

    try:
        try:
            formatted_dob = datetime.strptime(DOB_1, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid Date Format! Use DD/MM/YYYY")
            return

        try:
            value = float(passangers_Airway)
            result = value * 65000
            l.config(text=f"Amount: {result}")
        except ValueError:
            l.config(text="Invalid Passengers")
            return

        try:
            db = m.connect(host="localhost", user="root", password="K@rthi16", database="python")
            cur = db.cursor()

            query = """INSERT INTO airways (user_name, dob, airline, passport_no, phone_no, travel_class, total_amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            values = (user_name_1, formatted_dob, passangers_Airway, passport_No, PhoneNo_1, selected_class, result)

            cur.execute(query, values)
            db.commit()

            messagebox.showinfo("Submit", "Your Details Saved Successfully")

            clear_air()
            book_to_payment()

        except m.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")

    except Exception as e:
        messagebox.showerror("Unexpected Error", f"Error: {str(e)}")

entry = s.Entry(booking_frame, font=("Comic Sans MS", 15))
entry.place(x=850, y=310)

def clear_air():
    user_1.delete(0, END)
    dob_1.delete(0, END)
    entry.delete(0, END)
    passport_no_1.delete(0, END)
    phone_no_1.delete(0, END)
    air.delete(0,END)

b2 = s.Button(booking_frame, text="PAYMENT METHOD", font="Timesnewroman", width=17, height=2,command=lambda: [airway_db()])
b2.place(x=1250, y=650)

b3 = s.Button(booking_frame, text="BACK", font="Timesnewromen", width=8, height=2,command=lambda: [payment_to_welcome()])
b3.place(x=50, y=650)

# Booking Ends-1------------------------------------------------------------------------------------------------------------------------------------

# Booking Starts-2----------------------------------------------------------------------------------------------------------------------

booking_frame_2 = Frame(window, bg="#023D54")

loo = s.Label(booking_frame_2, text="ROADWAY BOOKING DETAILS", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
loo.place(x=650, y=30)

l11 = s.Label(booking_frame_2, text="ENTER YOUR NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l11.place(x=250, y=125)

user_2= s.Entry(booking_frame_2, width=20, font=("Comic Sans MS", 20))
user_2.place(x=850, y=125)

l22 = s.Label(booking_frame_2, text="ENTER YOUR DOB", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l22.place(x=250, y=210)

dob_2 = s.Entry(booking_frame_2, font=("Comic Sans MS", 20))
dob_2.place(x=850, y=210)

l33 = s.Label(booking_frame_2, text="ENTER YOUR NO OF PASSENGERS", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l33.place(x=250, y=300)

road= Combobox(booking_frame_2, font=("Comic Sans MS", 10))
road["values"]=("Select","First Class","Premium Class","Economy","Business class","Luxurious")
road.current(0)
road.place(x=1250,y=315)

ll = s.Label(booking_frame_2, text="Amount: ", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
ll.place(x=850, y=600)

l55 = s.Label(booking_frame_2, text="E_MAIL ADDRESS", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l55.place(x=250, y=400)

email_1= s.Entry(booking_frame_2, font=("Comic Sans MS", 20))
email_1.place(x=850, y=400)

l6 = s.Label(booking_frame_2, text="PHONE NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l6.place(x=250, y=500)

phone_no_2= s.Entry(booking_frame_2, font=("Comic Sans MS", 20))
phone_no_2.place(x=850, y=500)

def roadway_db():
    user_name_2 = user_2.get()
    DOB_2 = dob_2.get()
    passangers_roadway = entry_1.get()
    email = email_1.get()
    PhoneNo_2 = phone_no_2.get()
    selected_vehicle = road.get()

    if user_name_2 == "" or DOB_2 == "" or passangers_roadway == "" or email == "" or PhoneNo_2 == "" or selected_vehicle == "":
        messagebox.showerror("Error", "Fill all the details")
        return

    try:
        try:
            formatted_dob = datetime.strptime(DOB_2, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid Date Format! Use DD/MM/YYYY")
            return

        try:
            value = float(passangers_roadway)
            result = value * 6500
            ll.config(text=f"Amount: {result}")
        except ValueError:
            ll.config(text="Invalid Passengers")
            return

        email_pattern = r"[^@]+@[^@]+\.[a-zA-Z]{2,6}"
        if not re.match(email_pattern, email):
            messagebox.showerror("Error", "Invalid Email Format!")
            return

        try:
            db = m.connect(host="localhost", user="root", password="K@rthi16", database="python")
            cur = db.cursor()

            query = """INSERT INTO roadways (user_name, dob, passengers, email, phone_no, vehicle_type, total_amount)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            values = (user_name_2, formatted_dob, passangers_roadway, email, PhoneNo_2, selected_vehicle, result)

            cur.execute(query, values)
            db.commit()

            messagebox.showinfo("Submit", "Your Details Saved Successfully")

            clear_road()
            book_to_payment_1()

        except m.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")

    except Exception as e:
        messagebox.showerror("Unexpected Error", f"Error: {str(e)}")

entry_1 = s.Entry(booking_frame_2, font=("Comic Sans MS", 15))
entry_1.place(x=850, y=310)


def clear_road():
    user_2.delete(0, END)
    dob_2.delete(0, END)
    entry_1.delete(0, END)
    email_1.delete(0, END)
    phone_no_2.delete(0, END)
    road.delete(0,END)

b22 = s.Button(booking_frame_2, text="PAYMENT METHOD", font="Timesnewroman", width=17, height=2,command=lambda: [roadway_db()])
b22.place(x=1250, y=650)

b33 = s.Button(booking_frame_2, text="BACK", font="Timesnewromen", width=8, height=2,command=lambda: [payment_to_welcome_1()])
b33.place(x=50, y=650)

# Booking-2 Ends-------------------------------------------------------------------------------------------------------------------------

# Booking-3 starts-----------------------------------------------------------------------------------------------------------------------

booking_frame_3 = Frame(window, bg="#023D54")

looo = s.Label(booking_frame_3, text="RAILWAY BOOKING DETAILS", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
looo.place(x=650, y=30)

l111 = s.Label(booking_frame_3, text="ENTER YOUR NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l111.place(x=250, y=125)

user_3 = s.Entry(booking_frame_3, width=20, font=("Comic Sans MS", 20))
user_3.place(x=850, y=125)

l222 = s.Label(booking_frame_3, text="ENTER YOUR DOB", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l222.place(x=250, y=210)

dob_3= s.Entry(booking_frame_3, font=("Comic Sans MS", 20))
dob_3.place(x=850, y=210)

l333 = s.Label(booking_frame_3, text="ENTER YOUR NO OF PASSENGERS", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l333.place(x=250, y=300)

rail= Combobox(booking_frame_3, font=("Comic Sans MS", 10))
rail["values"]=("Select","First Ac","Second Ac","Third Ac","Sleeper","General")
rail.current(0)
rail.place(x=1250,y=315)

lll = s.Label(booking_frame_3, text="Amount: ", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lll.place(x=850, y=600)

l666 = s.Label(booking_frame_3, text="PHONE NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l666.place(x=250, y=400)

phone_no_3= s.Entry(booking_frame_3, font=("Comic Sans MS", 20))
phone_no_3.place(x=850, y=400)

def railway_db():
    user_name_3 = user_3.get()
    DOB_3 = dob_3.get()
    passangers_railway = entry_2.get()
    PhoneNo_3 = phone_no_3.get()
    selected_train_class = rail.get()

    if user_name_3 == "" or DOB_3 == "" or passangers_railway == "" or PhoneNo_3 == "" or selected_train_class == "":
        messagebox.showerror("Error", "Fill all the details")
        return

    try:
        try:
            formatted_dob = datetime.strptime(DOB_3, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid Date Format! Use DD/MM/YYYY")
            return

        try:
            value = float(passangers_railway)
            result = value * 25000
            lll.config(text=f"Amount: {result}")
        except ValueError:
            lll.config(text="Invalid Passengers")
            return

        try:
            db = m.connect(host="localhost", user="root", password="K@rthi16", database="python")
            cur = db.cursor()

            query = """INSERT INTO railways (user_name, dob, passengers, phone_no, train_class, total_amount)
                       VALUES (%s, %s, %s, %s, %s, %s)"""
            values = (user_name_3, formatted_dob, passangers_railway, PhoneNo_3, selected_train_class, result)

            cur.execute(query, values)
            db.commit()

            messagebox.showinfo("Submit", "Your Details Saved Successfully")

            clear_railway()
            book_to_payment_2()

        except m.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")

    except Exception as e:
        messagebox.showerror("Unexpected Error", f"Error: {str(e)}")

entry_2 = s.Entry(booking_frame_3, font=("Comic Sans MS", 15))
entry_2.place(x=850, y=310)

def clear_railway():
    user_3.delete(0, END)
    dob_3.delete(0, END)
    entry_2.delete(0, END)
    phone_no_3.delete(0, END)
    rail.delete(0,END)

b222 = s.Button(booking_frame_3, text="PAYMENT METHOD", font="Timesnewroman", width=17, height=2,command=lambda: [railway_db()])
b222.place(x=1250, y=650)

b333 = s.Button(booking_frame_3, text="BACK", font="Timesnewromen", width=8, height=2,command=lambda: [payment_to_welcome_2()])
b333.place(x=50, y=650)

# Booking-3 ends------------------------------------------------------------------------------------------------------------------------

# Payment page Starts--------------------------------------------------------------------------------------------------------------------

payment_frame = Frame(window, bg="#023D54")

lo = s.Label(payment_frame, text="PAYMENT METHOD", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lo.place(x=650, y=30)

# DEBIT CARD PIC
image_path = "bg pics/debit card.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame, image=photo)
label.image = photo
label.place(x=275, y=330)
l1 = s.Label(payment_frame, text="1.Debit Card", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=680, y=125)
b1 = s.Button(payment_frame, text="DEBIT CARD", font="Timesnewroman", width=17, height=2,command=lambda: [payment_to_debit()])
b1.place(x=270, y=555)

debit_frame = Frame(window, bg="#023D54")

l1 = s.Label(debit_frame, text="DEBIT CARD", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=730, y=70)

l1 = s.Label(debit_frame, text="ENTER YOUR NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=450, y=200)

debit_name = s.Entry(debit_frame, width=20, font=("Comic Sans MS", 20))
debit_name.place(x=850, y=200)

l2 = s.Label(debit_frame, text="ENTER CARD NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=300)

debit_card_no = s.Entry(debit_frame, font=("Comic Sans MS", 20))
debit_card_no.place(x=850, y=300)

l2 = s.Label(debit_frame, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=400)

debit_amount= s.Entry(debit_frame, font=("Comic Sans MS", 20))
debit_amount.place(x=850, y=400)

def debit():
    Debit_Name = debit_name.get()
    Card_No_1 = debit_card_no.get()
    Amount_1 = debit_amount.get()

    if Debit_Name == "" or Card_No_1 == "" or Amount_1 == "":
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into debit values('" + Debit_Name + "','" + Card_No_1 + "','" + Amount_1 + "')")
        db.commit()
        debit_to_last()

b2 = s.Button(debit_frame, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [debit()])
b2.place(x=720, y=500)

now = str(datetime.now())
l2 = s.Label(debit_frame, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=545, y=600)

# #UPI PAYMENT PIC

image_path = "bg pics/upi payment.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame, image=photo)
label.image = photo
label.place(x=675, y=330)
l2 = s.Label(payment_frame, text="2.UPI Payment", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=680, y=175)
b2 = s.Button(payment_frame, text="UPI", font="Timesnewroman", width=17, height=2, command=lambda: [payment_to_upi()])
b2.place(x=670, y=555)

upi_frame = Frame(window, bg="#023D54")

l1 = s.Label(upi_frame, text="UPI PAYMENT", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=730, y=70)

l1 = s.Label(upi_frame, text="ENTER YOUR NAME ", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=450, y=200)

upi_name = s.Entry(upi_frame, width=20, font=("Comic Sans MS", 20))
upi_name.place(x=850, y=200)

l2 = s.Label(upi_frame, text="ENTER CARD NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=300)

upi_card_no = s.Entry(upi_frame, font=("Comic Sans MS", 20))
upi_card_no.place(x=850, y=300)

l2 = s.Label(upi_frame, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=400)

upi_amount = s.Entry(upi_frame, font=("Comic Sans MS", 20))
upi_amount.place(x=850, y=400)

def upi():
    Upi_Name = upi_name.get()
    Card_No_2 = upi_card_no.get()
    Amount_2 = upi_amount.get()

    if Upi_Name == "" or Card_No_2 == "" or  Amount_2== "" :
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into upi values('" + Upi_Name + "','" + Card_No_2 + "','" + Amount_2 + "')")
        db.commit()
        upi_to_last()

b2 = s.Button(upi_frame, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [upi()])
b2.place(x=720, y=500)

now = str(datetime.now())
l2 = s.Label(upi_frame, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=545, y=600)

# NET BANKING
image_path = "bg pics/net banking.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame, image=photo)
label.image = photo
label.place(x=1075, y=330)
l3 = s.Label(payment_frame, text="3.Net Banking", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=680, y=225)
b2 = s.Button(payment_frame, text="NET BANK", font="Timesnewroman", width=17, height=2,
              command=lambda: [payment_to_net()])
b2.place(x=1070, y=555)

net_frame = Frame(window, bg="#023D54")

l1 = s.Label(net_frame, text="NET BANKING", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=730, y=50)

l1 = s.Label(net_frame, text="ENTER YOUR NAME ", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=400, y=150)

net_name = s.Entry(net_frame, width=20, font=("Comic Sans MS", 20))
net_name.place(x=850, y=150)

l2 = s.Label(net_frame, text="ENTER THE YOUR BANK NAME ", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=400, y=250)

bank_name = s.Entry(net_frame, font=("Comic Sans MS", 20))
bank_name.place(x=850, y=250)

l3 = s.Label(net_frame, text="ENTER THE ACCOUNT NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=400, y=350)

net_account_no = s.Entry(net_frame, font=("Comic Sans MS", 20))
net_account_no.place(x=850, y=350)

l3 = s.Label(net_frame, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=400, y=450)

net_amount = s.Entry(net_frame, font=("Comic Sans MS", 20))
net_amount.place(x=850, y=450)

def net_bank():
    Net_Name = net_name.get()
    Bank_Name = bank_name.get()
    Account_No = net_account_no.get()
    Amount_3 = net_amount.get()

    if Net_Name == "" or Bank_Name  == "" or Account_No == "" or Amount_3 == "":
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into net_bank values('" + Net_Name + "','" + Bank_Name  + "','" + Account_No + "','" + Amount_3 + "')")
        db.commit()
        net_to_last()

b2 = s.Button(net_frame, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [net_bank()])
b2.place(x=720, y=550)

now = str(datetime.now())
l2 = s.Label(net_frame, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=545, y=650)

# Payment Method -2

payment_frame_1 = Frame(window, bg="#023D54")

lo = s.Label(payment_frame_1, text="PAYMENT METHOD", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lo.place(x=650, y=30)

# DEBIT CARD PIC
image_path = "bg pics/debit card.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame_1, image=photo)
label.image = photo
label.place(x=275, y=330)
l1 = s.Label(payment_frame_1, text="1.Debit Card", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=680, y=125)
b1 = s.Button(payment_frame_1, text="DEBIT CARD", font="Timesnewroman", width=17, height=2,command=lambda: [payment_to_debit_1()])
b1.place(x=270, y=555)

debit_frame_1 = Frame(window, bg="#023D54")

l1 = s.Label(debit_frame_1, text="DEBIT CARD", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=700, y=70)

l1 = s.Label(debit_frame_1, text="ENTER YOUR NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=450, y=200)

debit_name_0 = s.Entry(debit_frame_1, width=20, font=("Comic Sans MS", 20))
debit_name_0.place(x=850, y=200)

l2 = s.Label(debit_frame_1, text="ENTER CARD NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=300)

debit_card_no_0 = s.Entry(debit_frame_1, font=("Comic Sans MS", 20))
debit_card_no_0.place(x=850, y=300)

l2 = s.Label(debit_frame_1, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=400)

debit_amount_0= s.Entry(debit_frame_1, font=("Comic Sans MS", 20))
debit_amount_0.place(x=850, y=400)

def debit_1():
    Debit_Name = debit_name_0.get()
    Card_No_1 = debit_card_no_0.get()
    Amount_1 = debit_amount_0.get()

    if Debit_Name == "" or Card_No_1 == "" or Amount_1 == "":
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into debit values('" + Debit_Name + "','" + Card_No_1 + "','" + Amount_1 + "')")
        db.commit()
        debit_to_last_1()

b2 = s.Button(debit_frame_1, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [debit_1()])
b2.place(x=720, y=500)

now = str(datetime.now())
l2 = s.Label(debit_frame_1, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=545, y=600)

# #UPI PAYMENT PIC

image_path = "bg pics/upi payment.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame_1, image=photo)
label.image = photo
label.place(x=675, y=330)
l2 = s.Label(payment_frame_1, text="2.UPI Payment", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=680, y=175)
b2 = s.Button(payment_frame_1, text="UPI", font="Timesnewroman", width=17, height=2, command=lambda: [payment_to_upi_1()])
b2.place(x=670, y=555)

upi_frame_1 = Frame(window, bg="#023D54")

l1 = s.Label(upi_frame_1, text="UPI PAYMENT", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=700, y=70)

l1 = s.Label(upi_frame_1, text="ENTER YOUR NAME ", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=450, y=200)

upi_name_0 = s.Entry(upi_frame_1, width=20, font=("Comic Sans MS", 20))
upi_name_0.place(x=850, y=200)

l2 = s.Label(upi_frame_1, text="ENTER CARD NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=300)

upi_card_no_0 = s.Entry(upi_frame_1, font=("Comic Sans MS", 20))
upi_card_no_0.place(x=850, y=300)

l2 = s.Label(upi_frame_1, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=400)

upi_amount_0 = s.Entry(upi_frame_1, font=("Comic Sans MS", 20))
upi_amount_0.place(x=850, y=400)

def upi_1():
    Upi_Name = upi_name_0.get()
    Card_No_2 = upi_card_no_0.get()
    Amount_2 = upi_amount_0.get()

    if Upi_Name == "" or Card_No_2 == "" or  Amount_2== "" :
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into upi values('" + Upi_Name + "','" + Card_No_2 + "','" + Amount_2 + "')")
        db.commit()
        upi_to_last_1()

b2 = s.Button(upi_frame_1, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [upi_1()])
b2.place(x=720, y=500)

now = str(datetime.now())
l2 = s.Label(upi_frame_1, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=545, y=600)

# NET BANKING
image_path = "bg pics/net banking.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame_1, image=photo)
label.image = photo
label.place(x=1075, y=330)
l3 = s.Label(payment_frame_1, text="3.Net Banking", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=680, y=225)
b2 = s.Button(payment_frame_1, text="NET BANK", font="Timesnewroman", width=17, height=2,
              command=lambda: [payment_to_net_1()])
b2.place(x=1070, y=555)

net_frame_1 = Frame(window, bg="#023D54")

l1 = s.Label(net_frame_1, text="NET BANKING", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=700, y=50)

l1 = s.Label(net_frame_1, text="ENTER YOUR NAME ", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=400, y=150)

net_name_0 = s.Entry(net_frame_1, width=20, font=("Comic Sans MS", 20))
net_name_0.place(x=850, y=150)

l2 = s.Label(net_frame_1, text="ENTER THE YOUR BANK NAME ", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=400, y=250)

bank_name_0 = s.Entry(net_frame_1, font=("Comic Sans MS", 20))
bank_name_0.place(x=850, y=250)

l3 = s.Label(net_frame_1, text="ENTER THE ACCOUNT NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=400, y=350)

net_account_no_0 = s.Entry(net_frame_1, font=("Comic Sans MS", 20))
net_account_no_0.place(x=850, y=350)

l3 = s.Label(net_frame_1, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=400, y=450)

net_amount_0 = s.Entry(net_frame_1, font=("Comic Sans MS", 20))
net_amount_0.place(x=850, y=450)

def net_bank_1():
    Net_Name = net_name_0.get()
    Bank_Name = bank_name_0.get()
    Account_No = net_account_no_0.get()
    Amount_3 = net_amount_0.get()


    if Net_Name == "" or Bank_Name  == "" or Account_No == "" or Amount_3 == "":
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into net_bank values('" + Net_Name + "','" + Bank_Name  + "','" + Account_No + "','" + Amount_3 + "')")
        db.commit()
        net_to_last_1()

b2 = s.Button(net_frame_1, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [net_bank_1()])
b2.place(x=720, y=550)

now = str(datetime.now())
l2 = s.Label(net_frame_1, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=545, y=650)

# Payment Method -3

payment_frame_2 = Frame(window, bg="#023D54")

lo = s.Label(payment_frame_2, text="PAYMENT METHOD", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
lo.place(x=650, y=30)

# DEBIT CARD PIC
image_path = "bg pics/debit card.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame_2, image=photo)
label.image = photo
label.place(x=275, y=330)
l1 = s.Label(payment_frame_2, text="1.Debit Card", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=680, y=125)
b1 = s.Button(payment_frame_2, text="DEBIT CARD", font="Timesnewroman", width=17, height=2,
              command=lambda: [payment_to_debit_2()])
b1.place(x=270, y=555)

debit_frame_2 = Frame(window, bg="#023D54")

l1 = s.Label(debit_frame_2, text="DEBIT CARD", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=700, y=70)

l1 = s.Label(debit_frame_2, text="ENTER YOUR NAME", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=450, y=200)

debit_name_1 = s.Entry(debit_frame_2, width=20, font=("Comic Sans MS", 20))
debit_name_1.place(x=850, y=200)

l2 = s.Label(debit_frame_2, text="ENTER CARD NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=300)

debit_card_no_1 = s.Entry(debit_frame_2, font=("Comic Sans MS", 20))
debit_card_no_1.place(x=850, y=300)

l2 = s.Label(debit_frame_2, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=400)

debit_amount_1= s.Entry(debit_frame_2, font=("Comic Sans MS", 20))
debit_amount_1.place(x=850, y=400)

def debit_2():
    Debit_Name = debit_name_1.get()
    Card_No_1 = debit_card_no_1.get()
    Amount_1 = debit_amount_1.get()

    if Debit_Name == "" or Card_No_1 == "" or Amount_1 == "":
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into debit values('" + Debit_Name + "','" + Card_No_1 + "','" + Amount_1 + "')")
        db.commit()
        debit_to_last_2()

b2 = s.Button(debit_frame_2, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [debit_2()])
b2.place(x=720, y=500)

now = str(datetime.now())
l2 = s.Label(debit_frame_2, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=545, y=600)

# #UPI PAYMENT PIC

image_path = "bg pics/upi payment.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame_2, image=photo)
label.image = photo
label.place(x=675, y=330)
l2 = s.Label(payment_frame_2, text="2.UPI Payment", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=680, y=175)
b2 = s.Button(payment_frame_2, text="UPI", font="Timesnewroman", width=17, height=2, command=lambda: [payment_to_upi_2()])
b2.place(x=670, y=555)

upi_frame_2 = Frame(window, bg="#023D54")

l1 = s.Label(upi_frame_2, text="UPI PAYMENT", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=700, y=70)

l1 = s.Label(upi_frame_2, text="ENTER YOUR NAME ", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=450, y=200)

upi_name_1 = s.Entry(upi_frame_2, width=20, font=("Comic Sans MS", 20))
upi_name_1.place(x=850, y=200)

l2 = s.Label(upi_frame_2, text="ENTER CARD NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=300)

upi_card_no_1 = s.Entry(upi_frame_2, font=("Comic Sans MS", 20))
upi_card_no_1.place(x=850, y=300)

l2 = s.Label(upi_frame_2, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=450, y=400)

upi_amount_1 = s.Entry(upi_frame_2, font=("Comic Sans MS", 20))
upi_amount_1.place(x=850, y=400)

def upi_2():
    Upi_Name = upi_name_1.get()
    Card_No_2 = upi_card_no_1.get()
    Amount_2 = upi_amount_1.get()

    if Upi_Name == "" or Card_No_2 == "" or  Amount_2== "" :
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into upi values('" + Upi_Name + "','" + Card_No_2 + "','" + Amount_2 + "')")
        db.commit()
        upi_to_last_2()

b2 = s.Button(upi_frame_2, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [upi_2()])
b2.place(x=720, y=500)

now = str(datetime.now())
l2 = s.Label(upi_frame_2, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=545, y=600)

# NET BANKING
image_path = "bg pics/net banking.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(payment_frame_2, image=photo)
label.image = photo
label.place(x=1075, y=330)
l3 = s.Label(payment_frame_2, text="3.Net Banking", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=680, y=225)
b2 = s.Button(payment_frame_2, text="NET BANK", font="Timesnewroman", width=17, height=2,
              command=lambda: [payment_to_net_2()])
b2.place(x=1070, y=555)

net_frame_2 = Frame(window, bg="#023D54")

l1 = s.Label(net_frame_2, text="NET BANKING", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=700, y=50)

l1 = s.Label(net_frame_2, text="ENTER YOUR NAME ", bg="#023D54", fg="white", font=("Comic Sans MS", 20,))
l1.place(x=400, y=150)

net_name_1 = s.Entry(net_frame_2, width=20, font=("Comic Sans MS", 20))
net_name_1.place(x=850, y=150)

l2 = s.Label(net_frame_2, text="ENTER THE YOUR BANK NAME ", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l2.place(x=400, y=250)

bank_name_1 = s.Entry(net_frame_2, font=("Comic Sans MS", 20))
bank_name_1.place(x=850, y=250)

l3 = s.Label(net_frame_2, text="ENTER THE ACCOUNT NUMBER", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=400, y=350)

net_account_no_1 = s.Entry(net_frame_2, font=("Comic Sans MS", 20))
net_account_no_1.place(x=850, y=350)

l3 = s.Label(net_frame_2, text="ENTER THE AMOUNT", bg="#023D54", fg="white", font=("Comic Sans MS", 20))
l3.place(x=400, y=450)

net_amount_1 = s.Entry(net_frame_2, font=("Comic Sans MS", 20))
net_amount_1.place(x=850, y=450)

def net_bank_2():
    Net_Name = net_name_1.get()
    Bank_Name = bank_name_1.get()
    Account_No = net_account_no_1.get()
    Amount_3 = net_amount_1.get()

    if Net_Name == "" or Bank_Name  == "" or Account_No == "" or Amount_3 == "":
        messagebox.showerror("error", "Fill the details")
    else:
        messagebox.showinfo("submit", "Your Details Saved Success Fully")
        db = m.connect(host="localhost", user="root", password="K@rthi16", db="python")
        cur = db.cursor()
        cur.execute("insert into net_bank values('" + Net_Name + "','" + Bank_Name  + "','" + Account_No + "','" + Amount_3 + "')")
        db.commit()
        net_to_last_2()


b2 = s.Button(net_frame_2, text="SUBMIT", font="Timesnewroman", width=17, height=2, command=lambda: [net_bank_2()])
b2.place(x=720, y=550)

now = str(datetime.now())
l2 = s.Label(net_frame_2, text="YOU BOOKED THE TICKET AT " + now, bg="#023D54", fg="white", font=("Comic Sans MS", 15))
l2.place(x=545, y=650)

# Last Frame It is used as a common frame

last_frame = Frame(window, bg="#023D54")
image_path = "bg pics/z last page.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = s.Label(last_frame, image=photo)
label.image = photo
label.place(x=300, y=150)

b4 = s.Button(payment_frame, text="BACK", font="Timesnewromen", width=8, height=2, command=lambda: [payment_to_book()])
b4.place(x=50, y=650)

b5 = s.Button(payment_frame_1, text="BACK", font="Timesnewromen", width=8, height=2, command=lambda: [payment_to_book_1()])
b5.place(x=50, y=650)

b6 = s.Button(payment_frame_2, text="BACK", font="Timesnewromen", width=8, height=2, command=lambda: [payment_to_book_2()])
b6.place(x=50, y=650)

window.mainloop()