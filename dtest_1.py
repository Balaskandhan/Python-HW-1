import sqlite3

conn = sqlite3.connect("zoo.sqlite")

cursor = conn.cursor()

result = cursor.execute("select * from animal_count")

print(result.fetchall())

conn.commit()

conn.close()
