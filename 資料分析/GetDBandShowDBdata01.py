from pymysql import *
import streamlit as st

def GetDBdata():
    conn = connect(host='localhost',
                   port=3306,user='root',
                   password='',
                   database='ksu_database',
                   charset='utf8')
    
    cursor_data = conn.cursor()
    
    count = cursor_data.execute('SELECT * FROM student')
    
    print("The number of rows is: %d " % count)
    
    cursor_data.close()
    conn.close()
    
    result = cursor_data.fetchall()
    return(result)

st.success("All of student data from ksu_database.student table is below:\n")
st.write(GetDBdata())