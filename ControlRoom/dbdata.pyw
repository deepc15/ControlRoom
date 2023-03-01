import sqlite3 as sl

con = sl.connect(r'F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\function.db')

with con:
    data = con.execute("SELECT * FROM BUTTONS WHERE buttonname = 'name1'")
    for row in data:
        print(row)