from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
class ordersClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x500+220+130")
        self.root.title("Inventory Management System   |  Created by Shubham Roy and Arpita Hatibaruah")
        self.root.configure(bg="#F0FDFA")
        self.ent1 = StringVar()
        self.ent2 = StringVar()
        self.ent3 = StringVar()
        self.ent4 = StringVar()
        self.ent5 = StringVar()
        self.ent6 = StringVar()
        self.ent7 = StringVar()
        self.ent8=StringVar()
        self.ent9 = StringVar()
        self.ent10= StringVar()
        label3 = Label(self.root, text="Manage Orders", font=("Arial", 30), bg="#414C6B", fg="white",anchor='w',padx=50).place(x=10,
                                                                                                               y=10,
                                                                                                               height=50,
                                                                                                               width=780)
        date=DateEntry(self.root, selectmode='day', textvariable=self.ent1,relief=RIDGE).place(x=680,y=20,height=20,width=100)
        b1 = Button(self.root, text='Filter Date',bg="#97DEE7").place(x=580,y=20,height=20,width=100)
        customer=Label(self.root,text="Customer",font=("Arial",10)).place(x=10,y=70,height=20,width=100)
        customerentry=Entry(self.root,textvariable=self.ent2,bd=2,relief=RIDGE).place(x=120,y=70,height=25,width=200)
        orderid=Label(self.root,text="Order ID",font=("Arial",10)).place(x=340,y=70,height=20,width=100)
        orderidentry = Entry(self.root, textvariable=self.ent3, bd=2, relief=RIDGE).place(x=450, y=70, height=25,
                                                                                           width=100)
        ship = Label(self.root, text="Shipping Method", font=("Arial", 10)).place(x=560, y=70, height=20, width=100)
        shipentry = ttk.Combobox(self.root, textvariable=self.ent8,values=("Select","Indian Post","BlueDart","Delhivery","FedX")).place(x=670, y=70, height=25,
                                                                                          width=100)
        employee = Label(self.root, text="Employee", font=("Arial", 10)).place(x=10, y=105, height=20, width=100)
        employeerentry = Entry(self.root, textvariable=self.ent4, bd=2, relief=RIDGE).place(x=120, y=105, height=25,
                                                                                           width=200)
        orderdate = Label(self.root, text="Order date", font=("Arial", 10)).place(x=340, y=105, height=20, width=100)
        orderdateentry = DateEntry(self.root,selectmode='day', textvariable=self.ent5, relief=RIDGE).place(x=450, y=105, height=25,
                                                                                          width=100)
        category = Label(self.root, text="Product Category", font=("Arial", 10)).place(x=560, y=105, height=20, width=100)
        categoryentry = Entry(self.root, textvariable=self.ent9, relief=RIDGE).place(x=670,
                                                                                                            y=105,
                                                                                                            height=25,
                                                                                                            width=100)
        product = Label(self.root, text="Product", font=("Arial", 10)).place(x=10, y=135, height=20, width=100)
        producterentry = Entry(self.root, textvariable=self.ent6, bd=2, relief=RIDGE).place(x=120, y=135, height=25,
                                                                                            width=200)
        num = Label(self.root, text="Product No.", font=("Arial", 10)).place(x=340, y=135, height=20, width=100)
        numeentry = Entry(self.root, textvariable=self.ent7, relief=RIDGE).place(x=450,
                                                                                                            y=135,
                                                                                                            height=25,
                                                                                                            width=100)
        quantity = Label(self.root, text="Quantity", font=("Arial", 10)).place(x=560, y=135, height=20, width=100)
        quantityentry = Entry(self.root, textvariable=self.ent10, relief=RIDGE).place(x=670,
                                                                                 y=135,
                                                                                 height=25,
                                                                                 width=100)
        Button1 = Button(self.root, text="Create Order", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=250, y=170,
                                                                                                     height=30,
                                                                                                     width=100)
        Button2 = Button(self.root, text="Delete Order", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=400,
                                                                                                             y=170,
                                                                                                             height=30,
                                                                                                             width=100)
        tableframe = Frame(self.root, bd=2, relief=RIDGE).place(x=20, y=210, height=200, width=750)

        employeetable = ttk.Treeview(self.root, columns=(
        "Customer","Product", "Quantity", "Unit price", "Total price" ), selectmode='browse').place(x=25,
                                                                                                                 y=215,
                                                                                                                 height=195,
                                                                                                                 width=745)
        Button3 = Button(self.root, text="Save", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=250,
                                                                                                             y=430,
                                                                                                             height=30,
                                                                                                             width=100)
        Button3 = Button(self.root, text="Order", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=400,
                                                                                                     y=430,
                                                                                                     height=30,
                                                                                                     width=100)


if __name__=="__main__":
    root = Tk()
    obj = ordersClass(root)
    root.mainloop()