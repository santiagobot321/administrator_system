CREATE DATABASE proyectoIntegrador;
USE proyectoIntegrador;


CREATE TABLE equipos (
	id INT PRIMARY KEY AUTO_INCREMENT, 
	hostname VARCHAR(150), 
	MAC VARCHAR(200), 
	IP VARCHAR(250), 
	estado VARCHAR(100)
);

INSERT INTO equipos (id, hostname, MAC, IP, estado) VALUES (1, "localhost", "B2:5D:E9:1E:AE:15", "166.23.190.148", "Buenas condiciones");

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
