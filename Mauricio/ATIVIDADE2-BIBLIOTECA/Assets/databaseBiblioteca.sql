CREATE DATABASE Biblioteca;

use Biblioteca;


CREATE TABLE Authors (
 AuthorID INT PRIMARY KEY,
 Name VARCHAR(100),
 BirthYear INT
);
CREATE TABLE Books (
 BookID INT PRIMARY KEY,
 Title VARCHAR(200),
 AuthorID INT,
 FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);
CREATE TABLE Loans (
 LoanID INT PRIMARY KEY,
 BookID INT,
 MemberID INT,
 LoanDate DATE,
 ReturnDate DATE,
 FOREIGN KEY (BookID) REFERENCES Books(BookID)
);

INSERT INTO Authors (AuthorID, Name, BirthYear) VALUES
(1, 'Gabriel Garcia Marquez', 1927),
(2, 'J.K. Rowling', 1965),
(3, 'George Orwell', 1903),
(4, 'Jane Austen', 1775),
(5, 'Fyodor Dostoevsky', 1821),
(6, 'Agatha Christie', 1890),
(7, 'Haruki Murakami', 1949),
(8, 'Leo Tolstoy', 1828),
(9, 'Mark Twain', 1835),
(10, 'Ernest Hemingway', 1899),
(11, 'Virginia Woolf', 1882),
(12, 'Isabel Allende', 1942),
(13, 'Franz Kafka', 1883),
(14, 'Charles Dickens', 1812),
(15, 'J.R.R. Tolkien', 1892),
(16, 'Stephen King', 1947),
(17, 'Oscar Wilde', 1854),
(18, 'Edgar Allan Poe', 1809),
(19, 'Herman Melville', 1819),
(20, 'Emily Bronte', 1818),
(21, 'James Joyce', 1882),
(22, 'Victor Hugo', 1802),
(23, 'H.G. Wells', 1866),
(24, 'Ray Bradbury', 1920),
(25, 'Isaac Asimov', 1920),
(26, 'George R.R. Martin', 1948),
(27, 'Arthur Conan Doyle', 1859),
(28, 'Margaret Atwood', 1939),
(29, 'Toni Morrison', 1931),
(30, 'Neil Gaiman', 1960);


-- Inserts para a tabela Books
INSERT INTO Books (BookID, Title, AuthorID) VALUES
(1, 'One Hundred Years of Solitude', 1),
(2, 'Harry Potter and the Philosopher''s Stone', 2),
(3, '1984', 3),
(4, 'Pride and Prejudice', 4),
(5, 'Crime and Punishment', 5),
(6, 'Murder on the Orient Express', 6),
(7, 'Norwegian Wood', 7),
(8, 'War and Peace', 8),
(9, 'Adventures of Huckleberry Finn', 9),
(10, 'The Old Man and the Sea', 10),
(11, 'To the Lighthouse', 11),
(12, 'The House of the Spirits', 12),
(13, 'The Metamorphosis', 13),
(14, 'A Tale of Two Cities', 14),
(15, 'The Hobbit', 15),
(16, 'The Shining', 16),
(17, 'The Picture of Dorian Gray', 17),
(18, 'The Raven', 18),
(19, 'Moby-Dick', 19),
(20, 'Wuthering Heights', 20),
(21, 'Ulysses', 21),
(22, 'Les Misérables', 22),
(23, 'The War of the Worlds', 23),
(24, 'Fahrenheit 451', 24),
(25, 'Foundation', 25),
(26, 'A Game of Thrones', 26),
(27, 'Sherlock Holmes', 27),
(28, 'The Handmaid''s Tale', 28),
(29, 'Beloved', 29),
(30, 'American Gods', 30);


-- Inserts para a tabela Loans
INSERT INTO Loans (LoanID, BookID, MemberID, LoanDate, ReturnDate) VALUES
(1, 1, 101, '2024-01-05', '2024-01-19'),
(2, 2, 102, '2024-02-01', '2024-02-15'),
(3, 3, 103, '2024-03-01', '2024-03-15'),
(4, 4, 104, '2024-04-10', '2024-04-24'),
(5, 5, 105, '2024-05-05', '2024-05-19'),
(6, 6, 106, '2024-06-12', '2024-06-26'),
(7, 7, 107, '2024-07-14', '2024-07-28'),
(8, 8, 108, '2024-08-10', '2024-08-24'),
(9, 9, 109, '2024-09-05', '2024-09-19'),
(10, 10, 110, '2024-10-02', '2024-10-16'),
(11, 11, 111, '2024-11-10', '2024-11-24'),
(12, 12, 112, '2024-12-05', '2024-12-19'),
(13, 13, 113, '2024-01-12', '2024-01-26'),
(14, 14, 114, '2024-02-18', '2024-03-04'),
(15, 15, 115, '2024-03-15', '2024-03-29'),
(16, 16, 116, '2024-04-22', '2024-05-06'),
(17, 17, 117, '2024-05-08', '2024-05-22'),
(18, 18, 118, '2024-06-15', '2024-06-29'),
(19, 19, 119, '2024-07-20', '2024-08-03'),
(20, 20, 120, '2024-08-17', '2024-08-31'),
(21, 21, 121, '2024-09-13', '2024-09-27'),
(22, 22, 122, '2024-10-09', '2024-10-23'),
(23, 23, 123, '2024-11-14', '2024-11-28'),
(24, 24, 124, '2024-12-01', '2024-12-15'),
(25, 25, 125, '2024-01-07', '2024-01-21'),
(26, 26, 126, '2024-02-13', '2024-02-27'),
(27, 27, 127, '2024-03-09', '2024-03-23'),
(28, 28, 128, '2024-04-05', '2024-04-19'),
(29, 29, 129, '2024-05-11', '2024-05-25'),
(30, 30, 130, '2024-06-07', '2024-06-21');


SELECT Books.Title, Authors.Name
FROM Books
JOIN Authors ON Books.AuthorID = Authors.AuthorID;

SELECT Books.Title, Loans.MemberID, Loans.LoanDate, Loans.ReturnDate
FROM Loans
JOIN Books ON Loans.BookID = Books.BookID;

SELECT Authors.Name, Books.Title
FROM Authors
LEFT JOIN Books ON Authors.AuthorID = Books.AuthorID;


SELECT Books.Title, Loans.LoanDate, Loans.ReturnDate
FROM Books
LEFT JOIN Loans ON Books.BookID = Loans.BookID;

SELECT COUNT(*) AS TotalLoans
FROM Loans;

SELECT Authors.Name, COUNT(Books.BookID) AS NumberOfBooks
FROM Authors
LEFT JOIN Books ON Authors.AuthorID = Books.AuthorID
GROUP BY Authors.Name;


-- Adiciona o novo autor
INSERT INTO Authors (AuthorID, Name, BirthYear) 
VALUES (31, 'W.xavier.7', 1994);

-- Adiciona o novo livro
INSERT INTO Books (BookID, Title, AuthorID) 
VALUES (31, 'Codigo do Desenvolverdor FullStack', 31);


-- Registra o novo empréstimo
INSERT INTO Loans (LoanID, BookID, MemberID, LoanDate, ReturnDate)
VALUES (31, 31, 131, '2024-11-12', NULL);

-- Verificando pelo BookID
SELECT * FROM Books WHERE BookID = 31;

-- Verificando pelo título do livro
SELECT * FROM Books WHERE Title = 'Codigo do Desenvolverdor FullStack';




