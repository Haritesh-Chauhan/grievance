from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk 
from datetime import datetime
import database_conn,login_here_1 ,view_complaints

class Dashboard:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Grievance Dashboard")
        self.root.resizable(False, False)
        display_width = self.root.winfo_screenwidth() - 10
        display_height = self.root.winfo_screenheight() - 70
        
        self.root.geometry(f"{display_width}x{display_height}+0+0")

        # Get the current date
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d/%m/%y")
        print("Current Date - ", formatted_date)
        # Extract the month from the given date
        # month = formatted_date.split('/')[1]
        # print("Current date month - ", month)
        
    # def dashboard_widgets(self):
    
        self.img = Image.open('classic.jpg').resize((1500,700))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.root, image=self.imgTk)
        self.imgLbl.place(x=0,y=0)
        
        title = Label(self.root, text="Grievance Portal", font=("Courier New", 32, "bold"), bg="#a3a3c2",
                        fg='#26273C', relief=SUNKEN, bd=10) 
        title.pack(side=TOP, fill=X)

        self.frame1 = Frame(self.root, width=500, height=575, bg='#e0e0eb', relief=FLAT, bd=2)
        self.frame1.place(x=10, y=80)

        self.frame2 = Frame(self.root, width=730, height=550, bg='#e0e0eb', relief=SUNKEN, bd=2)
        self.frame2.place(x=520, y=270, width=800, height=383)
        
        self.button = Button(self.root, text="Check Registration",command=self.show_treeview_data)
        self.button.place(x = 1200, y=225)
        
        self.button_2 = Button(self.root, text="View Complaint",command=self.viewed_complaint)
        self.button_2.place(x = 570, y=225)
        
       

        self.img_2 = Image.open('dashboard_pic.png').resize((480, 554))
        self.imgTk_2 = ImageTk.PhotoImage(self.img_2)
        self.imgLbl_2 = Label(self.frame1, image=self.imgTk_2)
        self.imgLbl_2.place(x=4, y=7)
        
       
        #Treeview
        
        self.col = ['ID','Username', 'Password', 'Email', 'Student ID','Status']
        self.tree = ttk.Treeview(self.frame2, columns=self.col, show='headings')
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Username')
        self.tree.heading('#3', text='Password')
        self.tree.heading('#4', text='Email')
        self.tree.heading('#5', text='Student ID')
        self.tree.heading('#6', text='Status')


        self.tree.column('#1', anchor=CENTER,width=80)
        self.tree.column('#2', anchor=CENTER,width=80)
        self.tree.column('#3', anchor=CENTER,width=80)
        self.tree.column('#4', anchor=CENTER,width=80)
        self.tree.column('#5', anchor=CENTER,width=80)
        self.tree.column('#6', anchor=CENTER,width=80)

        self.tree.pack(fill="both", expand=True)    

        # for i in database_conn.show_all_users():
        #     # print(i)
        #     i=list(i)
        #     # i[5] = "Inactive" if [5] == 0 else "Active"
        #     if i[5]==0:
        #         i[5]="Inactive"
        #     else:
        #         i[5]="Active"
        #     self.tree.insert("", 0, text=i[0], values=(i[0], i[1], i[2], i[3], i[4],i[5]))



        # self.tree.bind('<Double-Button-1>', self.actions)
        
        
        self.root.mainloop()
    
    def show_treeview_data(self):
        # Clear any existing data in the Treeview
        self.tree.delete(*self.tree.get_children())

        # Get the data from the database and populate the Treeview
        for i in database_conn.show_all_users():
            i = list(i)
            if i[5] == 0:
                i[5] = "Inactive"
            else:
                i[5] = "Active"
            self.tree.insert("", 0, text=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5]))
            self.tree.bind('<Double-Button-1>', self.actions)

    
    def actions(self, e):
        print("i am e",e)
        col = self.tree.identify_column(e.x)
        print(f'cols {col}')
        tt = self.tree.focus()
        
        itemSelected = self.tree.item(tt)
        
        Id = (
            self.tree.item(tt).get('values')
        )
        print(Id[0])
        self.name = Id[1]
   
        
        if col == "#6":
            response = messagebox.askyesno("Edit", "Are you sure you want to change the status?")
            if response:
                current_status = 0 if Id[5] == "Inactive" else 1
                new_status = 1 if current_status == 0 else 0
                data = (new_status, Id[0])
                print(data)
            
                status = database_conn.updateStatus(data)
                if status:
                    messagebox.showinfo("Saved", "Status Updated Successfully")
                    if new_status == 1:
                        self.root.destroy()
                        Dashboard()
                else:
                    messagebox.showwarning("Error", "Something went wrong")
            else:
                pass
            
    def viewed_complaint(self):
        self.root.destroy()
        view_complaints.ViewComplaints()
    
    
        
        
if __name__=='__main__':
    # if __debug__:
    #     print("Cannot open the Dashboard directly")
    # else:
        Dashboard()