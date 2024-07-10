import sqlite3

def create_database():
    con = sqlite3.connect("StudentSystemv.db")
    cur = con.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS learner (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                dob INTEGER,
                grade INTEGER,
                contact INTEGER,
                class TEXT)''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    learner_id INTEGER,
                    subject TEXT NOT NULL,
                    score INTEGER,
                    FOREIGN KEY (learner_id) REFERENCES learner(id))''')  # Corrected table name
    
    con.commit()
    con.close()
#adds the learmner to the database
    
def add_learner(name, surname, grade, contact, class_name, dob):
    con = sqlite3.connect("StudentSystemv.db")
    cur = con.cursor()
    
    cur.execute("INSERT INTO learner (name, surname, grade, contact, class, dob) VALUES (?, ?, ?, ?, ?, ?)",
                (name, surname, grade, contact, class_name, dob))
    
    con.commit()
    con.close()
    
#update the leaner on the database    
def update_learner(id, name, surname, grade, contact, class_name, dob):
    con = sqlite3.connect("StudentSystemv.db")
    cur = con.cursor()
    
    cur.execute("UPDATE learner SET name = ?, surname = ?, grade = ?, contact = ?, class = ?, dob = ? WHERE id = ?",
                (name, surname, grade, contact, class_name, dob, id))
    
    con.commit()
    con.close()
    
def delete_learner(id):
    con = sqlite3.connect("StudentSystemv.db")
    cur = con.cursor()
    
    cur.execute("DELETE FROM learner WHERE id = ?", (id,))
    
    con.commit()
    con.close()
    
def select_learners():
    con = sqlite3.connect("StudentSystemv.db")
    cur = con.cursor()
    
    cur.execute("SELECT * FROM learner")
    rows = cur.fetchall()
    
    con.close()
    return rows


create_database()
