import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry

# Replace with your own database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "yourpassword",
    "database": "school_db"
}

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("980x640")
        self.root.title("Student Management System")
        self.root.resizable(width=False, height=False)
        self.root.minsize(900, 640)

        # Database connection
        self.conn = None
        self.cursor = None
        self.connect_to_db()

        # Form frame
        form_frame = tk.LabelFrame(self.root, text="Student Data", padx=10, pady=10)
        form_frame.pack(fill="x", padx=10, pady=10)

        # Entry fields
        self.entries = {}

        # Student No
        tk.Label(form_frame, text="Student No").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entries["student_no"] = tk.Entry(form_frame, width=20)
        self.entries["student_no"].grid(row=0, column=1, padx=5, pady=5)

        # Name
        tk.Label(form_frame, text="Name").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entries["name"] = tk.Entry(form_frame, width=20)
        self.entries["name"].grid(row=1, column=1, padx=5, pady=5)

        # Course
        tk.Label(form_frame, text="Course").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entries["course"] = tk.Entry(form_frame, width=20)
        self.entries["course"].grid(row=2, column=1, padx=5, pady=5)

        # Date of Birth (Date Picker)
        tk.Label(form_frame, text="Date of Birth").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entries["dob"] = DateEntry(form_frame, width=18, background='darkblue',
                                        foreground='white', borderwidth=2, year=2000,
                                        date_pattern='yyyy-mm-dd')
        self.entries["dob"].grid(row=3, column=1, padx=5, pady=5)

        # Gender (Drop-down)
        tk.Label(form_frame, text="Gender").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entries["gender"] = ttk.Combobox(form_frame, values=["Male", "Female", "Other"],
                                              state="readonly", width=18)
        self.entries["gender"].grid(row=4, column=1, padx=5, pady=5)
        self.entries["gender"].current(0)

        # City
        tk.Label(form_frame, text="City").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.entries["city"] = tk.Entry(form_frame, width=20)
        self.entries["city"].grid(row=5, column=1, padx=5, pady=5)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", pady=10)

        tk.Button(btn_frame, text="Add Student", command=self.add_student).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Update Student", command=self.update_student).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Delete Student", command=self.delete_student).pack(side="left", padx=10)
        tk.Button(btn_frame, text="View Students", command=self.view_students).pack(side="left", padx=10)

        # 🔍 Search Frame
        search_frame = tk.LabelFrame(self.root, text="Search Student", padx=10, pady=10)
        search_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(search_frame, text="Search by Student No or Name").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(search_frame, text="Search", command=self.search_records).grid(row=0, column=2, padx=10)

        # 📊 Treeview Frame
        tree_frame = tk.Frame(self.root)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(tree_frame, columns=("student_no", "name", "course", "dob", "gender", "city"), show="headings")
        self.tree.heading("student_no", text="Student No")
        self.tree.heading("name", text="Name")
        self.tree.heading("course", text="Course")
        self.tree.heading("dob", text="DOB")
        self.tree.heading("gender", text="Gender")
        self.tree.heading("city", text="City")

        self.tree.column("student_no", width=100)
        self.tree.column("name", width=150)
        self.tree.column("course", width=120)
        self.tree.column("dob", width=100)
        self.tree.column("gender", width=100)
        self.tree.column("city", width=120)

        self.tree.pack(fill="both", expand=True)

        # Load all records initially
        self.view_students()

    def connect_to_db(self):
        try:
            self.conn = mysql.connector.connect(**db_config)
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database connection failed: {err}")

    def ensure_connection(self):
        if self.conn is None or not self.conn.is_connected():
            self.connect_to_db()

    def add_student(self):
        self.ensure_connection()
        student_no = self.entries["student_no"].get()
        name = self.entries["name"].get()
        course = self.entries["course"].get()
        dob = self.entries["dob"].get_date()
        gender = self.entries["gender"].get()
        city = self.entries["city"].get()

        try:
            sql = "INSERT INTO students (student_no, name, course, dob, gender, city) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (student_no, name, course, dob, gender, city))
            self.conn.commit()
            messagebox.showinfo("Success", "Student added successfully")
            self.view_students()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to add student: {err}")

    def update_student(self):
        self.ensure_connection()
        student_no = self.entries["student_no"].get()
        name = self.entries["name"].get()
        course = self.entries["course"].get()
        dob = self.entries["dob"].get_date()
        gender = self.entries["gender"].get()
        city = self.entries["city"].get()

        try:
            sql = "UPDATE students SET name=%s, course=%s, dob=%s, gender=%s, city=%s WHERE student_no=%s"
            self.cursor.execute(sql, (name, course, dob, gender, city, student_no))
            self.conn.commit()
            messagebox.showinfo("Success", "Student updated successfully")
            self.view_students()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to update student: {err}")

    def delete_student(self):
        self.ensure_connection()
        student_no = self.entries["student_no"].get()
        try:
            sql = "DELETE FROM students WHERE student_no=%s"
            self.cursor.execute(sql, (student_no,))
            self.conn.commit()
            messagebox.showinfo("Success", "Student deleted successfully")
            self.view_students()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to delete student: {err}")

    def view_students(self):
        self.ensure_connection()
        try:
            self.cursor.execute("SELECT * FROM students")
            rows = self.cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to fetch students: {err}")

    def search_records(self):
        self.ensure_connection()
        keyword = self.search_entry.get().strip()
        try:
            # Use LIKE for both student_no and name to allow partial matches
            sql = "SELECT * FROM students WHERE student_no LIKE %s OR name LIKE %s"
            self.cursor.execute(sql, (f"%{keyword}%", f"%{keyword}%"))
            rows = self.cursor.fetchall()

            # Clear existing rows in Treeview
            self.tree.delete(*self.tree.get_children())

            if rows:
                for row in rows:
                    self.tree.insert("", "end", values=row)
            else:
                messagebox.showinfo("Search Result", "No matching student found.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to search records: {err}")
    def clear_form(self):
        """Clear all entry fields in the form."""
        try:
            self.entries["student_no"].delete(0, tk.END)
            self.entries["name"].delete(0, tk.END)
            self.entries["course"].delete(0, tk.END)
            self.entries["dob"].set_date("")   # reset DateEntry
            self.entries["gender"].set("")     # reset Combobox
            self.entries["city"].delete(0, tk.END)
        except Exception as err:
            messagebox.showerror("Error", f"Failed to clear form: {err}")


def __del__(self):
    """Destructor to close database connection when the app is closed."""
    try:
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None and self.conn.is_connected():
            self.conn.close()
    except Exception as err:
        print(f"Error closing database connection: {err}")

    def search_records(self):
        self.ensure_connection()
        keyword = self.search_entry.get().strip()
        try:
            # Use LIKE for both student_no and name to allow partial matches
            sql = "SELECT * FROM students WHERE student_no LIKE %s OR name LIKE %s"
            self.cursor.execute(sql, (f"%{keyword}%", f"%{keyword}%"))
            rows = self.cursor.fetchall()

            # Clear existing rows in Treeview
            self.tree.delete(*self.tree.get_children())

            if rows:
                for row in rows:
                    self.tree.insert("", "end", values=row)
            else:
                messagebox.showinfo("Search Result", "No matching student found.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to search records: {err}")
