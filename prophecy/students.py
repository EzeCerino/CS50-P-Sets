import csv

from cs50 import SQL

# Open database
db = SQL("sqlite:///roster.db")

# Se creo la tabla de houses

#new = db.execute("SELECT house, head FROM students GROUP BY house")
#for row in new:
#    db.execute("INSERT INTO houses (house_name,head_house) VALUES (?,?)",row["house"],row["head"])

houses = db.execute("SELECT id, house_name FROM houses")
for house in houses:
    print(house["house_name"])
    new = db.execute("SELECT id FROM students WHERE house = ?",house["house_name"])
    for id in new:
        db.execute("INSERT INTO student_to_house (house_id,student_id) VALUES (?,?)",house["id"],id["id"])
        #print(id["id"])

#print(new)