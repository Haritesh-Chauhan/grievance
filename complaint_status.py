from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk 
from datetime import datetime
import database_conn,wall


class ComplaintStatus :
    
    def __init__(self,id):
        
        
        self.root = Tk()
        self.id = id
        print("id----------------->",id)
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
    
        self.root.geometry(f"{display_width}x{display_height}+0+0")
        self.img = Image.open('classic.jpg').resize((1500,700))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.root, image=self.imgTk)
        self.imgLbl.place(x=0,y=0)
        
        # Labels and Buttons
        
        title = Label(self.root, text="COMPLAINT STATUS", font=("Courier New", 32, "bold"), bg="#a3a3c2",
                        fg='#26273C', relief=SUNKEN, bd=10) 
        title.pack(side=TOP, fill=X)
        
        self.frame = Frame(self.root, bg='#e0e0eb', relief=FLAT, bd=2)
        self.frame.place(x=700, y=190, width=630, height=500)
        
        self.frame_2 = Frame(self.root, bg='#ccffcc', relief=FLAT, bd=2)
        self.frame_2.place(x=10, y=80, width=650, height=615)
        
        
        self.button = Button(self.root, text="Your Comaplaints", font=('Courier New', 17),bg='white',fg='black', command=self.your_comaplaint)
        self.button.place(x=700, y=100)
        
        self.button_2 = Button(self.root, text="Complaints Status", font=('Courier New', 17),bg='white',fg='black' ,command=self.status)
        self.button_2.place(x=965, y=100)
        
        self.button_3 = Button(self.root, text="Back", font=('Courier New', 17),bg='white',fg='black' ,command=self.back)
        self.button_3.place(x=1240, y=100)
        
        self.img_2 = Image.open('complaint.webp').resize((800,500))
        self.imgTk_2=ImageTk.PhotoImage(self.img_2)
        self.imgLbl_2=Label(self.frame_2, image=self.imgTk_2)
        self.imgLbl_2.place(x=-90,y=50)
        
        
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
        
        
        # self.data = database_conn.getSingleUser(id)
        # print("This is single user ID",self.data)
        # print(self.data[0][-1])
        # self.single_id = self.data[0][-1]
        # print("Singled--------->",self.single_id)
        
        
        
        self.root.mainloop()
        
        
    def your_comaplaint(self):
        # self.tree.delete(*self.tree.get_children())
        try :
        
          # Fetch all complaints
            all_complaints = database_conn.getSingleUser(self.id)
            print("alll",all_complaints)
            
            # Filter complaints for the current user
            # user_complaints = [complaint for complaint in all_complaints if complaint[0][-1] == self.id]
            # print("user",user_complaints)
            
            if all_complaints:
                
                    for i in all_complaints:
                        i = list(i)
                        if i[5] == 0:
                            i[5] = "Pending"
                        elif i[5] == 1:
                            i[5] = "In-Progress"
                        elif i[5] == 2:
                            i[5] = "Resolve"
                        self.tree.insert("", 0, text=i[0], values=(i[-1], i[1], i[2], i[3], i[4], i[5]))
                        self.tree.bind('<Double-Button-1>')
            else:
                messagebox.showinfo("No Complaints", "You haven't filed any complaints yet.")
                
        except Exception as e:
            print(f"Exception in view_complaints: {e}")
            messagebox.showerror("Error", f"Failed to fetch complaints: {e}")
            
    def status(self):
        print("View Stauts button is Clicked !!")
        self.root.destroy()
        ComplaintStatus(self.id)
        
    def back(self):
        self.root.destroy()
        wall.Main(self.id)
        
    
    


if __name__=='__main__':
    ComplaintStatus(1)