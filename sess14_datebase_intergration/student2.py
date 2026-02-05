# python script to demonstrate MySQL database CRUD operations on the command line
# NB: Ensure you installed the mysql python connector => pip install mysql-connector-python

import mysql.connector
from db_conn import db_config
from student import Student


# Function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mysql.connector.Error as error:
        print(f"Error: unable to connect to MySQL database:\n{error}")
        return None


# Function to close the connection
def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Closed connection to database")


# Function to read students
def read_students(connection):
    try:
        cursor = connection.cursor()
        select_query = "SELECT student_no, name, birthdate, gender, city FROM students"
        cursor.execute(select_query)
        students = cursor.fetchall()
        for student in students:
            student_obj = Student(*student)
            print(student_obj)
    except mysql.connector.Error as error:
        print(f"Error: unable to get student details\n{error}")
    finally:
        cursor.close()


# Function to insert/add a student record into the students database
def insert_student(connection, student):
    try:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO students (student_no, name, birthdate, gender, city)
            VALUES (%s, %s, %s, %s, %s)
        """
        student_data = (student.student_no, student.name, student.birthdate, student.gender, student.city)
        cursor.execute(insert_query, student_data)
        connection.commit()
        print(f"Student {student.name} inserted successfully")
    except mysql.connector.Error as error:
        print(f"Error: unable to insert student record\n{error}")
    finally:
        cursor.close()


# Function to update/modify student details
def update_student(connection, student):
    try:
        cursor = connection.cursor()
        update_query = """
            UPDATE students
            SET name = %s, birthdate = %s, gender = %s, city = %s
            WHERE student_no = %s
        """
        student_data = (student.name, student.birthdate, student.gender, student.city, student.student_no)
        cursor.execute(update_query, student_data)
        connection.commit()
        if cursor.rowcount > 0:
            print(f"Student {student.name} updated successfully")
        else:
            print(f"Student {student.student_no} does not exist")
    except mysql.connector.Error as error:
        print(f"Error: unable to update student details\n{error}")
    finally:
        cursor.close()


# Function to delete a student record from the database
def delete_student(connection, student_no):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM students WHERE student_no = %s"
        cursor.execute(delete_query, (student_no,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"Student {student_no} deleted successfully")
        else:
            print(f"Student {student_no} does not exist")
    except mysql.connector.Error as error:
        print(f"Error: unable to delete student record\n{error}")
    finally:
        cursor.close()


# Example usage
if __name__ == "__main__":
    conn = connect_to_database()
    if conn:
        # Read all students
        read_students(conn)

        # Insert a new student
        new_student = Student("S001", "Alice", "2000-05-15", "female", "Nairobi")
        insert_student(conn, new_student)

        # Update student details
        updated_student = Student("S001", "Alice W.", "2000-05-15", "female", "Mombasa")
        update_student(conn, updated_student)

        # Delete a student
        delete_student(conn, "S001")

        # Close connection
        close_connection(conn)
