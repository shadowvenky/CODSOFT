import csv
import os
from datetime import datetime
from tkinter import Tk, Label, Entry, Button, messagebox

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance App")
        self.root.geometry("400x300")

        self.label_name = Label(root, text="Enter Name:", font=("Arial", 14))
        self.label_name.pack(pady=10)

        self.entry_name = Entry(root, font=("Arial", 14))
        self.entry_name.pack(pady=10)

        self.mark_button = Button(root, text="Mark Attendance", font=("Arial", 14), command=self.mark_attendance)
        self.mark_button.pack(pady=10)

        self.show_button = Button(root, text="Show Attendance", font=("Arial", 14), command=self.show_attendance)
        self.show_button.pack(pady=10)

    def mark_attendance(self):
        name = self.entry_name.get().strip()
        if not name:
            messagebox.showerror("Error", "Name cannot be empty!")
            return

        filename = "attendance.csv"
        is_new_file = not os.path.exists(filename)

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            if is_new_file:
                writer.writerow(["Name", "Date", "Time"])

            current_time = datetime.now()
            date = current_time.strftime("%Y-%m-%d")
            time = current_time.strftime("%H:%M:%S")
            writer.writerow([name, date, time])

        messagebox.showinfo("Success", f"Attendance marked for {name}.")
        self.entry_name.delete(0, 'end')

    def show_attendance(self):
        filename = "attendance.csv"
        if not os.path.exists(filename):
            messagebox.showinfo("Info", "No attendance records found.")
            return

        with open(filename, "r") as file:
            records = file.readlines()

        if len(records) <= 1:
            messagebox.showinfo("Info", "No attendance records found.")
            return

        attendance_window = Tk()
        attendance_window.title("Attendance Records")
        attendance_window.geometry("400x400")

        Label(attendance_window, text="Attendance Records", font=("Arial", 16)).pack(pady=10)
        
        for record in records:
            Label(attendance_window, text=record.strip(), font=("Arial", 12), anchor="w", justify="left").pack(anchor="w", padx=10)

        attendance_window.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = AttendanceApp(root)
    root.mainloop()
