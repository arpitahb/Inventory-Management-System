from tkinter import *
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from sales import salesClass
from products import productsClass
from orders import ordersClass

class Main:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x700+0+0")
        self.root.title("Inventory Management System   |  Created by Shubham Roy and Arpita Hatibaruah")
        self.root.configure(bg="#F0FDFA")
        self.icon=PhotoImage(file="venv/Images/Icon2.png")
        self.homeicon = PhotoImage(file="venv/Images/homeicon1.png")
        self.menuicon = PhotoImage(file="venv/Images/menuicon.png")
#Title Section
        Title = Label(root, text="INVENTORY MANAGEMENT SYSTEM",image=self.icon,compound=LEFT, font=("Arial", 30), bg='#1E80C1', fg='white',anchor='w', padx=30).place(x=0, y=0, relwidth=1, height=50)
        logbutton=Label(self.root,text="Home",image=self.homeicon,compound=LEFT,font=("Arial",10),bg="white",fg="black").place(x=1350,y=10,height=30,width=150)

        #Menu Section



        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="#414C6B")
        LeftMenu.place(x=0,y=50,height=800,width=300)
        menulabel=Label(LeftMenu,text="Inventory Menu", font=("Arial",15),bg="#414C6B",fg="white",bd=10,relief=FLAT,cursor="hand2").pack(side=TOP,fill=X)
        menubutton1=Button(LeftMenu,text="Supplier" ,command=self.supplier, font=("Arial",15), bg="#414C6B",fg="white",anchor="w",padx=30,bd=10,relief=FLAT,cursor="hand2").pack(side=TOP,fill=X)
        menubutton2 = Button(LeftMenu, text="Category",command=self.category, font=("Arial", 15), bg="#414C6B", fg="white", anchor="w",padx=30,bd=10,relief=FLAT,cursor="hand2").pack(side=TOP, fill=X)
        menubutton3 = Button(LeftMenu, text="Employee",command=self.employee, font=("Arial", 15), bg="#414C6B", fg="white", anchor="w",padx=30,bd=10,relief=FLAT,cursor="hand2").pack(side=TOP, fill=X)
        menubutton4=Button(LeftMenu,text="Sales",command=self.sales, font=("Arial",15), bg="#414C6B",fg="white",anchor="w",padx=30,bd=10,relief=FLAT,cursor="hand2").pack(side=TOP,fill=X)
        menubutton4 = Button(LeftMenu, text="Products",command=self.products, font=("Arial", 15), bg="#414C6B", fg="white", anchor="w",padx=30,bd=10,relief=FLAT,cursor="hand2").pack(side=TOP, fill=X)
        menubutton5 = Button(LeftMenu, text="Orders",command=self.orders, font=("Arial", 15), bg="#414C6B", fg="white", anchor="w",padx=30,bd=10,relief=FLAT,cursor="hand2").pack(side=TOP, fill=X)
        menubutton6 = Button(LeftMenu, text="Company", font=("Arial", 15), bg="#414C6B", fg="white", anchor="w",
                             padx=30,bd=10,relief=FLAT,cursor="hand2").pack(side=TOP, fill=X)
        menubutton7 = Button(LeftMenu, text="Log Out", font=("Arial", 15), bg="#414C6B", fg="white", anchor="w",
                             padx=30,bd=10,relief=FLAT,cursor="hand2").pack(side=TOP, fill=X)
        #Dashboard section
        Dashboard=Frame(self.root, bd=5, relief=FLAT, bg="#F0FDFA")
        Dashboard.place(x=300,y=50,height=50,width=1300)
        Dash=Label(Dashboard,text="Dashboard", font=("Arial",20),fg="grey",anchor="w").pack(side=TOP, fill=X)

           #Labels in Dashboard
        dashLabel1=Label(self.root,text="Total Suppliers\n[ 0 ]",font=("Arial",20), relief=RIDGE,bg="#78C5DC").place(x=360,y=130,height=180,width=300)
        dashLabel2 = Label(self.root, text="Total Category\n[ 0 ]",font=("Arial",20), relief=RIDGE,bg="#97DEE7" ).place(x=690, y=130, height=180,
                                                                                       width=300)
        dashLabel3 = Label(self.root, text="Total Sales\n[ 0 ]",font=("Arial",20), relief=RIDGE,bg="#B7ECEA" ).place(x=1020, y=130, height=180,
                                                                                       width=300)
        dashLabel4 = Label(self.root, text="Total Products\n[ 0 ]",font=("Arial",20), relief=RIDGE,bg="#78C5DC" ).place(x=360, y=380, height=180,
                                                                                       width=300)
        dashLabel5 = Label(self.root, text="Total Orders\n[ 0 ]",font=("Arial",20), relief=RIDGE,bg="#97DEE7" ).place(x=690, y=380, height=180,
                                                                                       width=300)
        dashLabel6 = Label(self.root, text="Total Employess\n[ 0 ]",font=("Arial",20), relief=RIDGE,bg="#B7ECEA" ).place(x=1020, y=380, height=180,
                                                                                       width=300)
        footer=Label(self.root,text="This dasboard is a part of the Inventory Management System Project developed by Shubham Roy and Arpita Hatibaruah", font=("Arial", 10), bg="#1E80C1", fg="white").pack(side=BOTTOM, fill=X)

    def employee(self):
        self.emp=Toplevel(self.root)
        self.obj1=employeeClass(self.emp)

    def supplier(self):
        self.supp=Toplevel(self.root)
        self.obj2=supplierClass(self.supp)

    def category(self):
        self.categ=Toplevel(self.root)
        self.obj3=categoryClass(self.categ)

    def sales(self):
        self.sale=Toplevel(self.root)
        self.obj4=salesClass(self.sale)

    def products(self):
        self.product=Toplevel(self.root)
        self.obj5=productsClass(self.product)

    def orders(self):
        self.order=Toplevel(self.root)
        self.obj6=ordersClass(self.order)



if __name__=="__main__":
    root = Tk()
    obj = Main(root)
    root.mainloop()



