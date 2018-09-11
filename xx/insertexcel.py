import sqlite3

def createDataBase():
    cn = sqlite3.connect('check.db')
    cn.execute('''CREATE TABLE IF NOT EXISTS TB_CHECK
    (ID integer PRIMARY KEY AUTOINCREMENT,
    NUMBER INTEGER,
    ITEM TEXT,
    REFERENCE TEXT,
    SUMMARY TEXT,
    OBJECT TEXT,
    METHOD TEXT,
    CONDITION TEXT,
    VALUE TEXT,
    RESULT TEXT,
    SCORE TEXT,
    REMARKS TEXT,
    PROVINCE TEXT,
    TIME TEXT);''')

    cn.execute('''CREATE TABLE IF NOT EXISTS TB_SCORE
    (ID integer PRIMARY KEY AUTOINCREMENT,
    PROVINCE TEXT,
    TIME TEXT,
    FILETYPE TEXT,
    SCORE INTEGER);''')

if __name__ == '__main__':
    createDataBase()