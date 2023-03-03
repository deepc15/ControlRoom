from methods import *
from tkinter import *
from tkinter import ttk
import winapps
from tkinter import filedialog
from addcustfunc import *
import sys
import os
import sqlite3 as sl
import subprocess
import time
from ctypes import windll

# DB Initiation

con = sl.connect(r'F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\function.db')

# Creating and configuring the app background structure
window = Tk()
window.title("Control Room")
window.resizable(0,0)
# Configuring window size and color
# window.configure(width=500, height=300)
window.configure(bg='lightblue')
window.geometry('+%d+%d'%(500,300))
window.overrideredirect(True)

# Some WindowsOS styles, required for task bar integration
GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080

# Frames---------------------------------------------------------------------------------------------------
# Title Bar--------------
def moveapp(e):
    window.geometry(f'+{e.x_root}+{e.y_root}')

def closeapp():
    window.quit()

def minimizeapp():
    global z
    window.state('withdrawn')
    window.overrideredirect(False)
    window.state('iconic')
    z = 1

def set_appwindow(window):
    hwnd = windll.user32.GetParent(window.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    window.wm_withdraw()
    window.after(10, lambda: window.wm_deiconify())
    window.overrideredirect(True)

def frameMapped(event=None):
    global z
    window.overrideredirect(True)
    if z == 1:
        set_appwindow(window)
        z = 0
    
titlebar = Frame(window, relief= 'raised', bg= "darkgreen", bd=0)
titlebar.grid(sticky="ew", row=0, columnspan=2)
titlebar.grid_rowconfigure(0, weight=2)
titlebar.grid_columnconfigure(0, weight=2)
titlebar.bind("<B1-Motion>", moveapp)

titlehead = Frame(titlebar, relief= 'raised', bg= "darkgreen", bd=0)
titlehead.grid(sticky="ew", row=0, column=0)
titlehead.bind("<B1-Motion>", moveapp)

titleclose = Frame(titlebar, relief= 'raised', bg= "darkgreen", bd=0)
titleclose.grid(sticky="ew", row=0, column=1)
titleclose.bind("<B1-Motion>", moveapp)

titletext = Label(titlehead, text="   Control Room   ", bg="darkgreen", font=('Helvetica 11 bold'), fg="white")
titletext.grid(sticky="w",pady=4)
titletext.bind("<B1-Motion>", moveapp)

closelabel = Button(titleclose, text="  _  ", bg="darkgreen", fg="white", relief="raised", bd=1, command=minimizeapp)
closelabel.pack(side=LEFT,pady=4, padx=4)

closelabel = Button(titleclose, text=" ✖ ", bg="darkgreen", fg="white", relief="raised", bd=1, command=closeapp)
closelabel.pack(side=RIGHT,pady=4, padx=4)

"""
titlebar = Frame(window, relief= 'raised', bg= "darkgreen", bd=0)
titlebar.pack(expand=1, fill=X)
titlebar.bind("<B1-Motion>", moveapp)

titletext = Label(titlebar, text="   Control Room   ", bg="darkgreen", font=('Helvetica 11 bold'), fg="white")
titletext.pack(side=LEFT,pady=4)
titlebar.bind("<B1-Motion>", moveapp)

closelabel = Button(titlebar, text=" ✖ ", bg="darkgreen", fg="white", relief="raised", bd=1, command=closeapp)
closelabel.pack(side=RIGHT,pady=4)
"""

# Title Bar--------------

headerframe= Frame(window, relief= 'sunken', bg= "lightblue")
headerframe.grid(row=1, columnspan=2)
headerframe.grid_rowconfigure(0, weight=2)
headerframe.grid_columnconfigure(0, weight=2)

frame= Frame(window, relief= 'sunken', bg= "lightblue")
frame.grid(row=2, columnspan=2)
frame.grid_rowconfigure(0, weight=2)
frame.grid_columnconfigure(0, weight=2)

fsep= Frame(window, relief= 'sunken', bg= "lightblue")
fsep.grid(row=3, columnspan=2)
fsep.grid_rowconfigure(0, weight=2)
fsep.grid_columnconfigure(0, weight=2)

headerframe1= Frame(window, relief= 'sunken', bg= "lightblue")
headerframe1.grid(row=4, columnspan=2)
headerframe1.grid_rowconfigure(0, weight=2)
headerframe1.grid_columnconfigure(0, weight=2)

frame1= Frame(window, relief= 'sunken', bg= "lightblue")
frame1.grid(row=5, columnspan=2)
frame1.grid_rowconfigure(0, weight=2)
frame1.grid_columnconfigure(0, weight=2)

browseframe= Frame(window, relief= 'sunken', bg= "lightblue")
browseframe.grid(row=6, columnspan=2)
browseframe.grid_rowconfigure(0, weight=2)
browseframe.grid_columnconfigure(0, weight=2)

ssep= Frame(window, relief= 'sunken', bg= "lightblue")
ssep.grid(row=7, columnspan=2)
ssep.grid_rowconfigure(0, weight=2)
ssep.grid_columnconfigure(0, weight=2)

advancedframe= Frame(window, relief= 'sunken', bg= "lightblue")
advancedframe.grid(row=8, columnspan=2)
advancedframe.grid_rowconfigure(0, weight=2)
advancedframe.grid_columnconfigure(0, weight=2)

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
label= Label(headerframe, text= "System Applications", font=('Helvetica 10 bold'), bg= "lightblue")
label.pack()

# System App
# row1
showButton = Button(frame, text="Command Prompt", command=system)
showButton.grid(row=1, column=0, padx=10, pady=20)

showButton1 = Button(frame, text="Run", command=system1)
showButton1.grid(row=1, column=1, ipadx=10, pady=20)


label1= Label(headerframe1, text= "Custom Applications", font=('Helvetica 10 bold'), bg= "lightblue")
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
i=0
j=0
with con:
    data = con.execute("SELECT buttonname,buttontext FROM BUTTONFRAMES order by id asc")
    for row in data:
        exec(row[1])
        exec("\n" + row[0] + ".grid(row=" + str(i) + ", column="+ str(j) +", padx=10, pady=20)")
        if j>2:
            i=i+1
            j=0
        else:
            j=j+1

# upload unique

def browseFiles():
    # filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Application","*.exe*"),("all files","*.*")))
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Application","*.exe*"),("Shortcut","*.lnk*"),("Internet Shortcut","*.url*"),))
    list1 = str(filename.title()).split("/")
    str1 = list1[-1].split(".")[0]
    str2 = str1.replace(":"," ").replace("/"," ").replace("."," ").replace("-"," ").replace("?"," ").replace("_"," ").replace("+"," ").replace(";"," ").replace("<"," ").replace(">"," ").replace(","," ").replace("*"," ").replace("&"," ").replace("%"," ").replace("$"," ").replace("#"," ").replace("@"," ").replace("!"," ")
    str3 = str2.split(" ")[0]
    filee = str(filename.title()).replace(" ","").replace(":","").replace("/","").replace(".","").replace("-","").replace("?","").replace("_","").replace("+","").replace(";","").replace("<","").replace(">","").replace(",","").replace("*","").replace("&","").replace("%","").replace("$","").replace("#","").replace("@","").replace("!","")
    if len(str(filename)) != 0:
        sql = 'INSERT INTO BUTTONS (buttonname, buttontext) values(?, ?)'
        data = [
                (str3,
                 "\ndef " + str3 + "():\n\tos.startfile(r'" + str(filename) + "')")
        ]
        with con:
            con.executemany(sql, data)
        """rowcollist = {}
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
                intcol = intcol + 1"""
        sql1 = 'INSERT INTO BUTTONFRAMES (buttonname, buttontext) values(?, ?)'
        data1 = [
                (str3,
                 "\n" +str3 + " = Button(frame1, text='" + str3 + "', command=" + str3 + ", height=1, width=20)\n")   # + filee + ".grid(row=" + str(introw) + ", column="+ str(intcol) +", padx=10, pady=20)")
        ]
        with con:
            con.executemany(sql1, data1)
        # value="\n" +filee + " = Button(frame1, text='" + filee + "', command=addfunc." + filee + ")\n" + filee + ".grid(row=" + str(introw) + ", column="+ str(intcol) +", padx=10, pady=20)"
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

def deleteFrames():
    with con:
        data = con.execute("SELECT buttonname FROM BUTTONFRAMES order by id asc")
        rs = data.fetchone()
        if rs != None:
            os.startfile(r"F:\\Visual Studio Projects\\Deepsoumya\\repos\\ControlRoom\\ControlRoom\\deletecustapp.pyw")
            window.destroy()

advancebutton = Button(advancedframe, text="Delete Custom App...", command=deleteFrames)
advancebutton.grid(row=0, padx=10, pady=20)

window.bind("<Map>", frameMapped)
window.mainloop()