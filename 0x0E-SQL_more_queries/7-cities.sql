-- A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF EXISTS hbtn_0d_usa;
USE hbtn_Od_usa;
CREATE TABLE IF EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VACHAR(256) NOT NULL
	);
