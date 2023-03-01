from methods import *
from tkinter import *
from tkinter import ttk
import winapps
from tkinter import filedialog
import addcustfunc as addfunc
import sys
import os
import sqlite3 as sl

con = sl.connect(r'F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\function.db')

# Creating and configuring the app background structure
window = Tk()
window.title("Control Room")
window.resizable(0,0)
# Configuring window size and color
# window.configure(width=500, height=300)
window.configure(bg='lightblue')
# window.geometry("700x350")

# Frames---------------------------------------------------------------------------------------------------
headerframe= Frame(window, relief= 'sunken', bg= "lightblue")
headerframe.grid(row=0, column=0)
headerframe.grid_rowconfigure(0, weight=1)
headerframe.grid_columnconfigure(0, weight=1)

frame= Frame(window, relief= 'sunken', bg= "lightblue")
frame.grid(row=1, column=0)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

fsep= Frame(window, relief= 'sunken', bg= "lightblue")
fsep.grid(row=2, column=0)
fsep.grid_rowconfigure(0, weight=1)
fsep.grid_columnconfigure(0, weight=1)

headerframe1= Frame(window, relief= 'sunken', bg= "lightblue")
headerframe1.grid(row=3, column=0)
headerframe1.grid_rowconfigure(0, weight=1)
headerframe1.grid_columnconfigure(0, weight=1)

frame1= Frame(window, relief= 'sunken', bg= "lightblue")
frame1.grid(row=4, column=0)
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)

browseframe= Frame(window, relief= 'sunken', bg= "lightblue")
browseframe.grid(row=5, column=0)
browseframe.grid_rowconfigure(0, weight=1)
browseframe.grid_columnconfigure(0, weight=1)

ssep= Frame(window, relief= 'sunken', bg= "lightblue")
ssep.grid(row=6, column=0)
ssep.grid_rowconfigure(0, weight=1)
ssep.grid_columnconfigure(0, weight=1)

advancedframe= Frame(window, relief= 'sunken', bg= "lightblue")
advancedframe.grid(row=7, column=0)
advancedframe.grid_rowconfigure(0, weight=1)
advancedframe.grid_columnconfigure(0, weight=1)

# main window grid manager
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)

# Images to embed------------------------------------------------------------------------------------------
showmeimage= ImageTk.PhotoImage(resized_image)
"""
showmeimage1= ImageTk.PhotoImage(resized_image1)
showmeimage2= ImageTk.PhotoImage(resized_image2)
showmeimage3= ImageTk.PhotoImage(resized_image3)"""

# Craeting Front-end designs to interact-------------------------------------------------------------------
label= Label(headerframe, text= "System Applications", font=('Helvetica 13 bold'), bg= "lightblue")
label.pack()

# System App
# row1
showButton = Button(frame, text="Command Prompt", command=system)
showButton.grid(row=1, column=0, padx=10, pady=20)

showButton1 = Button(frame, text="Run", command=system1)
showButton1.grid(row=1, column=1, ipadx=10, pady=20)


label1= Label(headerframe1, text= "Custom Applications", font=('Helvetica 13 bold'), bg= "lightblue")
label1.pack()

# seperator
ttk.Separator(
    master=fsep,
    orient=HORIZONTAL,
    style='blue.TSeparator',
    class_= ttk.Separator,
    takefocus= 1,
    cursor='plus'    
).grid(row=2, columnspan=2, ipadx=120, pady=10)

# Custom App
# add code
with con:
    data = con.execute("SELECT * FROM BUTTONS")
    for row in data:
        print(row)

# DB Initiation

con = sl.connect(r'F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\function.db')

# upload unique

def browseFiles():
    # filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Application","*.exe*"),("all files","*.*")))
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Application","*.exe*"),("Shortcut","*.lnk*"),("Internet Shortcut","*.url*"),))
    if len(str(filename)) != 0:
        sql = 'INSERT INTO BUTTONS (id, buttonname, buttontext) values(?, ?, ?)'
        data = [
                (1,
                 str(filename.title()).replace(" ","").replace(":","").replace("/","").replace(".",""),
                 "\ndef " + str(filename.title()).replace(" ","").replace(":","").replace("/","").replace(".","") + "():\n\tos.startfile(r'" + str(filename) + "')")
        ]
        with con:
            con.executemany(sql, data)
        rowcollist = {}
        for child in frame1.winfo_children():
            info = child.grid_info()
            row_info = info['row']
            col_info = info['column']
            if not rowcollist.keys():
                rowcollist[int(row_info)] = int(col_info)
            elif int(max(rowcollist.keys())) < int(row_info):
                rowcollist[int(row_info)] = int(col_info)
            elif int(max(rowcollist.keys())) == int(row_info) and int(rowcollist[int(max(rowcollist.keys()))]) < int(col_info):
                rowcollist[int(row_info)] = int(col_info)
        if not frame1.winfo_children():
            introw = 0
            intcol = 0
        else:
            maxrow = max(rowcollist.keys())
            maxcol = rowcollist[maxrow]
            introw = int(maxrow)
            intcol = int(maxcol)
            if intcol >= 3:
                intcol = 0
                introw = introw + 1
            else:
                intcol = intcol + 1
        feature = str(filename.title()).replace(" ","").replace(":","").replace("/","").replace(".","")
        sql1 = 'INSERT INTO BUTTONFRAMES (id, buttonname, buttontext) values(?, ?, ?)'
        data1 = [
                (1,
                 str(filename.title()).replace(" ","").replace(":","").replace("/","").replace(".",""),
                 "\n" +feature + " = Button(frame1, text='" + feature + "', command=addfunc." + feature + ")\n" + feature + ".grid(row=" + str(introw) + ", column="+ str(intcol) +", padx=10, pady=20)")
        ]
        with con:
            con.executemany(sql1, data1)
        value="\n" +feature + " = Button(frame1, text='" + feature + "', command=addfunc." + feature + ")\n" + feature + ".grid(row=" + str(introw) + ", column="+ str(intcol) +", padx=10, pady=20)"
        window.destroy()
        os.startfile(r"F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\app.pyw")

button_explore = Button(browseframe, text = "Add External Applications", command = browseFiles)
button_explore.grid(row=0, padx=10, pady=20)

# seperator
ttk.Separator(
    master=ssep,
    orient=HORIZONTAL,
    style='blue.TSeparator',
    class_= ttk.Separator,
    takefocus= 1,
    cursor='plus'    
).grid(row=2, columnspan=2, ipadx=120, pady=10)

# Advanced Button
advancebutton = Button(advancedframe, text="Advance Features...")
advancebutton.grid(row=0, padx=10, pady=20)

window.mainloop()