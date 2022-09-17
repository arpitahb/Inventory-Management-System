from tkinter import *

class companyClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System   |  Created by Shubham Roy and Arpita Hatibaruah")
        self.root.configure(bg="#97DEE7")




if __name__=="__main__":
    root = Tk()
    obj = companyClass(root)
    root.mainloop()