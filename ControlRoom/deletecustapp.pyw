from tkinter import *
import os
import sqlite3 as sl
# from app import window as win

# DB Initiation

con = sl.connect(r'F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\function.db')

# Creating and configuring the app background structure
window1 = Tk()
window1.title("Delete Custom App")
window1.resizable(0,0)
# Configuring window size and color
# window.configure(width=500, height=300)
window1.configure(bg='lightblue')
window1.geometry("700x350")

frame1= Frame(window1, relief= 'sunken', bg= "lightblue")
frame1.grid(row=4, column=0)
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)

with con:
    data = con.execute("SELECT buttontext FROM BUTTONFRAMES order by id asc")
    for row in data:
        exec(row[0])

with con:
    data1 = con.execute("SELECT butttonname FROM BUTTONFRAMES order by id asc")
    for row1 in data1:
        # exec("\n"+ row[0] +"_1 = IntVar()\n" + row[0] + " = " + "Checkbutton(window, text = '"+ row[0] +"', variable="+ row[0] +"_1, onvalue = 1, offvalue = 0, height = 2, width = 10)")
        exec("\ndef "+ row1[0] +":\n\twith con:\n\t\tdata2 = "+
             "con.execute('delete from BUTTONFRAMES where buttonname="+row1[0]+"')\n\t\tdata3 ="+
             " con.execute('delete from BUTTONS where buttonname="+row1[0]+"')"+
             "\n\tos.startfile(r'F:\\Visual Studio Projects\\Deepsoumya\\repos\\ControlRoom\\ControlRoom\\app.pyw')")

window1.mainloop()