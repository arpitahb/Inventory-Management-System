from tkinter import *
from tkinter import ttk

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System   |  Created by Shubham Roy and Arpita Hatibaruah")
        self.root.configure(bg="#F0FDFA")
        self.ent1 = StringVar()
        self.ent2 = StringVar()
        self.ent3 = StringVar()
        self.ent4 = StringVar()
        self.ent5 = StringVar()
        self.ent6 = StringVar()
        self.ent7 = StringVar()
        self.ent8 = StringVar()

        label3 = Label(self.root, text="Supplier Details", font=("Arial", 30), bg="#414C6B", fg="white").place(x=10,
                                                                                                               y=10,
                                                                                                               height=50,
                                                                                                               relwidth=1)
        label4 = Label(self.root, text="Supplier ID", font=("Arial", 10)).place(x=20, y=100, height=30, width=100)
        label5 = Label(self.root, text="Supplier Name", font=("Arial", 10)).place(x=300, y=100, height=30, width=100)
        label6 = Label(self.root, text="Contact", font=("Arial", 10)).place(x=20, y=180, height=30, width=100)
        label7 = Label(self.root, text="Sales", font=("Arial", 10)).place(x=300, y=180, height=30, width=100)
        label8 = Label(self.root, text="Adress", font=("Arial", 10)).place(x=20, y=260, height=30, width=100)
        entry1 = Entry(self.root, textvariable=self.ent3, bd=2, relief=RIDGE).place(x=130, y=100, height=30, width=150)

        entry3 = Entry(self.root, textvariable=self.ent5, bd=2, relief=RIDGE).place(x=410, y=100, height=30, width=100)
        entry4 = Entry(self.root, textvariable=self.ent4, bd=2, relief=RIDGE).place(x=130, y=180, height=30, width=150)
        entry5 = ttk.Combobox(self.root, textvariable=self.ent6, values=("Select", "<1000", "1000-5000", "5000-10000",">10000"),
                              state="readonly", justify=CENTER).place(x=410, y=180, height=30, width=100)
        entry6 = Entry(self.root, textvariable=self.ent7, bd=2, relief=RIDGE).place(x=130, y=260, height=100, width=400)

        Button1 = Button(self.root, text="Save", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=50, y=380,
                                                                                                     height=30,
                                                                                                     width=100)
        Button1 = Button(self.root, text="Update", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=160, y=380,
                                                                                                       height=30,
                                                                                                       width=100)
        Button1 = Button(self.root, text="Delete", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=270, y=380,
                                                                                                       height=30,
                                                                                                       width=100)
        Button1 = Button(self.root, text="Clear", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=380, y=380,
                                                                                                      height=30,
                                                                                                      width=100)

        labelz = Label(self.root, text="Supplier ID", font=("Arial", 10)).place(x=600, y=100, height=30, width=100)
        entry1 = Entry(self.root, bd=2, relief=RIDGE).place(x=710, y=100, height=30, width=250)
        Button1 = Button(self.root, text="Search", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=970, y=100,
                                                                                                     height=30,
                                                                                                     width=100)
        tableframe = Frame(self.root, bd=2, relief=RIDGE).place(x=600, y=150, height=500, width=480)

        employeetable = ttk.Treeview(self.root, columns=(
        "Supplier ID", "Supplier Name", "Cotact", "Sales"), selectmode='browse').place(x=610,
                                                                                                                 y=160,
                                                                                                                 height=500,
                                                                                                                 width=470)


if __name__=="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()