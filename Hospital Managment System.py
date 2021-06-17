from tkinter import *
import tkinter.messagebox
root =Tk()
root.title("Hospital Managemnt System")
root.geometry("1350x750+0+0")
root.configure(bg="powder blue")
lbltitle=Label(root,text="Hospital Managemnt System",font=("arial",15,"bold"),bd=10,width=45,justify=CENTER,bg="gainsboro")
lbltitle.pack()
mainframe=Frame(root,width=1350,height=600,bg="powder blue")
mainframe.pack()
leftframe=Frame(mainframe,width=650,height=500,bg="cadet blue",bd=15,padx=2,pady=10,relief=RIDGE)
leftframe.pack(side=LEFT)
Rightframe=Frame(mainframe,width=650,height=500,bd=10,padx=2,pady=10,relief=RIDGE,bg="cadet blue")
Rightframe.pack(side=RIGHT)
Bottomframe=Frame(root,width=300,height=350,bg="cadet blue",bd=25,pady=10,padx=2,relief=RIDGE)
Bottomframe.pack(side=BOTTOM)
########################################################################
PatientName=StringVar()
PatientAge=StringVar()
PatientAddress=StringVar()
PatientReason=StringVar()
PatientWeight=StringVar()
PatientState=StringVar()
PatientEntryTime=StringVar()
PatientLeaveTime=StringVar()
DoctarName=StringVar()
NewEntry=StringVar()
ExitPage=StringVar()


def NewEntry():
    PatientName.set("")
    PatientAge.set("")
    PatientAddress.set("")
    PatientReason.set("")
    PatientWeight.set("")
    PatientState.set("")
    PatientEntryTime.set("")
    PatientLeaveTime.set("")
    DoctarName.set("")
    btnNewEntry("1,0",END)
def ExitPage():
    Exit = tkinter.Messagebox.askyesno("Hospitsl Management system", "confirm if  you want to  exit")
    if Exit > 0:
        root.destroy()
        return

##################################################################################################
lblName=Label(leftframe,text="patient Name",font=("arial",20,"bold"))
lblName.grid(column=0,row=0,sticky=W)
txtName=Entry(leftframe,text="patient Name",font=("arial",20,"bold"),bg="powder blue",bd=8,textvariable="patient Name")
txtName.grid(row=0,column=1)

lblAge=Label(leftframe,text="patientAge",font=("arial",20,"bold"))
lblAge.grid(column=0,row=1,sticky=W)
txtAge=Entry(leftframe,text="patient Age",font=("arial",20,"bold"),bg="powder blue",bd=8,textvariable="patient Age")
txtAge.grid(row=1,column=1)

lblweight=Label(leftframe,text="patientweight",font=("arial",20,"bold"))
lblweight.grid(column=0,row=2,sticky=W)
txtweight=Entry(leftframe,text="patient weight",font=("arial",20,"bold"),bg="powder blue",bd=8,textvariable="patient weight")
txtweight.grid(row=2,column=1)

lblAddress=Label(leftframe,text="patientAddress",font=("arial",20,"bold"))
lblAddress.grid(column=0,row=3,sticky=W)
txtAddress=Entry(leftframe,font=("arial",20,"bold"),bg="powder blue",bd=8,textvariable="patient Address")
txtAddress.grid(row=3,column=1)

lblReason=Label(leftframe,text="patient Reason",font=("arial",20,"bold"))
lblReason.grid(column=0,row=4,sticky=W)
txtReason=Entry(leftframe,font=("arial",20,"bold"),bg="powder blue",bd=8,textvariable="patient Reason")
txtReason.grid(row=4,column=1)

lblDoctorname=Label(leftframe,text="Doctor Name",font=("arial",25,"bold"))
lblDoctorname.grid(column=0,row=8,sticky=W)
txtDoctorname=Entry(leftframe,font=("arial",20,"bold"),bg="powder blue",bd=8,textvariable="Doctor Name")
txtDoctorname.grid(row=8,column=1)


lblEntryTime=Label(leftframe,text="patientEntryTime",font=("arial",20,"bold"))
lblEntryTime.grid(column=0,row=6,sticky=W)
txtEntrytime=Entry(leftframe,font=("arial",20,"bold"),bg="powder blue",bd=8,textvariable="patientEntryTime")
txtEntrytime.grid(row=6,column=1)

lblLeaveTime=Label(leftframe,text="patient State",font=("arial",20,"bold"))
lblLeaveTime.grid(column=0,row=7,sticky=W)
txtLeaveTime=Entry(leftframe,font=("arial",20,"bold"),bg="powder blue",bd=8,textvariable="patient State")
txtLeaveTime.grid(row=7,column=1)

lblState=Label(leftframe,text="patient State",font=("arial",20,"bold"))
lblState.grid(column=0,row=5,sticky=W)
txtstate=Entry(leftframe,font=("arial",20,"bold"),bg="powder blue",bd=8,textvariable="patient State")
txtstate.grid(row=5,column=1)

btnExit=Button(Bottomframe,text="Exit Page",font=("arial",20,"bold"),bd=30,justify=CENTER,bg="cadet blue",command=ExitPage)
btnExit.grid(row=0,column=0)

btnNewEntry =Button(Bottomframe,text="New Entry",font=("arial",20,"bold"),bd=30,justify=CENTER,bg="cadet blue",command=NewEntry)
btnNewEntry.grid(row=0,column=1)


root.mainloop()