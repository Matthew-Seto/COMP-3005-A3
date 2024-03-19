import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="660caa4e5c", port="5432")

cur = conn.cursor()

# Creates table 
cur.execute("""CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);
""")

# Inserts student into table
# cur.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
# ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
# ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
# ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
# """)

conn.commit()

cur.close()
conn.close()

def getAllStudents():
    try:
       # Connect to the database
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="660caa4e5c", port="5432")
        cur = conn.cursor()
        
        # Retrieve all records from the students table
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        
        # Display the retrieved records
        print("Student ID | First Name | Last Name | Email | Enrollment Date")
        for row in rows:
            print("{:10} | {:10} | {:10} | {:20} | {}".format(row[0], row[1], row[2], row[3], row[4]))
        
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)

#getAllStudents()

def addStudent(first_name, last_name, email, enrollment_date):
    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="660caa4e5c", port="5432")
        cur = conn.cursor()

        # Insert new student record into database
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))

        # Commit the addition
        conn.commit()

        print("Student Added.")

        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)

#addStudent("Mat", "Seto", "mat.seto@example.com", "2023-09-03")
        
def updateStudentEmail(student_id, new_email):
    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="660caa4e5c", port="5432")
        cur = conn.cursor()

        # Update email address of specified student
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        
        conn.commit()
        
        print("Email address updated successfully.")

        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)

#updateStudentEmail(4, "matseto@example.com")

# Deletes Student
def deleteStudent(student_id):
    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="660caa4e5c", port="5432")
        cur = conn.cursor()
        
        # Delete student based on ID
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        
        conn.commit()
        
        print("Student record deleted successfully.")
        
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)

deleteStudent(4)