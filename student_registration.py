
import tkinter as tk
from tkinter import messagebox


def register_student():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    course = course_entry.get().strip()
    email = email_entry.get().strip()

    if not name or not age or not course or not email:
        messagebox.showwarning(
            "Missing Details",
            "Please fill in all the fields."
        )
        return

    if not age.isdigit() or int(age) <= 0:
        messagebox.showwarning(
            "Invalid Age",
            "Please enter a valid positive age."
        )
        return

    messagebox.showinfo(
        "Registration Successful",
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Course: {course}\n"
        f"Email: {email}"
    )


root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x420")
root.resizable(False, False)

heading = tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 16, "bold")
)
heading.pack(pady=20)

tk.Label(root, text="Full Name").pack()
name_entry = tk.Entry(root, width=35)
name_entry.pack(pady=5)

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root, width=35)
age_entry.pack(pady=5)

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root, width=35)
course_entry.pack(pady=5)

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=35)
email_entry.pack(pady=5)

register_button = tk.Button(
    root,
    text="Register Student",
    command=register_student
)
register_button.pack(pady=20)

root.mainloop()
