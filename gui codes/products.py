from tkinter import *
from tkinter import ttk
class productsClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System   |  Created by Shubham Roy and Arpita Hatibaruah")
        self.root.configure(bg="#F0FDFA")
        self.ent1=StringVar()
        self.ent2 = StringVar()
        self.ent3 = StringVar()
        self.ent4 = StringVar()
        self.ent5 = StringVar()
        self.ent6 = StringVar()
        searchengine=LabelFrame(self.root,text="Search by").place(x=20,y=20,height=60,width=500)
        search=ttk.Combobox(self.root,textvariable=self.ent1,values=("Select","Product Id","Product name","Product Category"),state="readonly",justify=CENTER).place(x=30,y=45,height=20,width=100)
        label1=Entry(self.root, bd=2,textvariable=self.ent2,relief=RIDGE,bg="#FFFDD0").place(x=140,y=45,height=20,width=300)
        label2=Button(self.root, bd=2, text="Search",bg="#78C5DC").place(x=460,y=45,height=20,width=50)

     #Product Details
        label3=Label(self.root,text="Product Details",font=("Arial",30) ,bg="#414C6B",fg="white").place(x=10,y=100,height=50, width=500)
        label4=Label(self.root,text="Product ID", font=("Arial",10)).place(x=20,y=170,height=30,width=100)
        label5 = Label(self.root, text="product Name", font=("Arial", 10)).place(x=300, y=170, height=30, width=100)
        label6 = Label(self.root, text="Product Category", font=("Arial", 10)).place(x=20, y=250, height=30, width=100)
        label7 = Label(self.root, text="Sales", font=("Arial", 10)).place(x=300, y=250, height=30, width=100)
        entry1=Entry(self.root,textvariable=self.ent3,bd=2,relief=RIDGE).place(x=130,y=170,height=30,width=150)
        entry2 = Entry(self.root,textvariable=self.ent4, bd=2, relief=RIDGE).place(x=130, y=170, height=30, width=150)
        entry3 = Entry(self.root,textvariable=self.ent5, bd=2, relief=RIDGE).place(x=410, y=170, height=30, width=100)
        entry4 =Entry(self.root,textvariable=self.ent4, bd=2, relief=RIDGE).place(x=130, y=250, height=30, width=150)
        entry5 = ttk.Combobox(self.root,textvariable=self.ent6,values=("Select","<1000","1000-5000","5000-10000",">10000"),state="readonly",justify=CENTER ).place(x=410, y=250, height=30, width=100)
        Button1=Button(self.root,text="Save",bd=2,relief=RIDGE,bg="#97DEE7",fg="black").place(x=50,y=380,height=30,width= 100)
        Button1 = Button(self.root, text="Update", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=160, y=380,height=30,width=100)
        Button1 = Button(self.root, text="Delete", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=270, y=380,height=30,width=100)
        Button1 = Button(self.root, text="Clear", bd=2, relief=RIDGE, bg="#97DEE7", fg="black").place(x=380, y=380,height=30,width=100)

        tablelabel1 = Label(self.root, text="Product Table", font=("Arial", 30), bg="#414C6B", fg="white").place(x=540,
                                                                                                                  y=20,
                                                                                                                  height=50,
                                                                                                                  width=550)
        tableframe = Frame(self.root, bd=2, relief=RIDGE).place(x=540, y=80, height=500, width=550)

        employeetable = ttk.Treeview(self.root, columns=(
        "product ID", "product Name", "Category", "Sales"), selectmode='browse').place(x=550,
                                                                                                                 y=90,
                                                                                                                 height=500,
                                                                                                                 width=530)


if __name__=="__main__":
    root = Tk()
    obj = productsClass(root)
    root.mainloop()

