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
    cur.execute('''CREATE TABLE IF NOT EXISTS teacher (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email STRING NOT NULL,
                   password STRING NOT NULL)'''
        
    )
    
    
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

def retrieve_teacher(email, password):
    try:
        # Using a context manager for the connection ensures it is closed properly
        with sqlite3.connect("StudentSystemv.db") as con:
            cur = con.cursor()
            
            # Executing the query with parameters to protect against SQL injection
            cur.execute("SELECT email, password FROM teacher WHERE email=? AND password=?", (email, password))
            
            # Fetching the first (and only) row of the result set
            result = cur.fetchone()
            
            # If a result is found, return it
            if result:
                return result  # This will be a tuple (email, password)
            else:
                # If no result is found, return None or a suitable message
                return None
    except sqlite3.Error as e:
        # Handling any database errors
        print(f"An error occurred: {e}")
        return None
    
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

def searchByName( name):
    con = sqlite3.connect("StudentSystemv.db")
    cur = con.cursor()
    
    cur.execute("SELECT name,surname,grade,class,contact FROM learner WHERE name LIKE ?", ('%' + name + '%',))
    rows=cur.fetchall()
    con.close()
    return rows
    


create_database()
