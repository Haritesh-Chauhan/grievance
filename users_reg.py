from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import database_conn, users_login

class UserReg:
    
    def __init__(self):
        
        self.root=Tk()
        self.root.title('Register Window')
        self.root.config(bg='white smoke')

        display_width = self.root.winfo_screenwidth() - 10
        display_height = self.root.winfo_screenheight() - 70
        self.root.geometry(f"{display_width}x{display_height}+0+0")
        self.root.config(bg='white smoke')

        self.root.resizable(False, False)
        
        self.img = Image.open('classic.jpg').resize((1500,700))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.root, image=self.imgTk)
        self.imgLbl.place(x=0,y=0)

        self.heading2=Label(self.root, text='GRIEVANCE', font=('Courier New', 40, 'bold'),bg='white smoke',fg='#1f1f2e')
        self.heading2.place(x=125, y=200)

        self.heading3=Label(self.root, text='PORTAL', font=('Courier New', 40, 'bold'),bg='white smoke',fg='black')
        self.heading3.place(x=180, y=275)

        self.heading3=Label(self.root, text='   We are here for your help !!!', font=('Courier New', 23),bg='white smoke',fg='black', wraplength=300)
        self.heading3.place(x=125, y=375)

        # self.home=Button(self.root, text = 'HOME',font=('Helvetica', 18),bg='white',fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1)
        # self.home.place(x=1190, y=25)

        self.canvas = tk.Canvas(self.root, width=650, height=440,bg='white',borderwidth=3, relief=GROOVE)
        self.canvas.place(x=590,y=160)
        self.canvas.create_polygon(30, 30, 390, 30, 210, 290, fill="white")
        
        #LABELS
        
        self.userLbl = Label(self.root,text='USERNAME ',font=('Helvetica', 20),bg='white',fg='black')
        self.userLbl.place(x=650, y=200)
        
        self.passLbl=Label(self.root, text="PASSWORD ", font=('Helvetica', 20),bg='white',fg='black')
        self.passLbl.place(x=650, y=263)
        
        self.emailLbl = Label(self.root,text='EMAIL',font=('Helvetica', 20),bg='white',fg='black')
        self.emailLbl.place(x=650,y=326)
        
        self.std_id = Label(self.root, text="STUDENT ID" ,font=('Helvetica', 20),bg='white',fg='black')
        self.std_id.place(x=650,y=389)

        #ENTRIES
        
        self.userEntry=Entry(self.root,font=('Helvetica', 20),bg='white', fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1)
        self.userEntry.place(x=890,y=198)

        self.passEntry=Entry(self.root,font=('Helvetica', 20), show = '*',bg='white', fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1)
        self.passEntry.place(x=890,y=260)

        self.emailEntry=Entry(self.root,font=('Helvetica', 20),bg='white', fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1)
        self.emailEntry.place(x=890,y=322)

        self.stdidEntry=Entry(self.root,font=('Helvetica', 20), show = '*',bg='white', fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1)
        self.stdidEntry.place(x=890,y=384)

        #BUTTON

        self.loginBtn=Button(self.root, text="SIGN UP",font=('Helvetica',17),bg='red',fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1,command=self.registring)
        self.loginBtn.place(x=900, y=450)
        
        self.line1=Label(self.root,text="Already have an account?",font=('Helvetica', 17),bg='white',fg='black')
        self.line1.place(x=807,y=505)

        self.registerBtn = Button(self.root, text="  LOG IN  ", font=('Helvetica', 16), bg='red', fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1,command=self.back)
        self.registerBtn.place(x=900, y=538)

       

        self.root.mainloop()
        
        

    def registring(self):
        print('button is clicked')
        if self.userEntry.get() and self.passEntry.get() and self.emailEntry.get() and self.stdidEntry.get():
            print('data is given')
            response = database_conn.user_register((self.userEntry.get(),self.passEntry.get(), self.emailEntry.get(), self.stdidEntry.get()))
            print(response)
            if response:
                messagebox.showinfo('Success')
                self.root.destroy()
            else:
                messagebox.showerror('Alert', 'Invalid credentials')
        else:
            print('enter details')
            messagebox.showerror('Alert', 'Please your details.')

    def back(self):
        self.root.destroy()
        users_login.UserLogin()


if __name__=='__main__':
    UserReg()