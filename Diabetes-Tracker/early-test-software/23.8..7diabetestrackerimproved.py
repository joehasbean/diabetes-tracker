import sqlite3

con = sqlite3.connect("DiabetesDatabase.db")
cur = con.cursor()

# Create a table with specified column names, data types, and a primary key
cur.execute("""
    CREATE TABLE IF NOT EXISTS diabetes_data (
        id INTEGER PRIMARY KEY,
        bsg REAL,
        exchanges INTEGER
    )
""")

con.commit()
con.close()

