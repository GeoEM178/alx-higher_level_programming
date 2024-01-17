-- create database and table with name and id
-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- ussing the database
USE hbtn_0d_usa;
-- creating the table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
