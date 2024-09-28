from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox
import complaint_portal, complaint_status

class Main:
    
    def __init__(self, id):
        self.id = id
        self.root=Tk()
        print("id----------------->",id)
        self.root.title("Grievance Wall")
        self.root.resizable(False, False)
        display_width = self.root.winfo_screenwidth() - 10
        display_height = self.root.winfo_screenheight() - 70
        self.root.geometry(f"{display_width}x{display_height}+0+0")
        
        
        self.img = Image.open('classic.jpg').resize((1500,700))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.root, image=self.imgTk)
        self.imgLbl.place(x=0,y=0)

        self.headings=Label(self.root, text='IN - GRIEVANCE', font=('Courier New', 35, 'bold','underline'), bg='white', fg='red')
        self.headings.place(x=400, y=70)

        self.headings=Label(self.root, text='PORTAL', font=('Courier New', 35, 'bold','underline'), bg='white', fg='black')
        self.headings.place(x=820, y=70)

        self.home=Button(self.root, text = 'HOME',font=('Courier New', 15),bg='white',fg='black',borderwidth=4,relief=GROOVE, highlightbackground="black", highlightthickness=1, bd=1)
        self.home.place(x=1250, y=25)

        self.destroy=Button(self.root, text = 'Destroy',font=('Courier New', 15),bg='white',fg='black',borderwidth=4,relief=GROOVE, highlightbackground="black", highlightthickness=1, bd=1,command=self.exit)
        self.destroy.place(x=1100, y=25)

        self.your_complaint=Button(self.root,text="YOUR'S COMPLAINT", bg='white', fg='black',borderwidth=4,relief=GROOVE, highlightbackground="black", highlightthickness=1, bd=1,font=('Courier New', 20), command = self.complaint_portal)
        self.your_complaint.place(x=500, y=280)

        self.status=Button(self.root, text = 'COMPLAINT STATUS',font=('Courier New', 20),bg='white',fg='black',borderwidth=4,relief=GROOVE, highlightbackground="black", highlightthickness=1, bd=1, command = self.check_status)
        self.status.place(x=500, y=450)
   

        '''self.B1 = Button(self.root, text="ASK", command =self.ask)
        self.B1.place(x=930, y=345)'''
        
        
        '''self.ExitBtn=Button(self.root,text="Exit",font=('Helvetica', 17),bg='white',fg='black',borderwidth=4,relief="groove", highlightbackground="black", highlightthickness=1, bd=1,command=self.exit)
        self.ExitBtn.place(x=930,y=600)'''


        self.root.mainloop()

    def complaint_portal(self):
        self.root.destroy()
        complaint_portal.Complaint(self.id)
    
    def check_status(self):
        self.root.destroy()
        complaint_status.ComplaintStatus(self.id)

    def exit(self):
        messagebox.askquestion('ALERT','Do you want to exit the window?')
        self.root.destroy()

    def ask(self):
         messagebox.askquestion("Select the option from where you want to get the screenshots")


if __name__=="__main__":
    Main(1)