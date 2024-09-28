from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import database_conn, wall, users_reg, users_login


class UserLogin:
    
    def __init__(self):
        
        self.root = Tk()
        self.root.title('Login Window')
        self.root.resizable(False, False)
        display_width = self.root.winfo_screenwidth() - 10
        display_height = self.root.winfo_screenheight() - 70
        self.root.geometry(f"{display_width}x{display_height}+0+0")
        self.root.config(bg='white smoke')

        self.root.resizable(False, False)
        
        self.img = Image.open('classic.jpg').resize((1500,700))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.root, image=self.imgTk)
        self.imgLbl.place(x=0,y=0)

        self.heading2=Label(self.root, text='GRIEVANCE PORTAL', font=('Courier New', 40, 'bold'),bg='white smoke',fg='#1f1f2e', wraplength=500)
        self.heading2.place(x=150, y=175)

        # self.heading3=Label(self.root, text='NOTES', font=('Comic Sans MS', 40, 'bold'),bg='white smoke',fg='black')
        # self.heading3.place(x=265, y=275)

        self.heading3=Label(self.root, text='WE ARE HERE TO HELP YOU !!!', font=('Courier New', 23),bg='white smoke',fg='#1f1f2e', wraplength=370)
        self.heading3.place(x=170, y=340)

        self.home=Button(self.root, text = 'HOME',font=('Courier New', 15),bg='white',fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1)
        self.home.place(x=1200, y=25)

        self.canvas = tk.Canvas(self.root, width=620, height=370,bg='white',borderwidth=3, relief="groove")
        self.canvas.place(x=600,y=150)
        
        # Labels

        self.EmailLbl=Label(self.root,text='EMAIL ',font=('Courier New', 20),bg='white',fg='black')
        self.EmailLbl.place(x=640,y=200)

        self.PassLbl=Label(self.root, text="PASSWORD ", font=('Courier New', 20),bg='white',fg='black')
        self.PassLbl.place(x=640, y=263)
        
        # Entries
        
        self.EmailLbl_Ent=Entry(self.root,font=('Courier New', 17),bg='white', fg='black',borderwidth=4,relief=GROOVE, highlightbackground="black", highlightthickness=1, bd=1)
        self.EmailLbl_Ent.place(x=850,y=198)

        self.PassLbl_Ent=Entry(self.root,font=('Courier Newa', 17), show = '*',bg='white', fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1)
        self.PassLbl_Ent.place(x=850,y=260)

        # Button

        self.loginBtn=Button(self.root, text="LOGIN",font=('Courier New',17),bg='red',fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1, command = self.login)
        self.loginBtn.place(x=900, y=340)
        
        self.line1=Label(self.root,text='Dont have an account?',font=('Courier New', 17),bg='white',fg='black')
        self.line1.place(x=790,y=409)

        self.registerBtn = Button(self.root, text="CREATE NEW ACCOUNT", font=('Courier New', 16), bg='white', fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1,command=self.register)
        self.registerBtn.place(x=800, y=440)


        self.root.mainloop()
    

    def login(self):
        
        print('button is clicked')
        if self.EmailLbl_Ent.get() and self.PassLbl_Ent.get():
            print('data is given')
            response = database_conn.user_logging((self.EmailLbl_Ent.get(), self.PassLbl_Ent.get()))
            
            print(response)
            
            if response :
                for x in response :
                    print(x)
                    id = x[0]
                    status = x[-1]
                    name = x[1]
                    print("Name----------------->",name)
                    if status == 1 :
                        self.root.destroy()
                        wall.Main(id)
                    else :
                        messagebox.showinfo('Status Inactive')
                        self.root.destroy()
                        
                        
                        
            else:
                messagebox.showerror('Alert', 'Invalid credentials')
        else:
            print('enter details')
            messagebox.showerror('Alert', 'Please your details.')

    def register(self):
        self.root.destroy()
        users_reg.UserReg()
        

if __name__=='__main__':
    UserLogin()