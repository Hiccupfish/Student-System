import tkinter as tk
from tkinter import messagebox

import sqlite3

class LearnerManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Learner Management System")

        # Create UI components
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.age_label = tk.Label(root, text="Age")
        self.age_label.grid(row=1, column=0)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1)

        self.grade_label = tk.Label(root, text="Grade")
        self.grade_label.grid(row=2, column=0)
        self.grade_entry = tk.Entry(root)
        self.grade_entry.grid(row=2, column=1)

        self.learner_class_label = tk.Label(root, text="Class")  
        self.learner_class_label.grid(row=3, column=0)
        self.class_entry = tk.Entry(root)
        self.class_entry.grid(row=3, column=1)  # Corrected indentation

        self.add_button = tk.Button(root, text="Add Learner", command=self.add_learner)
        self.add_button.grid(row=6, column=0, columnspan=2)

    def add_learner(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        grade = self.grade_entry.get()
        class_name = self.class_entry.get()  # Changed 'class' to 'class_name'
        
        if name and age and grade and class_name:
            con = sqlite3.connect("StudentSystemv.db")
            cur = con.cursor()
            cur.execute("""INSERT INTO learner(name,age,grade,class_name) VALUES(name,age,grade,class_name)""") 
            
            
            

    
        messagebox.showinfo("Info", f"Learner {name} added successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LearnerManagementSystem(root)
    root.mainloop()
