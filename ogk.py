from tkinter import *

root = Tk()
root.geometry("600x400")

list_name = ["Mickey Mouse", "Elsa", "Anna", "Donald Duck"]
sd_name = {"name":"Shinchan",
           "Age":"5"
           }

try :
    print(list_name[5])
    print(sd_name["mom"])
    
except IndexError: 
    messagebox.showinfo("error, This Index is  out of range")
except KeyError() : 
    messagebox.showinfo("error, This Key does not exist")
    
root.mainloop()