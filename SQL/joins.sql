SHOW DATABASES;
-- CREATE DATABASE db_name;
-- use db_name;

use ch3;

--first table
CREATE TABLE Student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    s_name VARCHAR(20) NOT NULL
);

drop table Teacher;

INSERT INTO Student (s_name)
VALUES ('Ram Joshi'), ('Rahul Bhattarai'), ('Roma Pandey'), ('Roshani Paudel');

SELECT * FROM Student;
drop TABLE Student;

--Second Table
CREATE TABLE Teacher (
    id INT AUTO_INCREMENT PRIMARY KEY,
    T_name VARCHAR(20) NOT NULL
);

INSERT INTO Teacher (T_name)
VALUES ('Ram Joshi'), ('Raman Bhattarai'), ('Rohit Pandey'), ('Maya Paudel');

select * from Teacher;
DROP table Teacher;

--Union operation--
select * from Student Union Select * from Teacher; --However, it will eliminate duplicate rows from its result set. 
select * from Student Union All Select * from Teacher;   --it also shows the duplicate rows.



--Intersect operation--
select * from Student Intersect Select * from Teacher;


--Minus Operation--
select * from Student Minus Select * from Teacher; --maynot work
select * from Student Except Select * from Teacher; 


--inner join
SELECT *
FROM Student
INNER JOIN Teacher ON Student.s_name = Teacher.T_name;

--left join
SELECT *
FROM Student LEFT JOIN Teacher ON Student.s_name = Teacher.T_name;


--right join
SELECT Student.s_name,Teacher.T_name
FROM Student
RIGHT JOIN Teacher ON Student.s_name = Teacher.T_name;

SELECT * FROM Teacher;


