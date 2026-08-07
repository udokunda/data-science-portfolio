-- ===========================================================
-- Project: Student Database SQL Assignment
-- Author : Shellton Maleka
-- Database: MySQL
-- Description:
-- This project demonstrates fundamental SQL concepts including:
-- - Creating tables
-- - Inserting data
-- - Filtering records
-- - Pattern matching
-- - Aggregate functions
-- - GROUP BY
-- - Date functions
-- ===========================================================
CREATE DATABASE SQL_assignment02;
USE SQL_assignment02;


-- ===========================================================
-- QUESTION 1
-- Display the current date and time
-- ===========================================================

SELECT NOW() AS CurrentDateTime;


-- ===========================================================
-- QUESTION 2
-- Create the Student table
-- ===========================================================

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    LastName VARCHAR(50),
    FirstName VARCHAR(50),
    Fees DECIMAL(10,2),
    Gender VARCHAR(10),
    Course VARCHAR(50),
    DateOfBirth DATE,
    NSFASPayment DECIMAL(10,2)
);


-- ===========================================================
-- QUESTION 3
-- Insert 15 student records
-- ===========================================================

INSERT INTO Student
(StudentID, LastName, FirstName, Fees, Gender, Course, DateOfBirth, NSFASPayment)
VALUES
(1001, 'Mudau', 'Rendani', 45000.00, 'Male', 'Information Technology', '2003-05-12', 18000.00),
(1002, 'Netshifhethe', 'Lufuno', 52000.00, 'Female', 'Accounting', '2004-08-21', 22000.00),
(1003, 'Mulaudzi', 'Takalani', 61000.00, 'Male', 'Engineering', '2002-11-03', 25000.00),
(1004, 'Baloyi', 'Nkateko', 38000.00, 'Male', 'Business Management', '2005-02-18', 16000.00),
(1005, 'Hlungwani', 'Tsakani', 56000.00, 'Female', 'Information Technology', '2004-07-27', 21000.00),
(1006, 'Mavundla', 'Mbhazima', 47000.00, 'Male', 'Education', '2003-09-14', 19500.00),
(1007, 'Mashigo', 'Katlego', 34000.00, 'Male', 'Marketing', '2006-01-30', 15000.00),
(1008, 'Mokgadi', 'Ntswaki', 62500.00, 'Female', 'Engineering', '2002-06-11', 24000.00),
(1009, 'Mahlangu', 'Thabo', 42000.00, 'Male', 'Accounting', '2005-10-05', 17500.00),
(1010, 'Mbatha', 'Babalwa', 55000.00, 'Female', 'Human Resources', '2004-03-22', 23000.00),
(1011, 'Mgangatho', 'Luyanda', 36000.00, 'Male', 'Education', '2006-05-16', 15500.00),
(1012, 'Ndzuzo', 'Asanda', 64000.00, 'Female', 'Information Technology', '2002-12-09', 24500.00),
(1013, 'Dlamini', 'Sibusiso', 50000.00, 'Male', 'Business Management', '2003-04-25', 200.00),
(1014, 'Khumalo', 'Ayanda', 59000.00, 'Female', 'Marketing', '2005-08-13', 22500.00),
(1015, 'Mthembu', 'Sfiso', 43000.00, 'Male', 'Accounting', '2004-11-19', 17000.00);


-- ===========================================================
-- Verify that all records were inserted
-- ===========================================================

SELECT * FROM Student;


-- ===========================================================
-- QUESTION 4
-- Display students whose Fees are between R40 000 and R60 000
-- ===========================================================

SELECT *
FROM Student
WHERE Fees BETWEEN 40000 AND 60000;


-- ===========================================================
-- QUESTION 5
-- Display StudentID, FirstName, LastName and NSFASPayment
-- where NSFASPayment is between R18 000 and R22 000
-- ===========================================================

SELECT StudentID, FirstName, LastName, NSFASPayment
FROM Student
WHERE NSFASPayment BETWEEN 18000 AND 22000;


-- ===========================================================
-- QUESTION 6
-- Display all female students enrolled in
-- Information Technology
-- ===========================================================

SELECT *
FROM Student
WHERE Gender = 'Female'
AND Course = 'Information Technology';


-- ===========================================================
-- QUESTION 7
-- Display students studying Accounting or Engineering
-- ===========================================================

SELECT *
FROM Student
WHERE Course IN ('Accounting', 'Engineering');


-- ===========================================================
-- QUESTION 8
-- Display students whose LastName starts with M
-- ===========================================================

SELECT *
FROM Student
WHERE LastName LIKE 'M%';


-- ===========================================================
-- QUESTION 9
-- Display students whose FirstName ends with 'a'
-- ===========================================================

SELECT *
FROM Student
WHERE FirstName LIKE '%a';


-- ===========================================================
-- QUESTION 10
-- Display FirstName, LastName and DateOfBirth
-- of students born in 2005
-- ===========================================================

SELECT FirstName, LastName, DateOfBirth
FROM Student
WHERE YEAR(DateOfBirth) = 2005;


-- ===========================================================
-- QUESTION 11
-- Calculate the total Fees payable by all students
-- ===========================================================

SELECT SUM(Fees) AS TotalFees
FROM Student;


-- ===========================================================
-- QUESTION 12
-- Calculate the total NSFAS payment
-- ===========================================================

SELECT SUM(NSFASPayment) AS TotalNSFASPayment
FROM Student;


-- ===========================================================
-- QUESTION 13
-- Display each course and the number of students enrolled
-- ===========================================================

SELECT Course,
       COUNT(*) AS NumberOfStudents
FROM Student
GROUP BY Course;


-- ===========================================================
-- QUESTION 14
-- Determine the number of female students
-- ===========================================================

SELECT COUNT(*) AS FemaleStudents
FROM Student
WHERE Gender = 'Female';


-- ===========================================================
-- QUESTION 15
-- Display students who are NOT enrolled in
-- Accounting and Engineering
-- ===========================================================

SELECT *
FROM Student
WHERE Course NOT IN ('Accounting', 'Engineering');


-- ===========================================================
-- END OF PROJECT
-- ===========================================================