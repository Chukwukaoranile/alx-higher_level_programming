-- A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF EXISTS hbtn_0d_usa;
USE hbtn_Od_usa;
CREATE TABLE IF NOT EXISTS states (
  id INT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS cities (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY (state_id) REFERENCES states(id)
);
