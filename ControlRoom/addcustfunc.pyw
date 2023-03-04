import os
import sqlite3 as sl

# con = sl.connect(r'F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\function.db')
con = sl.connect(r'data\function.db')

with con:
    data = con.execute("SELECT buttontext FROM BUTTONS order by id asc")
    for row in data:
        exec(row[0])