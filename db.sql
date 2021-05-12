CREATE TABLE studens(id Serial, name text, adress text, age int);

INSERT INTO studens(name, adress, age) VALUES ('Ryan', 'San Francisco', 25);
INSERT INTO studens(name, adress, age) VALUES ('Jhon', 'New York', 18);

SELECT * FROM studens