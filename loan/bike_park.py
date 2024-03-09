import tkinter
from sqlite3 import Connection
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import customtkinter
from tkcalendar import DateEntry
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkFrame, CTkScrollableFrame, CTkImage, CTkTabview, \
    AppearanceModeTracker

# base page
def Base_Page():
    global root
    root = Tk()
    root.config(bg='#272727')
    root.title("Welcome")
    height = 400
    width = 600
    x = (root.winfo_screenwidth() / 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # root.overrideredirect(True)
    #Main frame
    base_frame=CTkFrame(root,width=600,height=400,corner_radius=0,fg_color='#e6f0ff')
    base_frame.pack(padx=0,pady=0)
    #Leftside frame
    left_side=CTkFrame(base_frame,width=300,height=400,corner_radius=0,fg_color='#F8F8F8')
    left_side.place(x=0,y=0)
    image = PhotoImage(file="Welcome.png")
    side_image = Label(left_side, image=image)
    side_image.place(x=60,y=110)

    #Base Action contain
    Base_Action=CTkFrame(base_frame,width=300,height=400,corner_radius=0,fg_color='#3385ff')
    Base_Action.place(x=300,y=0)
    PMS = Label(Base_Action,text="Bike Park Management", bg="#3385ff", fg="white", font=("Trebuchet Ms", 15, "bold"))
    PMS.place(x=25, y=30)
    icon1 = PhotoImage(file="Login.png")
    Log = Label(Base_Action, image=icon1)
    Login_Button = CTkButton(Base_Action, text="Login", font=("Times New Roman", 18), command=login, corner_radius=20)
    icon2 = PhotoImage(file="Picture1.png")
    NUsr = Label(Base_Action, image=icon2)
    NewUser_Button = CTkButton(Base_Action, text="Register", font=("Times New Roman", 18), command=BptoNu, corner_radius=20)
    Log.place(x=50, y=100)
    Login_Button.place(x=150, y=120)
    NUsr.place(x=50, y=200)
    NewUser_Button.place(x=150, y=220)

    root.resizable(False, False)
    root.mainloop()


# login windows
def Login_Page():
    global Login_GUI
    Login_GUI = Tk()
    Login_GUI.title("Login")
    Login_GUI.config(bg='#272727')
    height = 400
    width = 600
    x = (Login_GUI.winfo_screenwidth() / 2) - (width // 2)
    y = (Login_GUI.winfo_screenheight() // 2) - (height // 2)
    Login_GUI.geometry("%dx%d+%d+%d" % (width, height, x, y))
    frame = customtkinter.CTkFrame(master=Login_GUI, width=600, height=400, bg_color="#272727", corner_radius=0)
    frame.place(x=0,y=0)

    #right side frame
    right_side_frame=CTkFrame(frame,width=300,height=400,corner_radius=0,fg_color='#F8F8F8')
    right_side_frame.place(x=0,y=0)
    image = PhotoImage(file="Welcome.png")
    side_image = Label(right_side_frame, image=image)
    side_image.place(x=60, y=110)

    #left side frame
    left_side_frame=CTkFrame(frame,width=300,height=400,corner_radius=0,fg_color='#3385ff')
    left_side_frame.place(x=300)
    PMS = CTkLabel(left_side_frame, text="Welcome back ", font=("Helvetica", 20),text_color='#DCDCDC')
    PMS.place(x=50, y=45)

    lab1 = CTkLabel(left_side_frame, text="Email", padx=14, pady=5, font=("Times New Roman", 18),text_color='#DCDCDC')
    lab2 = CTkLabel(left_side_frame, text="Password", padx=14, pady=5, font=("Times New Roman", 18),text_color='#DCDCDC')
    lab3 = CTkLabel(left_side_frame, text="\n", font=("Times New Roman", 18))
    global email
    global Password
    email = CTkEntry(left_side_frame, font=("Times New Roman", 14), width=220, placeholder_text='Enter your Email',
                     placeholder_text_color='gray', corner_radius=8)
    Password = CTkEntry(left_side_frame, show="*", font=("Times New Roman", 14), width=220,
                        placeholder_text='Enter your Password', placeholder_text_color='gray', corner_radius=8)
    Login_Button = CTkButton(left_side_frame, text=" Login  ", command=validate, width=90, font=("Times New Roman", 14),
                             corner_radius=50)
    NewUser_Button = CTkButton(left_side_frame, text="Register", command=LptoNu, width=90, font=("Times New Roman", 14),
                               corner_radius=50)

    lab1.place(x=40, y=120)
    email.place(x=50, y=150)
    lab2.place(x=40, y=180)
    Password.place(x=50, y=210)
    lab3.place(x=0, y=210)
    Login_Button.place(x=50, y=260)
    NewUser_Button.place(x=170, y=260)
    Login_GUI.mainloop()

def login():
    root.destroy()
    Login_Page()

def LptoNu():
    Login_GUI.destroy()
    register_Page()


def BptoNu():
    root.destroy()
    register_Page()


# login validation function
def validate():
    c = 0
    conn = sqlite3.connect('riders_data.db')
    cursor = conn.execute("SELECT email,password,user_role,first_name FROM riders")
    for row in cursor:
        if (str(email.get()) == row[0]) and (str(Password.get()) == row[1]):
            c = 1
            break
        else:
            c = 0
    if c == 1:
        if row[2] == 'rider':
            messagebox.showinfo("Status", "Login Successfully " + row[3])
            User_Page()
        elif row[2] == 'employee':
            messagebox.showinfo("Status", "Login Successfully" + row[3])
            Dashboard_page()
        else:
            c = 0
    if c == 0:
        messagebox.showinfo("Status", "Login Failed.\nPlease Try Again")
    conn.commit()


#
def register_Page():
    global register_ui
    register_ui = Tk()
    register_ui.title("Register")
    register_ui.config(bg='#272727')
    height = 550
    width = 800
    x = (register_ui.winfo_screenwidth() / 2) - (width // 2)
    y = (register_ui.winfo_screenheight() // 2) - (height // 2)
    w, h = register_ui.winfo_screenwidth(), register_ui.winfo_screenheight()
    register_ui.geometry("%dx%d+%d+%d" % (width, height, x, y))

    #Main frame
    frame = CTkFrame(master=register_ui, width=800, height=550, corner_radius=0)
    frame.place(x=0, y=0)

    #right side frame
    right_side_frame=CTkFrame(frame,width=800,height=550,corner_radius=0,fg_color='#F8F8F8')
    right_side_frame.place(x=0,y=0)
    image = PhotoImage(file="Welcome.png")
    side_image = Label(right_side_frame, image=image)
    side_image.place(x=80, y=220)

    #left side frame
    left_side_frame=CTkFrame(frame,width=400,height=550,corner_radius=0,fg_color='#3385ff')
    left_side_frame.place(x=400,y=0)
    PMS = CTkLabel(left_side_frame, text="Register ", font=("Helvetica", 20), padx=20, pady=20,text_color='#D3D3D3')
    PMS.place(x=80, y=20)

    lab1 = CTkLabel(left_side_frame, text="First name", padx=10, pady=5, font=("Times New Roman", 18))
    lab2 = CTkLabel(left_side_frame, text="Street", padx=10, pady=5, font=("Times New Roman", 18))
    lab3 = CTkLabel(left_side_frame, text="City", padx=10, pady=5, font=("Times New Roman", 18))
    lab4 = CTkLabel(left_side_frame, text="Gender", padx=10, pady=5, font=("Times New Roman", 18))
    lab5 = CTkLabel(left_side_frame, text="Mobile", padx=10, pady=5, font=("Times New Roman", 18))
    lab6 = CTkLabel(left_side_frame, text="Email ", padx=10, pady=5, font=("Times New Roman", 18))
    lab7 = CTkLabel(left_side_frame, text="Last name", padx=10, pady=5, font=("Times New Roman", 18))
    lab8 = CTkLabel(left_side_frame, text="Password", padx=10, pady=5, font=("Times New Roman", 18))
    dob_label = CTkLabel(left_side_frame, text="Dirt of birth", padx=10, pady=5, font=("Times New Roman", 18))

    #feild variables
    global first_name
    global Street
    global City
    global Mobile
    global Dob
    global Email
    global lastname
    global user_role
    global Pass
    first_name = CTkEntry(left_side_frame, font=("Times New Roman", 14), placeholder_text='first name',
                          placeholder_text_color='gray', corner_radius=8)
    Street = CTkEntry(left_side_frame, font=("Times New Roman", 14), placeholder_text='Street',
                      placeholder_text_color='gray', corner_radius=8)
    City = CTkEntry(left_side_frame, font=("Times New Roman", 14), placeholder_text='City', placeholder_text_color='gray',
                    corner_radius=8)
    user_role = 'rider'
    global Gender
    Gender = StringVar()
    G1 = Radiobutton(left_side_frame, text="M", variable=Gender, value="Male", font=("Times New Roman", 14))
    G2 = Radiobutton(left_side_frame, text="F", variable=Gender, value="Female", font=("Times New Roman", 14))
    Dob = DateEntry(left_side_frame, font=("Times New Roman", 14), placeholder_text='mobile number',
                    placeholder_text_color='gray', corner_radius=8)
    Mobile = CTkEntry(left_side_frame, font=("Times New Roman", 14), placeholder_text='mobile number',
                      placeholder_text_color='gray', corner_radius=8)
    Email = CTkEntry(left_side_frame, font=("Times New Roman", 14), placeholder_text=' Email',
                     placeholder_text_color='gray', corner_radius=8)
    lastname = CTkEntry(left_side_frame, font=("Times New Roman", 14), placeholder_text='Last name',
                        placeholder_text_color='gray', corner_radius=8)
    Pass = CTkEntry(left_side_frame, font=("Times New Roman", 14), placeholder_text='Create password',
                    placeholder_text_color='gray', corner_radius=8)
    lab1.place(x=50, y=120)
    lab2.place(x=50, y=200)
    lab3.place(x=250, y=200)
    lab4.place(x=50, y=260)
    lab5.place(x=50, y=330)
    lab6.place(x=250, y=330)
    lab7.place(x=250, y=120)
    lab8.place(x=50, y=390)
    dob_label.place(x=240, y=260)
    first_name.place(x=50, y=160)
    lastname.place(x=250, y=160)
    Street.place(x=50, y=230)
    City.place(x=250, y=230)
    G1.place(x=50, y=290)
    G2.place(x=100, y=290)
    Dob.place(x=250, y=290)
    Mobile.place(x=50, y=360)
    Email.place(x=250, y=360)
    Pass.place(x=50, y=420)

    lab10 = CTkLabel(left_side_frame, text="", font=("Times New Roman", 28))
    lab10.place(x=10, y=490)
    Submit_Button = CTkButton(left_side_frame, text="Register", command=DB_Reg, font=("Times New Roman", 18),
                              corner_radius=50)
    Submit_Button.place(x=250, y=415)
    back_Button = CTkButton(left_side_frame, text="Go back", command= goback, font=("Times New Roman", 18),
                            corner_radius=20)
    back_Button.place(x=250, y=460)
    register_ui.resizable(False, False)
    register_ui.mainloop()


def goback():
    register_ui.destroy()
    Login_Page()


def DB_Reg():
    dbid = str(Mobile.get())
    dbfirstName = str(first_name.get())
    dbuserrole = str(user_role)
    dbstreet = str(Street.get())
    dbcity = str(City.get())
    dbMobile = str(Mobile.get())
    dbdob = str(Dob.get())
    dbGender = str(Gender.get())
    dbEmail = str(Email.get())
    dblastName = str(lastname.get())
    dbPassword = str(Pass.get())

    conn = sqlite3.connect('riders_data.db')
    cursor = conn.execute(
        "INSERT INTO riders (id,email,password,first_name,last_name,city,dob,mobile,gender,street,user_role) VALUES ("
        "?,?,?,?,?,?,?,?,?,?,?)",
        ( dbid,dbEmail, dbPassword, dbfirstName, dblastName, dbcity, dbdob, dbMobile, dbGender, dbstreet, dbuserrole))
    conn.commit()
    messagebox.showinfo("Status", "Successfully Registered .Welcome \nUse the email & Password to Login")
    register_ui.destroy()
    Base_Page()

#Employee home page
def Dashboard_page():
    Login_GUI.destroy()
    Dashboard_UI = Tk()
    Dashboard_UI.title("Admin Dashboard")
    Dashboard_UI.config(bg='#272727')
    # Main frame
    Admin_dashboard = CTkScrollableFrame(Dashboard_UI, corner_radius=0, width=1380, height=700)
    Admin_dashboard.pack(pady=0)
    Admin_dashboard.config(width=1380, height=700)
    w, h = Dashboard_UI.winfo_screenwidth(), Dashboard_UI.winfo_screenheight()
    Dashboard_UI.geometry("%dx%d+0+0" % (w, h))

    # right sidebar frame
    right_sidebar = CTkFrame(Admin_dashboard, corner_radius=20, border_width=1, border_color='#B8B8B8',fg_color='#00ace6', width=500,height=700)
    right_sidebar.place(x=850, y=100)

    #right sidebar content
    right_lable = CTkLabel(right_sidebar, text="Rented Equipment",text_color='#DCDCDC', font=("Times New Roman", 18), padx=5, pady=5)
    right_lable.place(x=10, y=10)
    # Treeview of
    style = ttk.Style(right_sidebar)
    style.theme_use('clam')
    style.configure('Treeview', font=('Roboto', 14))
    style.map('Treeview', background=[('selected', '#00ace6')])
    tree = ttk.Treeview(right_sidebar, height=15)
    tree['columns'] = ('Name', 'email', 'Item','Qty','Sale date')

    # Columns
    tree.column('#0', width=0, stretch=tkinter.NO)
    tree.column('Name', anchor=tkinter.CENTER, width=50)
    tree.column('email', anchor=tkinter.CENTER, width=160)
    tree.column('Item', anchor=tkinter.CENTER, width=100)
    tree.column('Qty', anchor=tkinter.CENTER, width=50)
    tree.column('Sale date', anchor=tkinter.CENTER, width=100)
    # heading
    tree.heading('Name', text='Name')
    tree.heading('email', text='email')
    tree.heading('Item', text='Item')
    tree.heading('Qty', text='Qty')
    tree.heading('Sale date', text='Sale date')
    # data query
    conn = sqlite3.connect('riders_data.db')
    u = conn.cursor()
    u.execute("SELECT* FROM sales")
    sales = u.fetchall()
    for sale in sales:
        tree.insert('', 'end',
                    values=(sale[2], sale[4], sale[7],sale[8],sale[9]))
        conn.close()
    tree.place(x=20, y=80)

    # left sidebar frame
    sidebar = CTkFrame(Admin_dashboard, corner_radius=20, border_width=1, border_color='#B8B8B8', width=250, height=700,fg_color='#00ace6')
    sidebar.place(x=10, y=100)
    #Treeview of
    style = ttk.Style(sidebar)
    style.theme_use('clam')
    style.configure('Treeview', font=('Roboto', 14))
    style.map('Treeview', background=[('selected', '#00ace6')])
    tree = ttk.Treeview(sidebar, height=15)
    tree['columns'] = ('No', 'Item', 'Qty')

    # Columns
    tree.column('#0', width=0, stretch=tkinter.NO)
    tree.column('No', anchor=tkinter.CENTER, width=50)
    tree.column('Item', anchor=tkinter.CENTER, width=100)
    tree.column('Qty', anchor=tkinter.CENTER, width=50)

    # heading
    tree.heading('No', text='No')
    tree.heading('Item', text='Item')
    tree.heading('Qty', text='Qty')
    # data query
    conn = sqlite3.connect('riders_data.db')
    u = conn.cursor()
    u.execute("SELECT* FROM equipments")
    riders = u.fetchall()
    for rider in riders:
        tree.insert('', 'end',
                    values=(rider[0], rider[1], rider[2]))
        conn.close()
    tree.place(x=10, y=80)

    Y = CTkLabel(sidebar, text="Equipments.",text_color='#DCDCDC', font=("Times New Roman", 22), padx=5, pady=5)
    Y.place(x=5, y=10)
    Add_equipement = CTkButton(sidebar, text="Add", corner_radius=20, width=50, height=20, font=("Times New Roman", 14),command=add_equipment_Page)
    Add_equipement.place(x=150, y=18)

    # navigation bar
    navibar_frame = CTkFrame(Admin_dashboard, corner_radius=0, width=1380, height=80, fg_color='#00ace6')
    navibar_frame.place(x=0, y=0)
    # main Content for available Equipment
    Text_Logo = CTkLabel(navibar_frame, text='Bike park', text_color='#FFFFFF',
                         font=('Roboto', 23, 'bold'))
    Text_Logo.place(x=10, y=20)
    search_bar = CTkEntry(navibar_frame, placeholder_text='Search here..', border_width=1, border_color='#F8F8F8',
                          font=('Roboto', 12),
                          placeholder_text_color='#888888', width=300, height=30, corner_radius=20,
                          )
    #Navigation item
    Employee_Button = CTkButton(navibar_frame, text="Employees", corner_radius=50, width=100, height=30,
                                   font=("Times New Roman", 14), command=Employees_page)
    User_Button = CTkButton(navibar_frame, text="Users", corner_radius=50, width=100, height=30,
                              font=("Times New Roman", 14), command= Users_page)
    Logout_Button = CTkButton(navibar_frame, text="Logout", font=("Times New Roman", 14), corner_radius=50, width=100,
                              height=30, command=UptoBp)
    Employee_Button.place(x=950, y=25)
    User_Button.place(x=1090, y=25)
    Logout_Button.place(x=1230, y=25)

    # main content frame
    main_screen = CTkFrame(Admin_dashboard, width=550, height=700)
    main_screen.place(x=260, y=100)
    Y = CTkLabel(main_screen, text="Bike Bookings.", font=("Times New Roman", 22), padx=5, pady=5)
    Y.place(x=5, y=10)

    # Treeview of
    style = ttk.Style(main_screen)
    style.theme_use('clam')
    style.configure('Treeview', font=('Roboto', 14))
    style.map('Treeview', background=[('selected', '#00ace6')])
    tree = ttk.Treeview(main_screen, height=15)
    tree['columns'] = ('First Name', 'Last_name', 'Booking Date', 'Contact','Postcode')

    # Columns
    tree.column('#0', width=0, stretch=tkinter.NO)
    tree.column('First Name', anchor=tkinter.CENTER, width=100)
    tree.column('Last_name', anchor=tkinter.CENTER, width=100)
    tree.column('Booking Date', anchor=tkinter.CENTER, width=100)
    tree.column('Contact', anchor=tkinter.CENTER, width=140)
    tree.column('Postcode', anchor=tkinter.CENTER, width=80)
    # heading
    tree.heading('First Name', text='First Name')
    tree.heading('Last_name', text='Last_name')
    tree.heading('Booking Date', text='Booking Date')
    tree.heading('Contact', text='Contact')
    tree.heading('Postcode', text='Postcode')
    # data query
    conn = sqlite3.connect('riders_data.db')
    u = conn.cursor()
    u.execute("SELECT* FROM bookings")
    bookings = u.fetchall()
    for booking in bookings:
        tree.insert('', 'end',
                    values=( booking[2], booking[3], booking[5], booking[6], booking[7]))
        conn.close()
    tree.place(x=10, y=60)

    Dashboard_UI.mainloop()


def Employees_page():
    global Employee_ui
    Employee_ui=Tk()
    Employee_ui.title("Employee Activities")
    Employee_frame=CTkFrame(Employee_ui,width=1380,height=700,corner_radius=0)
    Employee_frame.pack(pady=0)
    #Add employee
    right_frame=CTkFrame(Employee_frame,width=260,height=680,border_width=1,border_color='#DCDCDC',fg_color='#00ace6')
    right_frame.place(x=5,y=5)

    PMS = CTkLabel(right_frame, text="Add new Employee", font=("Helvetica", 18), padx=10, pady=10, text_color='#D3D3D3')
    lab1 = CTkLabel(right_frame, text="First name", padx=10, pady=5, font=("Times New Roman", 14))
    lab2 = CTkLabel(right_frame, text="Street", padx=10, pady=5, font=("Times New Roman", 14))
    lab3 = CTkLabel(right_frame, text="City", padx=10, pady=5, font=("Times New Roman", 14))
    lab4 = CTkLabel(right_frame, text="Gender", padx=10, pady=5, font=("Times New Roman", 14))
    lab5 = CTkLabel(right_frame, text="Mobile", padx=10, pady=5, font=("Times New Roman", 14))
    lab6 = CTkLabel(right_frame, text="Email ", padx=10, pady=5, font=("Times New Roman", 14))
    lab7 = CTkLabel(right_frame, text="Last name", padx=10, pady=5, font=("Times New Roman", 14))
    lab8 = CTkLabel(right_frame, text="Password", padx=10, pady=5, font=("Times New Roman", 14))
    dob_label = CTkLabel(right_frame, text="Dirt of birth", padx=10, pady=5, font=("Times New Roman", 14))

    # feild variables
    global first_name
    global Street
    global City
    global Mobile
    global Dob
    global Email
    global lastname
    global user_role
    global Pass
    global Gender
    first_name = CTkEntry(right_frame, font=("Times New Roman", 14), placeholder_text='first name',
                          placeholder_text_color='gray', corner_radius=8,width=100)
    Street = CTkEntry(right_frame, font=("Times New Roman", 14), placeholder_text='Street',
                      placeholder_text_color='gray', corner_radius=8,width=100)
    City = CTkEntry(right_frame, font=("Times New Roman", 14), placeholder_text='City',
                    placeholder_text_color='gray',
                    corner_radius=8,width=100)
    user_role = 'employee'
    Gender = StringVar()
    G1 = Radiobutton(right_frame, text="M", variable=Gender, value="Male", font=("Times New Roman", 14))
    G2 = Radiobutton(right_frame, text="F", variable=Gender, value="Female", font=("Times New Roman", 14))
    Dob = DateEntry(right_frame, font=("Times New Roman", 14), placeholder_text='mobile number',
                    placeholder_text_color='gray', corner_radius=8)
    Mobile = CTkEntry(right_frame, font=("Times New Roman", 14), placeholder_text='mobile number',
                      placeholder_text_color='gray', corner_radius=8,width=100)
    Email = CTkEntry(right_frame, font=("Times New Roman", 14), placeholder_text=' Email',
                     placeholder_text_color='gray', corner_radius=8,width=100)
    lastname = CTkEntry(right_frame, font=("Times New Roman", 14), placeholder_text='Last name',
                        placeholder_text_color='gray', corner_radius=8,width=100)
    Pass = CTkEntry(right_frame, font=("Times New Roman", 14), placeholder_text='Create password',
                    placeholder_text_color='gray', corner_radius=8,width=100)
    PMS.place(x=10, y=2)
    lab1.place(x=10, y=50)
    lab2.place(x=10, y=140)
    lab3.place(x=130, y=140)
    lab4.place(x=10, y=200)
    lab5.place(x=10, y=270)
    lab6.place(x=130, y=270)
    lab7.place(x=130, y=60)
    lab8.place(x=10, y=330)
    dob_label.place(x=10, y=200)
    first_name.place(x=10, y=100)
    lastname.place(x=130, y=100)
    Street.place(x=10, y=170)
    City.place(x=130, y=170)
    G1.place(x=10, y=230)
    G2.place(x=60, y=230)
    Dob.place(x=130, y=230)
    Mobile.place(x=10, y=300)
    Email.place(x=130, y=300)
    Pass.place(x=10, y=360)

    Submit_Button = CTkButton(right_frame, text="Add", command=DB_Reg, font=("Times New Roman", 14),
                              corner_radius=50,width=100)
    Submit_Button.place(x=140, y=360)

    #Scheduling
    scheduling_frame=CTkFrame(right_frame,width=250, height=260,border_width=1)
    scheduling_frame.place(x=5,y=410)
    global is_on_duty
    global start_time
    global end_time
    global email_Id

    Schedule_label=CTkLabel(scheduling_frame,text='Employee schedule')
    Schedule_label.place(x=10,y=5)
    email_Id=CTkEntry(scheduling_frame, placeholder_text='Email ', width=200)
    is_on_duty=CTkEntry(scheduling_frame,placeholder_text='On dute',width=200)
    start_time=CTkEntry(scheduling_frame,placeholder_text='Start time',width=200)
    end_time = CTkEntry(scheduling_frame, placeholder_text='End time', width=200)
    Update_button=CTkButton(scheduling_frame,text='Update',corner_radius=20,width=80,command=shift_Reg)
    Delete_button = CTkButton(scheduling_frame, text='Delete', corner_radius=20, width=80, command=Delete)
    email_Id.place(x=10, y=50)
    is_on_duty.place(x=10,y=90)
    start_time.place(x=10,y=130)
    end_time.place(x=10, y=180)
    Update_button.place(x=10,y=220)
    Delete_button.place(x=130, y=220)



    #Employee list
    main_flame=CTkFrame(Employee_frame,width=1130,height=680,border_width=1,border_color='#DCDCDC')
    main_flame.place(x=265,y=5)

    style=ttk.Style(main_flame)
    style.theme_use('clam')
    style.configure('Treeview',font=('Roboto',14))
    style.map('Treeview',background=[('selected','#00ace6')])
    tree=ttk.Treeview(main_flame,height=15)
    tree['columns']=('First Name','Last Name','Email','Password','User role','On Duty','Start time','End time')

    #Columns
    tree.column('#0',width=0,stretch=tkinter.NO)
    tree.column('First Name', anchor=tkinter.CENTER, width=120)
    tree.column('Last Name', anchor=tkinter.CENTER, width=120)
    tree.column('Email', anchor=tkinter.CENTER, width=160)
    tree.column('Password', anchor=tkinter.CENTER, width=160)
    tree.column('User role', anchor=tkinter.CENTER, width=120)
    tree.column('On Duty', anchor=tkinter.CENTER, width=80)
    tree.column('Start time', anchor=tkinter.CENTER, width=160)
    tree.column('End time', anchor=tkinter.CENTER, width=160)
#heading
    tree.heading('First Name',text='First Name')
    tree.heading('Last Name',text='Name')
    tree.heading('Email', text='Email')
    tree.heading('Password',text='Password')
    tree.heading('User role',text='User role')
    tree.heading('On Duty', text='On Duty')
    tree.heading('Start time', text='Start time')
    tree.heading('End time', text='End time')
    # data query
    conn = sqlite3.connect('riders_data.db')
    u = conn.cursor()
    u.execute("SELECT*FROM riders WHERE user_role='employee'")
    riders = u.fetchall()
    for rider in riders:
        tree.insert('','end', values=(rider[1],rider[2],rider[3],rider[8],rider[9],rider[13],rider[14],rider[15]))
        conn.close()

    tree.place(x=2,y=10)

    Employee_ui.resizable(False,False)
    Employee_ui.mainloop()






#Shift updating
def shift_Reg():
    dbId=str(email_Id.get())
    dbonDuty = str(is_on_duty.get())
    dbstart_time = str(start_time.get())
    dbend_time = str(end_time.get())
    #Database connection
    conn = sqlite3.connect('riders_data.db')
    cursor=conn.cursor()
    cursor.execute('UPDATE riders SET is_on_duty = ?,start_time = ?,end_time = ? WHERE Id=?',(dbonDuty,dbstart_time,dbend_time,dbId,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Status", "Successfully Updated .")
    Employee_ui.destroy()
    Employees_page()

#Delete employee
def Delete(email_Id):
    #dbId=str(email_Id.get())
    conn = sqlite3.connect('riders_data.db')
    cursor=conn.cursor()
    cursor.execute('DELETE FROM riders WHERE email = ?',(dbId,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Status", "Data Deleted successfully.")
    Employee_ui.destroy()
    Employees_page()


#Riders home page
def Users_page():
    global Users_ui
    global Id_entry
    Users_ui=Tk()
    Users_ui.title("Users")
    Users_frame=CTkScrollableFrame(Users_ui,width=1300,height=800,fg_color='#00ace6')
    Users_frame.pack(padx=5,pady=5)
    right_frame = CTkFrame(Users_frame, width=1300, height=780, border_width=1, border_color='#DCDCDC')
    right_frame.pack(padx=5, pady=5)

    Id_entry=CTkEntry(right_frame,placeholder_text='Enter email',font=('Roboto',12),width=300,corner_radius=50)
    delete_button=CTkButton(right_frame,text='Delete User',width=40,corner_radius=100,fg_color='#00ace6',command=Delete_user)
    Id_entry.place(x=50,y=20)
    delete_button.place(x=360,y=20)

    style = ttk.Style(right_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=('Roboto', 14))
    style.map('Treeview', background=[('selected', '#00ace6')])
    tree = ttk.Treeview(right_frame, height=15)
    tree['columns'] = ('First Name', 'Last Name', 'Email','DOB','Phone', 'Password', 'User role', 'City', 'Gender', 'Postcode')

    # Columns
    tree.column('#0', width=0, stretch=tkinter.NO)
    tree.column('First Name', anchor=tkinter.CENTER, width=120)
    tree.column('Last Name', anchor=tkinter.CENTER, width=120)
    tree.column('Email', anchor=tkinter.CENTER, width=200)
    tree.column('DOB', anchor=tkinter.CENTER, width=120)
    tree.column('Phone', anchor=tkinter.CENTER, width=160)
    tree.column('Password', anchor=tkinter.CENTER, width=160)
    tree.column('User role', anchor=tkinter.CENTER, width=100)
    tree.column('City', anchor=tkinter.CENTER, width=120)
    tree.column('Gender', anchor=tkinter.CENTER, width=80)
    tree.column('Postcode', anchor=tkinter.CENTER, width=100)
    # heading
    tree.heading('First Name', text='First Name')
    tree.heading('Last Name', text='Last Name')
    tree.heading('Email', text='Email')
    tree.heading('DOB', text='DOB')
    tree.heading('Phone', text='Phone')
    tree.heading('Password', text='Password')
    tree.heading('User role', text='User role')
    tree.heading('City', text='City')
    tree.heading('Gender', text='Gender')
    tree.heading('Postcode', text='Postcode')
    # data query
    conn = sqlite3.connect('riders_data.db')
    u = conn.cursor()
    u.execute("SELECT*,ROW_NUMBER() OVER() AS num_row FROM riders WHERE user_role='rider'")
    riders = u.fetchall()
    for rider in riders:
        tree.insert('', 'end',
                    values=(rider[1], rider[2], rider[3],rider[4],rider[5], rider[8], rider[9], rider[10], rider[11], rider[12]))
        conn.close()
    tree.place(x=2, y=60)
    Users_ui.mainloop()


#Delete User
def Delete_user(Id_entry):
    dbId=str(Id_entry.get())
    conn = sqlite3.connect('riders_data.db')
    cursor=conn.cursor()
    cursor.execute('DELETE FROM riders WHERE email = ?',(dbId,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Status", "Data Deleted successfully.")
    Users_ui.destroy()
    Users_page()

def add_equipment_Page():
    equipment_ui =Tk()
    equipment_ui.title("Add an Equipment - Revolution Bike Park")

    global quantity_id_entry
    global quantity_entry
    global equipment_entry

    frame =CTkFrame(equipment_ui, width=300, )
    frame.pack()

    # saving user info
    user_info_frame =LabelFrame(frame, text="Equipment Information")
    user_info_frame.grid(row=0, column=0, sticky="news")

    equipment_label =Label(user_info_frame, text="Equipement name")
    equipment_label.grid(row=0, column=0)
    quantity_label = Label(user_info_frame, text="Quantity")
    quantity_label.grid(row=2, column=0)
    quantity_id_label = Label(user_info_frame, text="Equipement name")
    quantity_id_label.grid(row=4, column=0)

    equipment_entry = CTkEntry(user_info_frame,placeholder_text='Name', placeholder_text_color='#909090')
    quantity_entry = CTkEntry(user_info_frame,placeholder_text='Quantity', placeholder_text_color='#909090')
    quantity_id_entry = CTkEntry(user_info_frame, placeholder_text='Equipment_id', placeholder_text_color='#909090')
    equipment_entry.grid(row=1, column=0)
    quantity_entry.grid(row=3, column=0)
    quantity_id_entry.grid(row=5, column=0)


    # Button
    button = tkinter.Button(frame, text="Add", command=Equipment_enter_data)
    button.grid(row=6, column=0, sticky="news", padx=20, pady=10)
    equipment_ui.mainloop()

def Equipment_enter_data():
    dbequipment_id = str(quantity_id_entry.get())
    dbequipment_Name = str(equipment_entry.get())
    dbquantity = str(quantity_entry.get())


    conn: Connection = sqlite3.connect('riders_data.db')
    cursor = conn.execute(
        "INSERT INTO equipments (equipment_id,equipment_Name,quantity) VALUES (?,?,?)",
        (dbequipment_id,dbequipment_Name,dbquantity))
    conn.commit()
    messagebox.showinfo("Status", "Added Successfully ")
    add_equipment_Page().destroy()
    Equipment_enter_data()


def User_Page():
    Login_GUI.destroy()
    global Home
    Home = Tk()
    Home.title('Home')
    # Main frame
    User_home = CTkScrollableFrame(Home, corner_radius=0, width=1380, height=900, orientation=VERTICAL)
    User_home.pack()
    Background_image = PhotoImage(file="pattern.png")
    side_image = Label(User_home, image=Background_image)
    side_image.place(x=0, y=0)

    User_home.config(width=1380, height=850)
    w, h = Home.winfo_screenwidth(), Home.winfo_screenheight()
    Home.geometry("%dx%d+0+0" % (w, h))
    #Banner frame
    banner_bar =CTkFrame(User_home,width=1380,height=80,corner_radius=0,fg_color='#585858')
    banner_bar.place(x=0,y=0)
    #Logo_frame
    Logo_frame = CTkFrame(banner_bar,width=36, height=36,corner_radius=100,fg_color='#3385ff')
    Logo_frame.place(x=680, y=10)
    email_text = CTkLabel(banner_bar, text='customer@bikepark.com', text_color='#E8E8E8', width=10, height=10, corner_radius=100,
                         font=('Roboto', 12, 'bold'))
    logo_text = CTkLabel(Logo_frame, text='BP', text_color='#E8E8E8',width=10,height=10,corner_radius=100,font=('Roboto',12,'bold'))
    logo1_text=CTkLabel(banner_bar,text='Bike',text_color='#3385ff',font=('Roboto',16,'bold'))
    logo2_text = CTkLabel(banner_bar, text='Park',text_color='#E8E8E8',font=('Roboto',16,'bold'))
    contact_text = CTkLabel(banner_bar, text='+919032970456', text_color='#E8E8E8', width=10, height=10,
                          corner_radius=100,
                          font=('Roboto', 12, 'bold'))
    email_text.place(x=10, y=50)
    logo_text.pack(padx=2.5,pady=2.5)
    logo1_text.place(x=668,y=40)
    logo2_text.place(x=705,y=40)
    contact_text.place(x=1200, y=50)
    # navigation bar
    navigation_bar = CTkFrame(User_home, bg_color='#00ace6', fg_color='#00ace6', width=1350, height=60)
    navigation_bar.place(x=0, y=80)
    # Logo label
    Equipment_availability = CTkLabel(navigation_bar, text='Bike Park', text_color='#E8E8E8',
                                      font=('Roboto', 23, 'bold'))
    Equipment_availability.place(x=10, y=20)
    global search_bar
    search_bar = CTkEntry(navigation_bar, placeholder_text='Search here..', font=('Roboto', 12),
                          placeholder_text_color='#888888', width=240, height=30, corner_radius=20,
                          border_color='#F5F5F5')
    search_bar.place(x=1090, y=15)
    search_button = CTkButton(navigation_bar, text='Search', width=50, height=24, bg_color='#F8F8F8', corner_radius=50,command= De)
    search_button.place(x=1259, y=17.5)

    BookParking_Button = CTkButton(navigation_bar, text="Book Parking", corner_radius=50, width=100, height=30,
                                   font=("Times New Roman", 14), command=Book_Page)
    Policy_Button = CTkButton(navigation_bar, text="Parking Policy", corner_radius=50, width=100, height=30,
                              font=("Times New Roman", 14), command=ParkingPolicy)
    Logout_Button = CTkButton(navigation_bar, text="Logout", font=("Times New Roman", 14), corner_radius=50, width=100,
                              height=30, command=UptoBp)
    About_us = CTkButton(navigation_bar, text="About Us", corner_radius=50, width=100, height=30,
                         font=("Times New Roman", 14), command=AboutUs)
    BookParking_Button.place(x=480, y=14)
    Policy_Button.place(x=620, y=14)
    About_us.place(x=760, y=14)
    Logout_Button.place(x=880, y=14)

    #right side content frame
    Right_side_frame=CTkFrame(User_home,width=300,height=900,corner_radius=0,fg_color='#00ace6')
    Right_side_frame.place(x=0,y=140)
    #right frame content
    header=CTkLabel(Right_side_frame,text='Equipments For Rent ',text_color='#F8F8F8',font=('Roboto',14,'bold'))
    header.place(x=20,y=20)
    global y_axis_value
    global x_axis_value

    style = ttk.Style(Right_side_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=('Roboto', 14))
    style.map('Treeview', background=[('selected', '#00ace6')])
    tree = ttk.Treeview(Right_side_frame, height=15)
    tree['columns'] = ('No', 'Item', 'Qty')

    # Columns
    tree.column('#0', width=0, stretch=tkinter.NO)
    tree.column('No', anchor=tkinter.CENTER, width=50)
    tree.column('Item', anchor=tkinter.CENTER, width=100)
    tree.column('Qty', anchor=tkinter.CENTER, width=50)

    # heading
    tree.heading('No', text='No')
    tree.heading('Item', text='Item')
    tree.heading('Qty', text='Qty')
    # data query
    conn = sqlite3.connect('riders_data.db')
    u = conn.cursor()
    u.execute("SELECT* FROM equipments")
    riders = u.fetchall()
    for rider in riders:
        tree.insert('', 'end',
                    values=(rider[0], rider[1], rider[2]))
        conn.close()
    tree.place(x=10, y=60)

    #main content frame
    infor_frame=CTkFrame(User_home,width=600,height=400,fg_color='#F0F0F0',bg_color='#696969')
    infor_frame.place(x=500,y=250)
    bike_image = PhotoImage(file="unsplash.png")
    side_image = Label(infor_frame, image=bike_image)
    side_image.place(x=200, y=90)
    intro_header = CTkLabel(infor_frame,text='Get Rolling with Bike Park',text_color='#00ace6',font=('Roboto',20,'bold'))
    intro_text=CTkLabel(infor_frame,text='Ready to hit the trails? Experience the ease and convenience of Bike Parks\n '
                                         'prototype management system! Book your bike parking slot or rent equipment now and\n '
                                         'embark on your adventure hassle-free.')
    Rent_button=CTkButton(infor_frame,text='Rent Now',width=300,height=50,corner_radius=0,text_color='#00ace6',fg_color='#F0F0F0',border_color='#00ace6',command=Rent_Page)
    Book_button = CTkButton(infor_frame, text='Book Now',width=300,height=50,corner_radius=0,fg_color='#00ace6',command=Book_Page)
    intro_header.place(x=50,y=25)
    intro_text.place(x=100, y=250)
    Rent_button.place(x=0, y=350)
    Book_button.place(x=300, y=350)



    Home.mainloop()


def De():
   zz=str(search_bar.get())
   conn = sqlite3.connect('riders_data.db')
   cursor = conn.execute("SELECT*FROM bookings")
   for row in cursor:
       if row[1] != zz:
           global S
           S = f"You do have any bookings.Book now"
           messagebox.showinfo("Details", S)
       else:
           S = f"bookings DETAILS : \nbooking_id = " + str(row[0]) + "\nbooking_date = " + row[5] + "\nfirst_name = " + \
               row[2] + "\nlast_name = " + row[3] + "\npostcode = " + row[7]
           messagebox.showinfo("Details", S)
   conn.commit()

def ParkingPolicy():
    messagebox.showinfo("Parking Policy", "NOTE :\n \nAll students wishing to use parking facilities operated by the "
                                          "University Parking Office on the University Park campus, or any property "
                                          "owned or leased by The Lovely Professional University, must register "
                                          "their vehicle with the Parking Office and, while parked, properly display "
                                          "an authorized parking permit.\n\nParking permits must be properly "
                                          "displayed while parked:\n\nMOTORCYCLES: Permit (sticker) must be clearly "
                                          "visible from the front or rear of the motorcycle.\nAUTOMOBILES: Hang "
                                          "permit from rearview mirror, facing forward. Permit must be clearly "
                                          "visible. If windshield tint strip prevents clear display, permit hangers "
                                          "are available from the Parking Office.\n\nExceptions must be approved by "
                                          "the Parking Office in advance.")


def AboutUs():
    messagebox.showinfo("About Us",
                        "NOTE : \nWelcome to Bike Park, a prototype management system designed to streamline the "
                        "operations of bicycle rental services and park management. At Bike Park, we're dedicated to "
                        "providing a user-friendly platform for both customers and employees, built with Python, "
                        "tkinter, and SQLite technologies.\n\nOur primary focus is on developing a functional "
                        "prototype web application that enables customers to easily book available bike parking "
                        "spaces. These bookings are seamlessly uploaded to a secure database, ensuring efficient "
                        "management of park resources.\n\nAdditionally, Bike Park offers a comprehensive management "
                        "system tailored for park employees. This system allows staff to oversee bookings, "
                        "manage rental equipment inventory, and facilitate staff scheduling to optimize operational "
                        "efficiency.\nWhile the current iteration of Bike Park is a prototype, our goal is to create "
                        "a robust solution that meets the outlined criteria. If you're a skilled Python developer "
                        "interested in contributing to this exciting project, we welcome your expertise. Together, "
                        "we can further refine and enhance Bike Park to meet the needs of both customers and park "
                        "management staff.\n\nIf you're interested in joining our team or discussing further details "
                        "about the project, we'd be delighted to connect with you. Let's collaborate to bring Bike "
                        "Park to life and revolutionize the bicycle rental industry.")


def UptoBp():
    messagebox.showinfo("Status", "Successfully Logged Off")
    Home.destroy()
    Base_Page()


def Book_Page():
    booking_ui = tkinter.Tk()
    booking_ui.title("Book a place - Revolution Bike Park")
    global first_name_entry
    global last_name_entry
    global email_entry
    global dob_select
    global postcode_entry
    global phone_entry
    global bookdate_select

    frame =CTkFrame(booking_ui, width=300,height=600 )
    frame.pack()

    # saving user info
    user_info_frame = tkinter.LabelFrame(frame, text="Rider Information")
    user_info_frame.grid(row=0, column=0, sticky="news")

    first_name_label = tkinter.Label(user_info_frame, text="First Name")
    first_name_label.grid(row=0, column=0)
    last_name_label = tkinter.Label(user_info_frame, text="Last name")
    last_name_label.grid(row=0, column=1)

    first_name_entry = tkinter.Entry(user_info_frame)
    last_name_entry = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)

    email_label = tkinter.Label(user_info_frame, text='Email')
    email_entry = tkinter.Entry(user_info_frame)
    email_label.grid(row=0, column=2)
    email_entry.grid(row=1, column=2)

    dob_label = tkinter.Label(user_info_frame, text='Date of Birth')
    dob_select = DateEntry(user_info_frame, selectmode='day')
    dob_label.grid(row=2, column=0)
    dob_select.grid(row=3, column=0, padx=10, pady=5)

    postcode_label = tkinter.Label(user_info_frame, text="Postcode")
    postcode_entry = tkinter.Entry(user_info_frame)
    postcode_label.grid(row=2, column=1)
    postcode_entry.grid(row=3, column=1)

    phone_label = tkinter.Label(user_info_frame, text="Emergency contact number")
    phone_entry = tkinter.Entry(user_info_frame)
    phone_label.grid(row=2, column=2)
    phone_entry.grid(row=3, column=2)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Saving Course info
    booking_frame = tkinter.LabelFrame(frame, text="Booking information")
    booking_frame.grid(row=1, column=0, sticky="news")

    bookdate_label = tkinter.Label(booking_frame, text="Please select the date you would like to ride")
    bookdate_select = DateEntry(booking_frame, selectmode='day')
    bookdate_label.grid(row=0)
    bookdate_select.grid(row=1)

    for widget in booking_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Accept terms
    terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
    terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    accept_var = tkinter.StringVar(value="Not Accepted")
    terms_check = tkinter.Checkbutton(terms_frame,
                                      text="I take full responsibility for my/my child's safety and fully understand "
                                           "the risks involved.",
                                      variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
    terms_check.grid(row=0, column=0)

    # Button
    button = tkinter.Button(frame, text="Enter data", command=enter_data)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    booking_ui .resizable(False, False)
    booking_ui.mainloop()



def enter_data():
    dbrider_id = str(email_entry.get())
    dbid = str(email_entry.get())
    dbfirstName = str(first_name_entry.get())
    dblastName = str(last_name_entry.get())
    dbEmail = str(email_entry.get())
    dbdob = str(dob_select.get())
    dbpostcode = str(postcode_entry.get())
    dbMobile = str(phone_entry.get())
    dbbookingdate = str(bookdate_select.get())

    conn: Connection = sqlite3.connect('riders_data.db')
    cursor = conn.execute(
        "INSERT INTO bookings (rider_id,booking_id,first_name,last_name,email,dob,postcode,emergence_contact,"
        "booking_date) VALUES (?,?,?,?,?,?,?,?,?)",
        (dbrider_id, dbid, dbfirstName, dblastName, dbEmail, dbdob, dbpostcode, dbMobile, dbbookingdate))
    conn.commit()
    messagebox.showinfo("Status", "Successfully booked")
    Book_Page().destroy()
    enter_data()

#rent popup
def Rent_Page():
    global Rent_ui
    Rent_ui = tkinter.Tk()
    Rent_ui.title("Rent an Equipment - Revolution Bike Park")
    global first_name_entry
    global last_name_entry
    global email_entry
    global quantity_entry
    global dob_select
    global postcode_entry
    global phone_entry
    global bookdate_select
    global equipement_entry
    global City_entry

    frame = tkinter.Frame(Rent_ui, width=300, )
    frame.pack()

    # saving user info
    user_info_frame = tkinter.LabelFrame(frame, text="Rider Information")
    user_info_frame.grid(row=0, column=0, sticky="news")

    first_name_label = tkinter.Label(user_info_frame, text="First Name")
    first_name_label.grid(row=0, column=0)
    last_name_label = tkinter.Label(user_info_frame, text="Last name")
    last_name_label.grid(row=0, column=1)

    first_name_entry = CTkEntry(user_info_frame,placeholder_text='first_name', placeholder_text_color='#909090')
    last_name_entry = CTkEntry(user_info_frame,placeholder_text='last_name', placeholder_text_color='#909090')
    first_name_entry.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)

    email_label = tkinter.Label(user_info_frame, text='Email')
    email_entry = CTkEntry(user_info_frame,placeholder_text='Email', placeholder_text_color='#909090')
    email_label.grid(row=0, column=2)
    email_entry.grid(row=1, column=2)

    City_label = tkinter.Label(user_info_frame, text="City")
    City_entry =CTkEntry(user_info_frame,placeholder_text='City', placeholder_text_color='#909090')
    City_label.grid(row=2, column=0)
    City_entry.grid(row=3, column=0)

    postcode_label = tkinter.Label(user_info_frame, text="Postcode")
    postcode_entry = CTkEntry(user_info_frame,placeholder_text='Postcode', placeholder_text_color='#909090')
    postcode_label.grid(row=2, column=1)
    postcode_entry.grid(row=3, column=1)

    phone_label = tkinter.Label(user_info_frame, text="contact number")
    phone_entry = CTkEntry(user_info_frame,placeholder_text='Mobile number', placeholder_text_color='#909090')
    phone_label.grid(row=2, column=2)
    phone_entry.grid(row=3, column=2)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Saving Course info
    booking_frame = tkinter.LabelFrame(frame, text="Booking information")
    booking_frame.grid(row=1, column=0, sticky="news")

    equipement_label = tkinter.Label(booking_frame, text='Equipment name')
    equipement_entry = CTkEntry(booking_frame,placeholder_text='Equipment name', placeholder_text_color='#909090' )
    equipement_label.grid(row=0, column=0)
    equipement_entry.grid(row=1, column=0, padx=10, pady=5)

    bookdate_label = tkinter.Label(booking_frame, text="Please select the date you would like to ride")
    bookdate_select = DateEntry(booking_frame, selectmode='day')
    bookdate_label.grid(row=0,column=1)
    bookdate_select.grid(row=1,column=1)

    quantity_label = tkinter.Label(booking_frame, text='Quantity')
    quantity_entry = CTkEntry(booking_frame, placeholder_text='Quantity', placeholder_text_color='#909090', )
    quantity_label.grid(row=0, column=2)
    quantity_entry.grid(row=1, column=2, padx=10, pady=5)

    for widget in booking_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
    # Accept terms
    terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
    terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    accept_var = tkinter.StringVar(value="Not Accepted")
    terms_check = tkinter.Checkbutton(terms_frame,
                                      text="I take full responsibility for this item and fully understand "
                                           "the risks involved.",
                                      variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
    terms_check.grid(row=0, column=0)

    # Button
    button = tkinter.Button(frame, text="Submit", command=rent_enter_data)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    Rent_ui.mainloop()

def rent_enter_data():
    dbsales_id = str(email_entry.get())
    dbriderid = str(email_entry.get())
    dbfirstName = str(first_name_entry.get())
    dblastName = str(last_name_entry.get())
    dbEmail = str(email_entry.get())
    dbCity = str(email_entry.get())
    dbpostcode = str(postcode_entry.get())
    dbMobile = str(phone_entry.get())
    dbequipment_name = str(equipement_entry.get())
    dbReturn_date = str(phone_entry.get())
    dbqantity = str(quantity_entry.get())

    conn: Connection = sqlite3.connect('riders_data.db')
    cursor = conn.execute(
        "INSERT INTO sales (sale_id,rider_id,first_name,last_name,email,city,phone_number,item,quantity,sale_date,postcode) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (dbsales_id,dbriderid,dbfirstName,dblastName,dbEmail,dbCity,dbMobile,dbequipment_name,dbqantity, dbReturn_date,dbpostcode))
    messagebox.showinfo("Status", "Successfully Rented")
    Rent_ui.destroy()
    rent_enter_data()

Base_Page()
