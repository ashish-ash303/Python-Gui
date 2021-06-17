from tkinter import *
root=Tk()
import random
from datetime import datetime
import tkinter.messagebox
class Hotel:
    def __init__(self, a):
        self.root = root
        self.root.title("Hotel Managment System")

        self.root.geometry = ("1350x750+0+0")

        self.root.config(background="powder blue")

        mainframe = Frame(self.root)
        mainframe.grid()

        Topframe = Frame(mainframe, bd=14, width=1350, height=550, padx=20, relief=RIDGE, bg="cadet blue")
        Topframe.pack(side=TOP)

        Leftframe = Frame(Topframe, bd=10, width=450, height=550, padx=2, relief=RIDGE, bg="powder blue")
        Leftframe.pack(side=LEFT)

        Rightframe = Frame(Topframe, bd=10, width=820, height=550, padx=2, relief=RIDGE, bg="cadet blue")
        Rightframe.pack(side=RIGHT)

        Buttomframe = Frame(mainframe, bd=28, width=1350, height=550, padx=2, relief=RIDGE, bg="powder blue")
        Buttomframe.pack(side=BOTTOM)


        def iExit():
            iExit=tkinter.messagebox.askyesno("Hotel Management system","confirm if  you want to  exit")
            if iExit>0:
                a.destroy()
                return

        def Receipt():
           self.txtReceipt.insert(END,customerid.get()+"\t"+ Firstname.get()+"\t"+ surname.get()+"\t"+ address.get()+"\t"+address.get()+"\n")
        def Reset():
            customerid.set("")
            Firstname .set("")
            surname .set("")
            address.set("")
            City.set("")

            Reset.set("")
            self.txtReceipt.delete("1.0",END)

        def TotalCostandDate():

            inDate=checkindate.get()
            outDate=checkoutdate.get()
            inDate=datetime.strptime(checkindate,"%d/%m/%Y")
            outDate=datetime.strptime(checkoutdate,"%d/%m/%Y")
            Totalnodays.set(abs(outDate-inDate).days)


        customerid = StringVar()
        Firstname = StringVar()
        surname = StringVar()
        address = StringVar()
        City = StringVar()
        Mobileno = StringVar()
        Email = StringVar()
        Idproof = StringVar()
        DOB = StringVar()
        Nationality = StringVar()
        Totalnodays = StringVar()
        Exit = StringVar()
        paid = StringVar()
        Total = StringVar()
        roomtype = StringVar()
        Receipt = StringVar()
        checkindate = StringVar()
        checkoutdate = StringVar()
        Gender = StringVar()
        Reset=StringVar()
        Roomno=StringVar()
        self.lblcustomerid = Label(Leftframe, font=("arial", 14, "bold"), text="customerid", padx=2, bg="powder blue")
        self.lblcustomerid.grid(row=0, column=0, sticky=W)

        self.txtcustomerid = Entry(Leftframe, font=("arial", 14, "bold"), text="customerid", width=20)
        self.txtcustomerid.grid(row=0, column=1, pady=3, padx=20, )

        self.Firstname = Label(Leftframe, font=("arial", 14, "bold"), text="Firstname", padx=2, bg="powder blue")
        self.Firstname.grid(row=1, column=0, sticky=W)

        self.Firstname = Entry(Leftframe, font=("arial", 14, "bold"), text="Firstname", width=20)
        self.Firstname.grid(row=1, column=1, pady=3, padx=20, )

        self.surname = Label(Leftframe, font=("arial", 14, "bold"), text="surname", padx=2, bg="powder blue")
        self.surname.grid(row=2, column=0, sticky=W)

        self.surname = Entry(Leftframe, font=("arial", 14, "bold"), text="surname", width=20)
        self.surname.grid(row=2, column=1, pady=3, padx=20 )


        self.City = Entry(Leftframe, font=("arial", 14, "bold"), text="City", width=20)
        self.City.grid(row=4, column=1, pady=3, padx=20, )





        self.Mobileno = Entry(Leftframe, font=("arial", 14, "bold"), text="Mobileno", width=20)
        self.Mobileno.grid(row=5, column=1, pady=3, padx=20, )

        self.Email = Label(Leftframe, font=("arial", 14, "bold"), text="Email", padx=2, bg="powder blue")
        self.Email.grid(row=6, column=0, sticky=W)

        self.Email = Entry(Leftframe, font=("arial", 14, "bold"), text="Email", width=20)
        self.Email.grid(row=6, column=1, pady=3, padx=20, )

        self.Idproof = Label(Leftframe,font=("arial",14, "bold"), text="Idproof", padx=2, bg="powder blue")
        self.Idproof.grid(row=7, column=0, sticky=W)

        self.Idproof = Entry(Leftframe, font=("arial", 14, "bold"), text="Idproof", width=20)
        self.Idproof.grid(row=7, column=1, pady=3, padx=20)


        self.DOB = Label(Leftframe, font=("arial", 14, "bold"), text="DOB", padx=2, bg="powder blue")
        self.DOB.grid(row=8, column=0, sticky=W)

        self.DOB = Entry(Leftframe, font=("arial", 14, "bold"), text="DOB", width=20)
        self.DOB.grid(row=8, column=1, pady=3, padx=20)


        self.lblNationality =Label (Leftframe, font=("arial", 14, "bold"), text="Nationality", padx=2, bg="powder blue",pady=2)
        self.lblNationality.grid(row=9,column=0,sticky=W)

        self.Nationality=Entry(Leftframe,font=("arial", 14, "bold"), text="Nationality", width=20)
        self.Nationality.grid(row=9,column=1,pady=3,padx=20)
        self.checkindate = Label(Leftframe, font=("arial", 14, "bold"), text="checkindate", padx=2, bg="powder blue")
        self.checkindate.grid(row=11, column=0, sticky=W)

        self.checkindate = Entry(Leftframe, font=("arial", 14, "bold"), text="checkindate", width=20)
        self.checkindate.grid(row=11, column=1, pady=3, padx=20)

        self.checkoutdate = Label(Leftframe, font=("arial", 14, "bold"), text="checkoutdate", padx=2, bg="powder blue")
        self.checkoutdate.grid(row=12, column=0, sticky=W)

        self.checkoutdate = Entry(Leftframe, font=("arial", 14, "bold"), text="checkoutdate", width=20)
        self.checkoutdate.grid(row=12, column=1, pady=3, padx=20)

        self.roomtype = Label(Leftframe, font=("arial", 14, "bold"), text="roomtype", padx=2, bg="powder blue")
        self.roomtype.grid(row=13, column=0, sticky=W)

        self.roomtype = Entry(Leftframe, font=("arial", 14, "bold"), text="roomtype", width=20)
        self.roomtype.grid(row=13, column=1, pady=3, padx=20)

        self.Roomno = Label(Leftframe, font=("arial", 14, "bold"), text="Roomno", padx=2, bg="powder blue")
        self.Roomno.grid(row=14, column=0, sticky=W)

        self.Roomno = Entry(Leftframe, font=("arial", 14, "bold"), text="Roomno", width=20)
        self.Roomno.grid(row=14, column=1, pady=3, padx=20)

        self.lblLabel=Label(Rightframe,font=('arial',10,'bold'),pady =9,bg='cadet blue',text="customer id\tFirstname\t surname\t address\t  Totalnofdays\t checkindate\t checkoutdate\t cont:\t")
        self.lblLabel.grid(row=0,column= 0,columnspan=1)
        self.txtRecipt=Text(Rightframe,height=15,width=108,bd=10,font=('arial',11,'bold'))
        self.lblLabel.grid(row=0,column= 0,columnspan=1)
        self.txtRecipt=Text(Rightframe,height=15,width=108,bd=10,font=('arial',11,'bold'))
        self.txtRecipt.grid(row=1,column=0,columnspan=2,padx=2,pady=5)

#===================================================================================================================================
        self.lblDays=Label(Rightframe,font=('arial',14,'bold'),text='No of Days',bd=7,bg="cadet blue",fg="Black")
        self.lblDays.grid(row=2,column=0,sticky=W)
        self.txtDays=Entry(Rightframe,font=('arial',10,'bold'),textvariable='TotalnofDays',bd=7,bg="white",width=67,justify=LEFT)
        self.txtDays.grid(row=2,column=0)


        self.lblpaid=Label(Rightframe,font=('arial',14,'bold'),text='Total  paid',bd=7,bg="cadet blue",fg="Black")
        self.lblpaid.grid(row=3,column=0,sticky=W)

        self.txtpaid = Entry(Rightframe, font=('arial', 10, 'bold'), textvariable='Total paid', bd=7, bg="white",
                              width=67, justify=LEFT)
        self.txtpaid.grid(row=3, column=0)

        self.btnTotal= Button(Buttomframe,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=25,height=2,bg='powder blue',text="Total",command=Total).grid(row=0,column=4,padx=2)



        self.btnReceipt=Button(Buttomframe,padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=21, height=2,bg='powder blue', text="Receipt",command=Receipt).grid(row=0, column=5, padx=2)
        self.btnReset=Button(Buttomframe,padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=21, height=2,bg='powder blue', text="Reset",command=Reset).grid(row=0, column=6, padx=2)


        self.btnExit=Button(Buttomframe,padx=16,pady=1,bd=4, fg="black", font=('arial', 16, 'bold'), width=21, height=2,bg='powder blue', text="Exit",command=iExit).grid(row=0, column=7, padx=2)



if __name__ == '__main__':
        root = Tk()
        application = Hotel(root)
        root.mainloop()


