-- Create the 'movie_dir' database
CREATE DATABASE movie_dir;

-- Use the 'movie_dir' database
USE movie_dir;

-- Create the 'movies' table to store movie information
CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    director VARCHAR(255) NOT NULL,
    year INT NOT NULL
);

-- Create the 'bookings' table to store booking information
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    booking_date DATE NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);

-- Insert real movie data into the 'movies' table
INSERT INTO movies (title, director, year) VALUES
    ('The Shawshank Redemption', 'Frank Darabont', 1994),
    ('The Godfather', 'Francis Ford Coppola', 1972),
    ('Pulp Fiction', 'Quentin Tarantino', 1994),
    ('The Dark Knight', 'Christopher Nolan', 2008),
    ('Forrest Gump', 'Robert Zemeckis', 1994);

-- Insert sample bookings into the 'bookings' table
-- Replace 'movie_id' with the appropriate 'id' of the movie you want to book
INSERT INTO bookings (movie_id, user_name, booking_date) VALUES
    (1, 'Andy Dufresne', CURDATE()),
    (2, 'Michael Corleone', CURDATE()),
    (1, 'Ellis Boyd Redding', CURDATE()),
    (3, 'Jules Winnfield', CURDATE()),
    (4, 'Bruce Wayne', CURDATE());

