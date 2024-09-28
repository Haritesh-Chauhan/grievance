from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import database_conn, dashboard_2

class AdminLogin:
    
    def __init__(self) :
        self.root = Tk()
        self.root.geometry('1075x500')
        self.root.title("Grievance")
        self.root.resizable(False, False)
        # GETTING SCREEN CO-ORDINATES
        display_width = self.root.winfo_screenwidth() - 10
        display_height = self.root.winfo_screenheight() - 70
        # self.root.geometry(f"{display_width}x{display_height}+0+0")
        
    # def admn_login_widgets(self):
        
        self.first = Label(self.root, text='GRIEVANCE PORTAL', fg='#1f1f2e', font=('Courier New', 24, 'bold'), wraplength=800,
                           justify='left')
        self.first.place(x=680, y=28)

        self.frame2 = Frame(self.root, width=325, height=400, bg='#E1E1E1', relief=SUNKEN, bd=10)
        self.frame2.place(x=675, y=70)

        self.first1 = Label(self.frame2, text='Sign Into Your Account', bg='#E1E1E1', fg='#33334d',
                            font=('Courier New', 15, 'bold'), wraplength=400, justify='left')
        self.first1.place(x=12, y=20)

        self.img = Image.open('images.jpeg')
        self.img = self.img.resize((600, 480))

        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imglbl = Label(self.root, image=self.imgTk)
        self.imglbl.place(x=8, y=8)

        self.firstlbl = Label(self.frame2, text='USERNAME', bg='#E1E1E1', fg='#666699', font=('Courier New', 16, 'bold'),
                              wraplength=400, justify='left')
        self.firstlbl.place(x=10, y=85)

        self.username_entry = Entry(self.frame2,font=('Comfortaa',12),width=20)
        self.username_entry.place(x=105, y=125)

        self.passlbl = Label(self.frame2, text='PASSWORD', bg='#E1E1E1', fg='#666699', font=('Courier New', 17, 'bold'),
                             wraplength=400, justify='left')
        self.passlbl.place(x=10, y=165)

        self.password_entry = Entry(self.frame2,font=('Comfortaa',12),width=20, show='*')
        self.password_entry.place(x=105, y=205,)

        self.loginbtn = Button(self.frame2, text='LOGIN', bg='#E1E1E1', fg='#666699', activebackground='#E1E1E1',
                               activeforeground='#666699', font=('Courier New', 12, 'bold'),command=self.run_admin_login)
        self.loginbtn.place(x=115, y=270)
        self.root.mainloop()
        
    def run_admin_login(self):
        if self.username_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter the username first")
        elif self.password_entry.get() == "":
            messagebox.showwarning("Alert!", "Please enter the password first")
        else:
            print(f'Username is {self.username_entry.get()}, Password is {self.password_entry.get()}')

            login_result = database_conn.admin_logged((self.username_entry.get().strip(), self.password_entry.get()))

            if login_result:
                messagebox.showinfo('Success', 'Login successful.')
                self.root.destroy()
                dashboard_2.Dashboard()
            #     d = dashboard.Dashboard()
            #     d.dashboard_menus()
            #     d.dashboard_widgets()
            else:
                messagebox.showerror('Alert', 'Invalid username or password')
        
                 
        
if __name__ == '__main__':
    AdminLogin()
