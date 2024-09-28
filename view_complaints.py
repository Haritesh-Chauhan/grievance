from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk 
from datetime import datetime
import database_conn , course_insert_update
import dashboard_2


class ViewComplaints :
    
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Grievance Dashboard")
        self.root.resizable(False, False)
        display_width = self.root.winfo_screenwidth() - 10
        display_height = self.root.winfo_screenheight() - 70
        
        self.root.geometry(f"{display_width}x{display_height}+0+0")
        self.img = Image.open('classic.jpg').resize((1500,700))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.root, image=self.imgTk)
        self.imgLbl.place(x=0,y=0)

        
        # Get the current date
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d/%m/%y")
        print("Current Date - ", formatted_date)
        # Extract the month from the given date
        # month = formatted_date.split('/')[1]
        # print("Current date month - ", month)
        
    # def dashboard_widgets(self):
        
        # Labels and Buttons
        
        title = Label(self.root, text="COMPLAINT STATUS", font=("Courier New", 32, "bold"), bg="#a3a3c2",
                        fg='#26273C', relief=SUNKEN, bd=10) 
        title.pack(side=TOP, fill=X)
        
        self.frame = Frame(self.root, bg='#e0e0eb', relief=FLAT, bd=2)
        self.frame.place(x=650, y=150, width=700, height=540)
        
        self.frame_2 = Frame(self.root, bg='#e0e0eb', relief=FLAT, bd=2)
        self.frame_2.place(x=20, y=150, width=625, height=540)
        
        
        
       
        
        
        self.button = Button(self.root, text="View Comaplaints", font=('Courier New', 17),bg='white',fg='black',border=6, command=self.view_comaplaint)
        self.button.place(x=760, y=90)
        
        self.button_2 = Button(self.root, text="CRUD Course", font=('Courier New', 17),bg='white',fg='black',border=6,command=self.edit_courses)
        self.button_2.place(x=400, y=90)
        
        
        self.button_3 = Button(self.root, text="CRUD Catagory", font=('Courier New', 17),bg='white',border=6,fg='black',command=self.edit_category)
        self.button_3.place(x=50, y=90)
        
        self.button_4  = Button(self.root, text="Back",font=('Courier New', 15),bg='white',border=6,fg='black',command=self.back)
        self.button_4.place(x=1270, y=90)
        
        self.img_2 = Image.open('complaint_view.png').resize((620, 554))
        self.imgTk_2 = ImageTk.PhotoImage(self.img_2)
        self.imgLbl_2 = Label(self.frame_2, image=self.imgTk_2)
        self.imgLbl_2.place(x=0, y=0)
        

        
        # self.button_3 = Button(self.root, text="CRUD Catagory", font=('Courier New', 17),bg='white',fg='black',command=self.view_category)
        # self.button_3.place(x=50, y=200)
        
        # self.button_3 = Button(self.root, text="CRUD Catagory", font=('Courier New', 17),bg='white',fg='black',command=self.view_category)
        # self.button_3.place(x=50, y=200)
        
        # self.button_3 = Button(self.root, text="CRUD Catagory", font=('Courier New', 17),bg='white',fg='black',command=self.view_category)
        # self.button_3.place(x=50, y=200)
        
        # Treeview
        
        self.col = ['ID','Course', 'Categories', 'Room Number', 'Your Complaints','Status']
        self.tree = ttk.Treeview(self.frame, columns=self.col, show='headings')
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Course')
        self.tree.heading('#3', text='Categories')
        self.tree.heading('#4', text='Room Number')
        self.tree.heading('#5', text='Your Complaints')
        self.tree.heading('#6', text='Status')


        self.tree.column('#1', anchor=CENTER,width=80)
        self.tree.column('#2', anchor=CENTER,width=80)
        self.tree.column('#3', anchor=CENTER,width=80)
        self.tree.column('#4', anchor=CENTER,width=80)
        self.tree.column('#5', anchor=CENTER,width=80)
        self.tree.column('#6', anchor=CENTER,width=80)

        self.tree.pack(fill="both", expand=True)
        
        

        
        
        
        
        self.root.mainloop()
        
        
    def view_comaplaint(self):
        self.tree.delete(*self.tree.get_children())
        
        for i in database_conn.view_users_complaints():
            i = list(i)
            print(i)
            # if i[5] == 0:
            #     i[5] = "Pending"
            # elif i[5] == 1:
            #     i[5] = "In-Progress"
            # elif i[5] == 2 :
            #     i[5] = "Resolve"
            
            status_map = {0: "Pending", 1: "In-Progress", 2: "Resolved"}
            i[5] = status_map.get(i[5], "Unknown")
            print("i[5]----------------->",i[5])
            # "Pending" if i[5]==0 else "In-Progress" if i[5]==1 else "Resolved"
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
   
        
        if col == "#6":
            response = messagebox.askyesno("Edit", "Are you sure you want to change the status?")
            if response:
                current_status = {"Pending": 0, "In-Progress": 1, "Resolved": 2}.get(Id[5], 0)
                new_status = (current_status + 1) % 3
                if current_status == 2:
                    messagebox.showinfo("Info", "This complaint is already resolved and cannot be changed.")
                    return
                data = (new_status, Id[0])
                print("data------------------------>",data)
                # current_status = 1 if Id[5] == "In-Progress" else 0
                # print(current_status)
                # new_status = 2 if current_status == 1 else 1
                # print(new_status)
                # data = (new_status, Id[0])
                # print("Data ------------------->",data)
            
                status = database_conn.changeStatus(data)
                if status:
                    messagebox.showinfo("Saved", "Status Updated Successfully")
                    # if new_status == 1:
                    self.root.destroy()
                    ViewComplaints()
                else:
                    messagebox.showwarning("Error", "Something went wrong")
            else:
                pass
    
    
    def edit_courses(self):
        messagebox.showinfo("Sure !!!",'Moving forward!!!')
        self.root.destroy()
        course_insert_update.InsertUpdate()
        
        
        
        
    def edit_category(self):
        messagebox.showinfo("Sure !!!",'Moving forward!!!')
        self.root.destroy()
        course_insert_update.InsertUpdate()
        
    def back(self):
        self.root.destroy()
        dashboard_2.Dashboard()
        
        
        
   


if __name__=='__main__':
    ViewComplaints()