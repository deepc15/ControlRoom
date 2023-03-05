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

#con = sl.connect(r'F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\function.db')
con = sl.connect('data\\function.db')

# Creating and configuring the app background structure
window = Tk()
window.title("Control Room")
window.resizable(0,0)
# Configuring window size and color
# window.configure(width=500, height=300)
window.configure(bg='lightgreen')
window.geometry('+%d+%d'%(500,300))
window.overrideredirect(True)

# Some WindowsOS styles, required for task bar integration
GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080

# Frames---------------------------------------------------------------------------------------------------
# Title Bar--------------
global z
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
    
titlebar = Frame(window, relief= 'raised', bg= "lightblue", bd=0)
titlebar.grid(sticky="ew", row=0, columnspan=2)
titlebar.grid_rowconfigure(0, weight=2)
titlebar.grid_columnconfigure(0, weight=2)
titlebar.bind("<B1-Motion>", moveapp)

titlehead = Frame(titlebar, relief= 'raised', bg= "lightblue", bd=0)
titlehead.grid(sticky="ew", row=0, column=0)
titlehead.bind("<B1-Motion>", moveapp)

titleclose = Frame(titlebar, relief= 'raised', bg= "lightblue", bd=0)
titleclose.grid(sticky="ew", row=0, column=1)
titleclose.bind("<B1-Motion>", moveapp)

titletext = Label(titlehead, text="   Control Room   ", bg="lightblue", font=('Helvetica 11 bold'), fg="darkgreen")
titletext.grid(sticky="w",pady=4)
titletext.bind("<B1-Motion>", moveapp)

closelabel = Button(titleclose, text="  _  ", bg="lightblue", fg="darkgreen", relief="raised", bd=1, command=minimizeapp)
closelabel.pack(side=LEFT,pady=4, padx=4)

closelabel = Button(titleclose, text=" ✖ ", bg="lightblue", fg="darkgreen", relief="raised", bd=1, command=closeapp)
# text=" ✖ "
closelabel.pack(side=RIGHT,pady=4, padx=4)

# Title Bar--------------

# FrameList--------------
# format ["Frame Name","Frame Configuration","row","columnspan","width","weight"]
framelist = [
    ["headerframe","window, relief= 'sunken', bg= 'lightgreen'","1","2","0","2"],
    ["frame","window, relief= 'sunken', bg= 'lightgreen'","2","2","0","2"],
    ["fsep","window, relief= 'sunken', bg= 'lightgreen'","3","2","0","2"],
    ["headerframe1","window, relief= 'sunken', bg= 'lightgreen'","4","2","0","2"],
    ["frame1","window, relief= 'sunken', bg= 'lightgreen'","5","2","0","2"],
    ["browseframe","window, relief= 'sunken', bg= 'lightgreen'","6","2","0","2"],
    ["ssep","window, relief= 'sunken', bg= 'lightgreen'","7","2","0","2"],
    ["advancedframe","window, relief= 'sunken', bg= 'lightgreen'","8","2","0","2"],
]

# FrameList--------------

# Fetch Frames-----------
for framesss in framelist:
    exec("\n"+framesss[0]+"= Frame("+framesss[1]+")"+
    "\n"+framesss[0]+".grid(row="+framesss[2]+", columnspan="+framesss[3]+", sticky='ew')"+
    "\n"+framesss[0]+".grid_rowconfigure("+framesss[4]+", weight="+framesss[5]+")"+
    "\n"+framesss[0]+".grid_columnconfigure("+framesss[4]+", weight="+framesss[5]+")")

# main window grid manager
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)

# Images to embed------------------------------------------------------------------------------------------
# showmeimage= ImageTk.PhotoImage(resized_image)

# Craeting Front-end designs to interact-------------------------------------------------------------------
label= Label(headerframe, text= "System Applications", font=('Helvetica 10 bold'), bg= "lightgreen")
label.pack()

# System App
# row1
showButton = Button(frame, text="Command Prompt", command=system, height=1, width=20, bg='darkgreen', fg='white')
showButton.grid(row=1, column=0, pady=20, padx=10)

showButton1 = Button(frame, text="Run", command=system1, height=1, width=20, bg='darkgreen', fg='white')
showButton1.grid(row=1, column=1, pady=20, padx=10)

# seperator
sep1 = ttk.Separator(
    master=fsep,
    orient=HORIZONTAL,
    style='blue.TSeparator',
    class_= ttk.Separator,
    takefocus= 1,
    cursor='plus'    
)
sep1.grid(row=0, sticky="ew")
# sep1.grid_columnconfigure(1, weight=2)

label1= Label(headerframe1, text= "Custom Applications", font=('Helvetica 10 bold'), bg= "lightgreen")
label1.pack()



# Custom App
# add code
i=0
j=0
with con:
    data = con.execute("SELECT buttonname,buttontext FROM BUTTONFRAMES order by id asc")
    for row in data:
        exec(row[1])
        exec("\n" + row[0] + ".grid(row=" + str(i) + ", column="+ str(j) +", padx=10, pady=20)")
        if i==1 and j==1:
            break
        elif j==1:
            i=i+1
            j=0
        else:
            j=j+1

# upload unique

def browseFiles():
    # filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Application","*.exe*"),("all files","*.*")))
    l=0
    m=0
    with con:
        data12 = con.execute("SELECT buttonname,buttontext FROM BUTTONFRAMES order by id asc")
        for row in data12:
            if m==1:
                l=l+1
                m=0
            else:
                m=m+1
    if l==2 and m==0:
        return 0
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
                 "\n" +str3 + " = Button(frame1, text='" + str3 + "', command=" + str3 + ", height=1, width=20, bg='darkgreen', fg='white')\n")   # + filee + ".grid(row=" + str(introw) + ", column="+ str(intcol) +", padx=10, pady=20)")
        ]
        with con:
            con.executemany(sql1, data1)
        # value="\n" +filee + " = Button(frame1, text='" + filee + "', command=addfunc." + filee + ")\n" + filee + ".grid(row=" + str(introw) + ", column="+ str(intcol) +", padx=10, pady=20)"
        window.destroy()
        #os.startfile(r"F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\app.pyw")
        os.startfile(r"data\\app.pyw")

button_explore = Button(browseframe, text = "Add External Applications", command = browseFiles, bg= "lightblue")
button_explore.grid(row=0, padx=10, pady=20)


# seperator
sep2 = ttk.Separator(
    master=ssep,
    orient=HORIZONTAL,
    style='blue.TSeparator',
    class_= ttk.Separator,
    takefocus= 1,
    cursor='plus'    
)
sep2.grid(row=0, sticky="ew")
# sep1.grid_columnconfigure(1, weight=2)

def deleteFrames():
    with con:
        data = con.execute("SELECT buttonname FROM BUTTONFRAMES order by id asc")
        rs = data.fetchone()
        if rs != None:
            #os.startfile(r"F:\\Visual Studio Projects\\Deepsoumya\\repos\\ControlRoom\\ControlRoom\\deletecustapp.pyw")
            os.startfile(r"data\\deletecustapp.pyw")
            window.destroy()

advancebutton = Button(advancedframe, text="Delete Custom App...", command=deleteFrames, bg= "red", fg="white")
advancebutton.grid(row=0, padx=10, pady=20)

window.bind("<Map>", frameMapped)
window.after(10, lambda: set_appwindow(window))
window.mainloop()