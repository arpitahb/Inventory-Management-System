from tkinter import *
from tkinter import ttk

class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x500+220+130")
        self.root.title("Inventory Management System   |  Created by Shubham Roy and Arpita Hatibaruah")
        self.root.configure(bg="#F0FDFA")
        self.ent1=StringVar()
        self.ent2=StringVar()
        label3 = Label(self.root, text="Sales Details", font=("Arial", 30), bg="#414C6B", fg="white").place(x=10,
                                                                                                               y=10,
                                                                                                               height=50,
                                                                                                               width=580)
        searchengine = LabelFrame(self.root, text="Search by").place(x=20, y=70, height=60, width=550)
        search = ttk.Combobox(self.root, textvariable=self.ent1,
                              values=("Select", "<1000", "1000-5000", "5000-10000",">10000"), state="readonly",
                              justify=CENTER).place(x=30, y=90, height=20, width=100)
        label1 = Entry(self.root, bd=2, textvariable=self.ent2, relief=RIDGE, bg="#FFFDD0").place(x=140, y=90,
                                                                                                  height=30, width=300)
        label2 = Button(self.root, bd=2, text="Search", bg="#78C5DC").place(x=460, y=90, height=20, width=50)

        tableframe = Frame(self.root, bd=2, relief=RIDGE).place(x=20, y=140, height=500, width=550)

        employeetable = ttk.Treeview(self.root, columns=(
            "Product category", "Product  Name", "Supplier Name", "Sales"), selectmode='browse').place(x=30,
                                                                                           y=150,
                                                                                           height=500,
                                                                                           width=530)



if __name__=="__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()