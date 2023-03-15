-- A script that creates a table called second_table and insers records in the current database in your MySQL server.
-- Creates a table called first_table in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
INSERT INTO second_table value('1', 'John', '10');
INSERT INTO second_table value('2', 'Alex', '3');
INSERT INTO second_table value('3', 'Bob', '14');
INSERT INTO second_table value('4', 'George', '8');
