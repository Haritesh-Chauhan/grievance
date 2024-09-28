from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from PIL import Image , ImageTk
import database_conn, users_reg , complaint_status , wall


class Complaint:
    
    def __init__(self,id ):
        
        self.root = Tk()
        self.id = id
        print(id)
        self.root.title("Complaint Portal")
        self.root.resizable(False, False)
        display_width = self.root.winfo_screenwidth() - 10
        display_height = self.root.winfo_screenheight() - 70
        
        self.root.geometry(f"{display_width}x{display_height}+0+0")

        # Get the current date
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d/%m/%y")
        print("Current Date - ", formatted_date)
        
        self.img = Image.open('classic.jpg').resize((1500,700))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.root, image=self.imgTk)
        self.imgLbl.place(x=0,y=0)
        
        
        # Label
        
        title = Label(self.root, text="Grievance Portal", font=("Courier New", 32, "bold"), bg="#d1d1e0",
                        fg='#26273C', relief=SUNKEN, bd=10) 
        title.pack(side=TOP, fill=X)
        
        self.course=Label(self.root,text='Course',font=('Courier New', 17),bg='white',fg='black')
        self.course.place(x=300,y=160)

        self.category=Label(self.root, text="Categories", font=('Courier New', 17),bg='white',fg='black')
        self.category.place(x=300, y=220)
        
        self.room=Label(self.root,text='Room Number',font=('Courier New', 17),bg='white',fg='black')
        self.room.place(x=300,y=280)

        self.complaint=Label(self.root, text="Complaint", font=('Courier New', 17),bg='white',fg='black')
        self.complaint.place(x=300, y=340)
        
        # Entry
        courses = database_conn.course()
        print(courses)
        self.course_names = [course[1] for course in courses]
        self.course_ids = [course[0] for course in courses]
        self.course_dict = dict(zip(self.course_names, self.course_ids))
        print(self.course_dict)
        
        
        self.courseEnt = ttk.Combobox(self.root,values=self.course_names,font=('Courier New', 17) )
        self.courseEnt.place(x=500,y=160)
        
        # Bind the combobox selection event
        self.courseEnt.bind("<<ComboboxSelected>>", self.update_selected_course)
        # Add this as an instance variable
        self.selected_course_id = None
        
        
        category = database_conn.categories()
        print(category)
        
                
        self.catagory_name = [cat[1] for cat in category]
        self.category_ids = [cat[0] for cat in category]
        self.category_dict = dict(zip(self.catagory_name, self.category_ids))
        print(self.category_dict)
        
        self.categoryEnt=ttk.Combobox(self.root,values=self.catagory_name, font=('Courier New', 17))
        self.categoryEnt.place(x=500, y=220)
        
        # Bind the combobox selection event
        self.categoryEnt.bind("<<ComboboxSelected>>", self.update_selected_category)

        # Add this as an instance variable
        self.selected_catagory_id = None
        
        self.roomEnt=Entry(self.root,text='Room Number',font=('Courier New', 17),bg='white',fg='black')
        self.roomEnt.place(x=500,y=280)

        self.complaintEnt = Text(self.root, font=('Courier New', 17), bg='white', fg='black', width=30, height=5)
        self.complaintEnt.place(x=500, y=340)


        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.complaintEnt.yview)
        scrollbar.place(x=910, y=340, height=125) 

        self.complaintEnt.config(yscrollcommand=scrollbar.set)
        
        self.button = Button(self.root, text="SUBMIT", font=('Courier New', 17),bg='white',fg='black',command=self.submit_complaint )
        self.button.place(x=560, y=550)
        
        self.button_2 = Button(self.root, text="BACK", font=('Courier New', 17),bg='white',fg='black',command=self.back )
        self.button_2.place(x=750, y=550)
        # if self.button:
        #     self.button_2 = Button(self.root, text="View Grievance", font=('Courier New', 17),bg='white',fg='black',  )
        # self.button_2.place(x=590, y=550)
     
        
        
        
        self.root.mainloop()
        
    
    def update_selected_course(self,event):
        self.selected_course = self.courseEnt.get()
        self.selected_course_id = self.course_dict.get(self.selected_course)
        print(f"Selected course: {self.selected_course}, ID: {self.selected_course_id}")
        
    def update_selected_category(self,event) :
        self.selected_catagory = self.categoryEnt.get()
        self.selected_catagory_id = self.category_dict.get(self.selected_catagory)
        print(f"Selected catarory: {self.selected_catagory}, ID: {self.selected_catagory_id}")
        
    def submit_complaint(self):
        print("In Submit Complaint")

        if self.id and self.courseEnt.get() and self.categoryEnt.get() and self.roomEnt.get() and self.complaintEnt.get("1.0", "end-1c").strip():
            
            verify = (self.id ,self.selected_course, self.selected_catagory, self.roomEnt.get(), self.complaintEnt.get("1.0", "end-1c").strip())
            print("Verified--------------->",verify)
            id = verify[0]
            print("id-------------------",id)
            
            try:
                success = database_conn.grievance_save(verify)
                print("Success----------------->",success)
                if success:
                    messagebox.showinfo("Success", "Complaint Registered Successfully!")
                    self.root.destroy()
                    complaint_status.ComplaintStatus(id)
                    
                else:
                    messagebox.showerror("Error", "Failed to register complaint. Please try again.")
                    
            except Exception as e :
                print(f"Exception: {e}")
                messagebox.showerror("Error", f"Failed to register complaint: {e}")
                
        else :
            messagebox.showerror("Something Went Wrong...")
            
            
    def back(self):
        self.root.destroy()
        wall.Main(self.id)
            
            
            
        
if __name__=='__main__':
    Complaint(1)
    
        
        
        