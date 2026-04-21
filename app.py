import sqlite3

db = sqlite3.connect("tree")
cursor = db.cursor()
sql = "SELECT * from treetable;"
cursor.execute(sql)
results = cursor.fetchall()

db.close()