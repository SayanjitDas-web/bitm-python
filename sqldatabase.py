import sqlite3

con = sqlite3.connect("student.db")

cursor = con.cursor()

cursor.execute(
    "DELETE FROM students WHERE name = ?",
    ("Sayanjit",)
)

con.commit()
con.close()