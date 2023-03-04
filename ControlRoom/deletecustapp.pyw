from tkinter import *
import os
import sqlite3 as sl
from ctypes import windll
#from app import window as win

# DB Initiation

#con = sl.connect(r'F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\function.db')
con = sl.connect(r'data\function.db')

# Creating and configuring the app background structure
window1 = Tk()
window1.title("Delete Custom App")
window1.resizable(0,0)
# Configuring window size and color
# window.configure(width=500, height=300)
window1.configure(bg='lightgreen')
window1.geometry('+%d+%d'%(500,300))
window1.overrideredirect(True)

# Title Bar--------------
# Some WindowsOS styles, required for task bar integration
GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080

def moveapp(e):
    window1.geometry(f'+{e.x_root}+{e.y_root}')

def minimizeapp():
    global dele
    window1.state('withdrawn')
    window1.overrideredirect(False)
    window1.state('iconic')
    dele = 1

def closeframe():
    window1.destroy()
    # os.startfile(r'F:\\Visual Studio Projects\\Deepsoumya\\repos\\ControlRoom\\ControlRoom\\app.pyw')
    os.startfile(r'data\app.pyw')

def set_appwindow(window1):
    hwnd = windll.user32.GetParent(window1.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    window1.wm_withdraw()
    window1.after(10, lambda: window1.wm_deiconify())
    window1.overrideredirect(True)

def frameMapped(event=None):
    global dele
    window1.overrideredirect(True)
    if dele == 1:
        set_appwindow(window1)
        dele = 0
    
titlebar = Frame(window1, relief= 'raised', bg= "lightblue", bd=0)
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

titletext = Label(titlehead, text="   Delete Custom Apps   ", bg="lightblue", font=('Helvetica 11 bold'), fg="darkgreen")
titletext.grid(sticky="w",pady=4)
titletext.bind("<B1-Motion>", moveapp)

closelabel = Button(titleclose, text="  _  ", bg="lightblue", fg="darkgreen", relief="raised", bd=1, command=minimizeapp)
closelabel.pack(side=LEFT,pady=4, padx=4)

closelabel = Button(titleclose, text=" ✖ ", bg="lightblue", fg="darkgreen", relief="raised", bd=1, command=closeframe)
closelabel.pack(side=RIGHT,pady=4, padx=4)

# Title Bar--------------

frame1= Frame(window1, relief= 'sunken', bg= "lightgreen")
frame1.grid(row=1, column=0)
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)

footerframe= Frame(window1, relief= 'sunken', bg= "lightgreen")
footerframe.grid(row=2, column=0)
footerframe.grid_rowconfigure(0, weight=1)
footerframe.grid_columnconfigure(0, weight=1)

with con:
    data1 = con.execute("SELECT buttonname FROM BUTTONFRAMES order by id asc")
    for row1 in data1:
        # exec("\n"+ row[0] +"_1 = IntVar()\n" + row[0] + " = " + "Checkbutton(window, text = '"+ row[0] +"', variable="+ row[0] +"_1, onvalue = 1, offvalue = 0, height = 2, width = 10)")
        """exec("\ndef "+ row1[0] +"():\n\twith con:\n\t\tdata2 = "+
             "con.execute('delete from BUTTONFRAMES where buttonname=\""+row1[0]+"\"')\n\t\tdata3 ="+
             " con.execute('delete from BUTTONS where buttonname=\""+row1[0]+"\"')"+
             "\n\tos.startfile(r'F:\\Visual Studio Projects\\Deepsoumya\\repos\\ControlRoom\\ControlRoom\\app.pyw')\n\twindow1.destroy()")"""
        exec("\ndef "+ row1[0] +"():\n\twith con:\n\t\tdata2 = "+
             "con.execute('delete from BUTTONFRAMES where buttonname=\""+row1[0]+"\"')\n\t\tdata3 ="+
             " con.execute('delete from BUTTONS where buttonname=\""+row1[0]+"\"')"+
             "\n\tos.startfile(r'data\app.pyw')\n\twindow1.destroy()")

with con:
    i=0
    j=0
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

def disable_event():
   pass

"""
close = Button(footerframe, text="Close", command=closeframe)
close.grid(row=0, padx=10, pady=20)"""

window1.protocol("WM_DELETE_WINDOW", disable_event)
window1.bind("<Map>", frameMapped)
window1.mainloop()