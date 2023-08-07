import sqlite3  
con = sqlite3.connect("Diabetes Database")
cur = con.cursor()
cur.execute("CREATE TABLE data(bsg, exchanges)")
