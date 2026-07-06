import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
category TEXT,
description TEXT,
amount REAL
)
""")

conn.commit()

# ---------------- FUNCTIONS ----------------

# Add expense
def add_expense():
    date = entry_date.get()
    category = entry_category.get()
    description = entry_desc.get()
    amount = entry_amount.get()

    if date == "" or category == "" or amount == "":
        messagebox.showwarning("Input Error", "Please fill required fields")
        return

    cursor.execute(
        "INSERT INTO expenses(date,category,description,amount) VALUES(?,?,?,?)",
        (date, category, description, amount)
    )

    conn.commit()

    messagebox.showinfo("Success", "Expense Added Successfully!")

    clear_fields()


# View expenses
def view_expenses():

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    text_box.delete("1.0", tk.END)

    text_box.insert(tk.END, "ID | Date | Category | Description | Amount\n")
    text_box.insert(tk.END, "---------------------------------------------\n")

    for row in rows:
        text_box.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}\n")


# Total expense
def total_expense():

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    messagebox.showinfo("Total Expense", f"Total Expense = {total}")


# Delete expense
def delete_expense():

    expense_id = entry_delete.get()

    if expense_id == "":
        messagebox.showwarning("Error", "Enter Expense ID")
        return

    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()

    messagebox.showinfo("Deleted", "Expense Deleted")

    entry_delete.delete(0, tk.END)


# Clear input fields
def clear_fields():
    entry_date.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_desc.delete(0, tk.END)
    entry_amount.delete(0, tk.END)


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("550x500")
root.configure(bg="lightblue")

title = tk.Label(root, text="Personal Expense Tracker", font=("Arial", 18, "bold"), bg="lightblue")
title.pack(pady=10)

# Date
tk.Label(root, text="Date (DD-MM-YYYY)", bg="lightblue").pack()
entry_date = tk.Entry(root, width=30)
entry_date.pack()

# Category
tk.Label(root, text="Category", bg="lightblue").pack()
entry_category = tk.Entry(root, width=30)
entry_category.pack()

# Description
tk.Label(root, text="Description", bg="lightblue").pack()
entry_desc = tk.Entry(root, width=30)
entry_desc.pack()

# Amount
tk.Label(root, text="Amount", bg="lightblue").pack()
entry_amount = tk.Entry(root, width=30)
entry_amount.pack()

# Buttons
tk.Button(root, text="Add Expense", width=20, command=add_expense).pack(pady=5)

tk.Button(root, text="View Expenses", width=20, command=view_expenses).pack(pady=5)

tk.Button(root, text="Total Expense", width=20, command=total_expense).pack(pady=5)

# Delete section
tk.Label(root, text="Enter Expense ID to Delete", bg="lightblue").pack(pady=5)
entry_delete = tk.Entry(root, width=20)
entry_delete.pack()

tk.Button(root, text="Delete Expense", width=20, command=delete_expense).pack(pady=5)

# Text box
text_box = tk.Text(root, height=12, width=65)
text_box.pack(pady=10)

root.mainloop()
