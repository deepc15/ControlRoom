import sqlite3 as sl

con = sl.connect(r'F:\Visual Studio Projects\Deepsoumya\repos\ControlRoom\ControlRoom\function.db')

with con:
    con.execute("""
        CREATE TABLE BUTTONS (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            buttonname TEXT,
            buttontext INTEGER
        );
    """)

sql = 'INSERT INTO USER (id, buttonname, buttontext) values(?, ?, ?)'
data = [
    (1, 'name1', 'buttonpath1'),
    (2, 'name2', 'buttonpath2'),
    (3, 'name3', 'buttonpath3')
]

with con:
    con.executemany(sql, data)