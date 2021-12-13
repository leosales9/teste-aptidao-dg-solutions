CREATE TABLE IF NOT EXISTS people (
    person_id SERIAL,
    person_name VARCHAR(64) NOT NULL,
    person_birthdate DATE NOT NULL
);