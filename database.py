import sqlite3
conn = sqlite3.connect("test.db")
print("Opened database successfully")
cursor = conn.execute("select id,name,address,salary from Company")
for row in cursor:
    print("Id", row[0])
    print("NAME", row[1])
    print("ADDRESS", row[2])
    print("SALARY", row[3])
print("Operation done successfully....!")
conn.close()    
    