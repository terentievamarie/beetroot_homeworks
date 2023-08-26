CREATE TABLE puples(
	id INT AUTO_INCREMENT PRIMARY KEY ,
	name VARCHAR(255),
	age INT,
	grade INT
);
ALTER TABLE puples RENAME TO students;

ALTER TABLE students ADD COLUMN faculty VARCHAR(255);

INSERT INTO students (id,name, age, grade, faculty)
VALUES (1, "ALice", 19, 2, "English"), (2, "John", 20, 3, "Polish"), (3, "Mary", 22, 5, "Ukrainian");

UPDATE students
SET age = 23
WHERE name = "Alice";

DELETE FROM students
WHERE age = 22;

