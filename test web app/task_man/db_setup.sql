CREATE DATABASE `task_man` CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'task_user'@'localhost' IDENTIFIED BY '1';
GRANT ALL PRIVILEGES ON *.* TO 'task_user'@'localhost';