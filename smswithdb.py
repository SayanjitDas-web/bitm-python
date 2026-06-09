import tkinter as tk
import sqlite3

conn = sqlite3.connect("student.db")

class StudentManagementSystem:
    def __init__(self):
        self.cursor = conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            roll INTEGER,
            year INTEGER
        )
        """)
        
        conn.commit()
        
    def add_data(self,name,age,roll,year):
        self.cursor.execute(
            "INSERT INTO students (name, age, roll, year) VALUES ( ?, ?, ?, ?)",
            (name,age,roll,year)
        )
        conn.commit()
        
    def get_all_data(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()
    
    def delete_data(self,student_id):
        self.cursor.execute("DELETE FROM students WHERE id = ?",(student_id,))
        conn.commit()
        
    