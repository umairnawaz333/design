import pyodbc as py
from PyQt5 import QtCore,QtWidgets
conn = py.connect('Driver={SQL Server};'
                      'Server=UMAIR;'
                      'password='
                      'Database=PSL;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
def get(query):
    try:
        l=[]
        for row in cursor.execute(query):
            l.append(row)
        return l

    except:
        return 'Can\'t process'
