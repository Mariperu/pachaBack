CREATE DATABASE PT70823995;

CREATE TABLE IF NOT EXISTS Salon (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    año_escolar VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Alumnos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    identificador VARCHAR(10),
    edad INTEGER,
    correo VARCHAR(100)
    salon_id INTEGER REFERENCES Salon(id)
);

CREATE TABLE IF NOT EXISTS Cursos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    profesor VARCHAR(100),
    salon_id INTEGER REFERENCES Salon(id)
);

CREATE TABLE IF NOT EXISTS Profesores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    identificador VARCHAR(10),
    edad INTEGER,
    correo VARCHAR(100),
    salon_id INTEGER REFERENCES Salon(id)
);