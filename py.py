import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to handle movie booking
def book_movie():
    title = movie_var.get()
    user_name = name_entry.get()
    showtime = showtime_var.get()
    num_seats = seats_entry.get()
    
    if title == "Select a Movie":
        messagebox.showinfo("Error", "Please select a movie.")
        return

    if not user_name or not num_seats:
        messagebox.showinfo("Error", "Please provide your name and the number of seats.")
        return

    try:
        cursor.execute("SELECT id FROM movies WHERE title = %s", (title,))
        movie_id = cursor.fetchone()[0]

        cursor.execute("INSERT INTO bookings (movie_id, user_name, booking_date, num_seats) VALUES (%s, %s, CURDATE(), %s)", (movie_id, user_name, num_seats))
        conn.commit()

        messagebox.showinfo("Booking Confirmation", f"Booking for '{title}' by {user_name} at {showtime} with {num_seats} seats has been confirmed.")
    
        name_entry.delete(0, tk.END)
        seats_entry.delete(0, tk.END)
    except mysql.connector.Error as e:
        conn.rollback()
        messagebox.showerror("Database Error", f"Error booking movie: {e}")

# Create a MySQL connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="programmer@20",
    database="movie_dir"
)

cursor = conn.cursor()

# Create the main GUI window
root = tk.Tk()
root.title("Movie Booking System")

# Fetch available movies from the database
cursor.execute("SELECT title FROM movies")
movie_records = cursor.fetchall()
movies = ["Select a Movie"] + [record[0] for record in movie_records]

# Sample showtimes for the selected movie
showtimes = ["-",
    "PVR-2023-11-10 14:30:00",
    "PVR-2023-11-10 17:00:00",
    "PVR-2023-11-10 20:00:00",
    "INOX-2023-11-10 13:30:00",
    "INOX-2023-11-10 15:30:00",
    "INOX-2023-11-10 19:00:00"
    "Cinepolis-2023-11-10 10:00:00",
    "Cinepolis-2023-11-10 15:00:00",
    "Cinepolis-2023-11-10 18:30:00",
]

# Create and configure labels, entry fields, and buttons
movie_label = tk.Label(root, text="Select a Movie:")
showtime_label = tk.Label(root, text="Select Showtime & Theater:")
name_label = tk.Label(root, text="Your Name:")
seats_label = tk.Label(root, text="Number of Seats:")

movie_var = tk.StringVar(value="Select a Movie")
showtime_var = tk.StringVar(value=showtimes[0])  # Initialize with the first showtime
name_entry = tk.Entry(root)
seats_entry = tk.Entry(root)

movie_dropdown = tk.OptionMenu(root, movie_var, *movies)
showtime_dropdown = tk.OptionMenu(root, showtime_var, *showtimes)

book_button = tk.Button(root, text="Book Movie", command=book_movie)

# Arrange the widgets in the window using the grid layout
movie_label.grid(row=0, column=0)
showtime_label.grid(row=1, column=0)
name_label.grid(row=2, column=0)
seats_label.grid(row=3, column=0)

movie_dropdown.grid(row=0, column=1)
showtime_dropdown.grid(row=1, column=1)
name_entry.grid(row=2, column=1)
seats_entry.grid(row=3, column=1)

book_button.grid(row=4, column=0, columnspan=2)

# Start the GUI main loop
root.mainloop()