from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk 
from datetime import datetime
import database_conn


class InsertUpdate :
    
    def __init__(self):
        
        
        self.root = Tk()
        self.root.title("Insert & Update")
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
        self.root.geometry(f"{display_width}x{display_height}+0+0")
        self.img = Image.open('classic.jpg').resize((1500,700))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.root, image=self.imgTk)
        self.imgLbl.place(x=0,y=0)
        
        # Labels and Buttons
        
        title = Label(self.root, text="COURSES & CATEGORY (CRUD)", font=("Courier New", 32, "bold"), bg="#a3a3c2",
                        fg='#26273C', relief=SUNKEN, bd=10) 
        title.pack(side=TOP, fill=X)
        
        self.frame_2 = Frame(self.root, bg='#E0E0EB', relief=FLAT, bd=2)
        self.frame_2.place(x=600, y=100, width=700, height=225)

        self.frame_3 = Frame(self.root, bg='#E0E0EB', relief=FLAT, bd=2)
        self.frame_3.place(x=600, y=400, width=700, height=225)
        
        self.button = Button(self.root, text="View Courses", font=('Courier New', 17),bg='white',fg='black',command=self.view_courses)
        self.button.place(x=50, y=100)
        
        self.button_2 = Button(self.root, text="View Category", font=('Courier New', 17),bg='white',fg='black',command=self.view_category)
        self.button_2.place(x=50, y=410)
        
        
        # Add Insert Course button
        self.insert_course_btn = Button(self.root, text="Insert Course", font=('Courier New', 14), bg='white', fg='black',command=self.show_insert_course)
        self.insert_course_btn.place(x=300, y=100)
        
       # Add entry field for new course (initially hidden)
        self.new_course_entry = Entry(self.root, font=('Courier New', 14))
        self.new_course_entry.place(x=50, y=200)
        self.new_course_entry.place_forget()
        
        
        # Add Submit button for new course (initially hidden)
        self.submit_course_btn = Button(self.root, text="Submit Course", font=('Courier New', 14), bg='white', fg='black', command=self.insert_course)
        self.submit_course_btn.place(x=300, y=200)
        self.submit_course_btn.place_forget()
        
        # Variable to track if insert fields are visible
        self.insert_fields_visible = False
        
        #For Category
        
        self.button_3 = Button(self.root, text="Insert Category", font=('Courier New', 14),bg='white',fg='black',command=self.show_insert_category)
        self.button_3.place(x=300, y=410)
        
        
        self.new_category_entry = Entry(self.root, font=('Courier New', 14))
        self.new_category_entry.place(x=50, y=510)
        self.new_category_entry.place_forget()
        
        self.submit_category_btn = Button(self.root, text="Submit Category", font=('Courier New', 14), bg='white', fg='black', command=self.insert_category)
        self.submit_category_btn.place(x=300, y=510)
        self.submit_category_btn.place_forget()   
        
        # Variable to track if insert fields are visible
        self.category_fields_visible = False
             
        # Treeview_2
        
        self.col_2 = ['ID','Course Name', 'Update','Delete']
        self.tree_2 = ttk.Treeview(self.frame_2, columns=self.col_2, show='headings')
        self.tree_2.heading('#1', text='ID')
        self.tree_2.heading('#2', text='Course Name')
        self.tree_2.heading('#3', text='Update')
        self.tree_2.heading('#4', text='Delete')
        


        self.tree_2.column('#1', anchor=CENTER,width=80)
        self.tree_2.column('#2', anchor=CENTER,width=80)
        self.tree_2.column('#3', anchor=CENTER,width=80)
        self.tree_2.column('#4', anchor=CENTER,width=80)
        

        self.tree_2.pack(fill="both", expand=True)
        
        
        
          # Treeview_3
        
        self.col_3 = ['ID','Catagory Name', 'Update','Delete']
        self.tree_3 = ttk.Treeview(self.frame_3, columns=self.col_3, show='headings')
        self.tree_3.heading('#1', text='ID')
        self.tree_3.heading('#2', text='Catagory Name')
        self.tree_3.heading('#3', text='Update')
        self.tree_3.heading('#4', text='Delete')
        


        self.tree_3.column('#1', anchor=CENTER,width=80)
        self.tree_3.column('#2', anchor=CENTER,width=80)
        self.tree_3.column('#3', anchor=CENTER,width=80)
        self.tree_3.column('#4', anchor=CENTER,width=80)
        

        self.tree_3.pack(fill="both", expand=True)
        
        # Update fields (initially hidden)
        self.update_entry = Entry(self.root, font=('Courier New', 14))
        self.update_entry.place(x=50, y=250)
        self.update_entry.place_forget()

        self.update_btn = Button(self.root, text="Confirm Update", font=('Courier New', 14), bg='white', fg='black', command=self.confirm_update)
        self.update_btn.place(x=300, y=250)
        self.update_btn.place_forget()

        self.current_update_id = None
        self.current_update_type = None
        
        
        
        self.root.mainloop()
        
        
    def view_courses(self):
        self.tree_2.delete(*self.tree_2.get_children())
        data = database_conn.view_all_courses()
        print(data)
        for x in data :
            print(x)
            self.tree_2.insert("", 0, text=x[0], values=(x[0], x[1], 'Update','Delete'))
        self.tree_2.bind('<Double-Button-1>', self.actions_2)
            
            
    def actions_2(self,e):
        print("i am e",e)
        col = self.tree_2.identify_column(e.x)
        print(f'cols {col}')
        tt = self.tree_2.focus()
        
        itemSelected = self.tree_2.item(tt)
        
        Id = (
            self.tree_2.item(tt).get('values')
        )
        print("ID------------------->",Id[0])
        if col == "#3":
            self.show_update_field(Id[0], Id[1], "course")
            
        elif col == "#4":
            response = messagebox.askyesno("Delete", "Are you sure you want to delete this course?")
            if response:
                data = database_conn.delete_all_courses(Id[0])
                
                print("Data-------------?",data)
                if data :
                    messagebox.showinfo("Deleted Successfully")
                    # if new_status == 1:
                    self.root.destroy()
                    InsertUpdate()
                    self.view_courses()
             
             
    def show_update_field(self, id, current_value, update_type):
        self.update_entry.delete(0, END)
        self.update_entry.insert(0, current_value)
        self.update_entry.place(x=50, y=250)
        self.update_btn.place(x=300, y=250)
        self.current_update_id = id
        print("Current_ID--------------------->",self.current_update_id)
        self.current_update_type = update_type 
        print("current_update_type--------------------->",self.current_update_type)
        
    
    
    def confirm_update(self):
        new_value = self.update_entry.get()
        if new_value:
            if self.current_update_type == "course":
                success = database_conn.update_all_courses(self.current_update_id, new_value)
                if success:
                    messagebox.showinfo("Success", "Course updated successfully")
                    self.root.destroy()
                    InsertUpdate()
                    self.view_courses()
                else:
                    messagebox.showerror("Error", "Failed to update course")
            elif self.current_update_type == "category":
                success = database_conn.update_all_category(self.current_update_id, new_value)
                if success:
                    messagebox.showinfo("Success", "Category updated successfully")
                    InsertUpdate()
                    self.view_category()
                else:
                    messagebox.showerror("Error", "Failed to update category")
            
            self.update_entry.place_forget()
            self.update_btn.place_forget()
            self.current_update_id = None
            self.current_update_type = None
        else:
            messagebox.showwarning("Warning", "Please enter a value")
    
                
                    
    def view_category(self):
        self.tree_3.delete(*self.tree_3.get_children())
        data = database_conn.view_all_category()
        print(data)
        for x in data :
            print(x)
            self.tree_3.insert("", 0, text=x[0], values=(x[0], x[1], 'Update', 'Delete'))
        self.tree_3.bind('<Double-Button-1>',self.actions_3)
            
            
    def actions_3(self,e):
        print("i am e",e)
        col = self.tree_3.identify_column(e.x)
        print(f'cols {col}')
        tt = self.tree_3.focus()
        
        itemSelected = self.tree_3.item(tt)
        
        Id = (
            self.tree_3.item(tt).get('values')
        )
        print("ID------------------->",Id)
        if col == '#3':
            self.show_update_field(Id[0],Id[1],"category")
            
        elif col == "#4":
            response = messagebox.askyesno("Delete", "Are you sure you want to delete this course?")
            if response:
                data = database_conn.delete_all_category(Id[0])
                
                print("Data-------------?",data)
                if data :
                    messagebox.showinfo("Deleted Successfully")
                    # if new_status == 1:
                    self.root.destroy()
                    InsertUpdate()
                    self.view_category()
                    
                    
    def show_insert_course(self):
        if not self.insert_fields_visible:
            self.new_course_entry.place(x=50, y=200)
            self.submit_course_btn.place(x=300, y=200)
            self.insert_fields_visible = True
                  
    def insert_course(self):
        self.new_course = self.new_course_entry.get()
        if self.new_course:
            success = database_conn.insert_all_courses(self.new_course)
            if success :
                messagebox.showinfo("Success", "New course added successfully")
                self.root.destroy()
                InsertUpdate()
                self.view_courses()
                
            else:
                messagebox.showerror("Error", "Failed to add new course")
        else:
            messagebox.showwarning("Warning", "Please enter a course name")

    def show_insert_category(self):
        if not self.category_fields_visible:
            self.new_category_entry.place(x=50, y=510)
            self.submit_category_btn.place(x=300, y=510)
            self.category_fields_visible = True
            
    def insert_category(self):
        
        new_category = self.new_category_entry.get()
        if new_category:
            success = database_conn.insert_all_category(new_category)
            if success:
                messagebox.showinfo("Success", "New category added successfully")
                self.root.destroy()
                self.view_category()
            else:
                messagebox.showerror("Error", "Failed to add new category")
        else:
            messagebox.showwarning("Warning", "Please enter a category name")
            
    
    
        
if __name__=='__main__':
    InsertUpdate()