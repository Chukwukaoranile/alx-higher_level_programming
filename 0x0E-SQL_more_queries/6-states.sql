-- A script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- creates the database hbtn_0d_usa.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selecting the database
USE hbtn_0d_usa;
-- Create table with name state.
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
