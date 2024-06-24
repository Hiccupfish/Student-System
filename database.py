import sqlite3

def create_database():
    con = sqlite3.connect("StudentSystemv.db")
    cur = con.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS learner (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT)''')
    
    
    cur.execute('''CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    learner_id INTEGER,
                    subject TEXT NOT NULL,
                    score INTEGER,
                    FOREIGN KEY (learner_id) REFERENCES learners(id))''')
    
    con.commit()
    con.close()
create_database()
create_database()