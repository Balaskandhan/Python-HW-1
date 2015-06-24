import sqlite3

conn = sqlite3.connect("zoo.sqlite") #create connection to zoo.sqlite database, creates the database if it doesn't already exist

cursor = conn.cursor() #provides are cursor to the above connection (the means of executing the SQL queries)

# cursor.execute("create table animal_count (name text, count integer)") #execute the create table query
# 
# cursor.execute("insert into animal_count(name, count) values('Elephant', 3)") #inset a row into the animal_count table

cursor.execute("insert into animal_count(name, count) values('Alligator', 5)")

conn.commit() #commit changes to the database

conn.close() #close the connection
