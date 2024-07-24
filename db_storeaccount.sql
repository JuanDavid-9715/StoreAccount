CREATE DATABASE IF NOT EXISTS storeaccount;
USE storeaccount;

-- DROP TABLE diary;
-- DROP TABLE monthly;
-- DROP TABLE yearly;

CREATE TABLE yearly(
	id INT AUTO_INCREMENT PRIMARY KEY,
    year varchar(5),
    sales DOUBLE,
    supplierExpenses DOUBLE,
	overheads DOUBLE,
    total DOUBLE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE monthly(
	id INT AUTO_INCREMENT PRIMARY KEY,
    month varchar(5),
    sales DOUBLE,
    supplierExpenses DOUBLE,
	overheads DOUBLE,
    total DOUBLE,
    creationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updateDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    yearlyID INT,
    FOREIGN KEY (yearlyID) REFERENCES yearly(id)
);

CREATE TABLE diary(
	id INT AUTO_INCREMENT PRIMARY KEY,
    day varchar(5),
    sales DOUBLE,
    supplierExpenses DOUBLE,
	overheads DOUBLE,
    total DOUBLE,
    creationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updateDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    monthlyID INT,
    FOREIGN KEY (monthlyID) REFERENCES monthly(id)
);


INSERT INTO yearly(year, sales, supplierExpenses, overheads, total) VALUES(2024, 1000000.0, 1000000.0, 1000000.0, 1000000.0);
INSERT INTO yearly(year, sales, supplierExpenses, overheads, total) VALUES(2023, 2000000.0, 2000000.0, 2000000.0, 2000000.0);
INSERT INTO yearly(year, sales, supplierExpenses, overheads, total) VALUES(2022, 3000000.0, 3000000.0, 3000000.0, 3000000.0);
INSERT INTO yearly(year, sales, supplierExpenses, overheads, total) VALUES(2021, 4000000.0, 4000000.0, 4000000.0, 4000000.0);
INSERT INTO yearly(year) VALUES(2020);

INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(1, 1000000.0, 1000000.0, 1000000.0, 1000000.0, 1);
INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(2, 2000000.0, 2000000.0, 2000000.0, 2000000.0, 1);
INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(3, 3000000.0, 3000000.0, 3000000.0, 3000000.0, 1);
INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(4, 4000000.0, 4000000.0, 4000000.0, 4000000.0, 1);
INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(5, 5000000.0, 5000000.0, 5000000.0, 5000000.0, 1);
INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(6, 6000000.0, 6000000.0, 6000000.0, 6000000.0, 1);
INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(7, 7000000.0, 7000000.0, 7000000.0, 7000000.0, 1);
INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(1, 1000000.0, 1000000.0, 1000000.0, 1000000.0, 2);
INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(2, 2000000.0, 2000000.0, 2000000.0, 2000000.0, 2);
INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(3, 3000000.0, 3000000.0, 3000000.0, 3000000.0, 2);
INSERT INTO monthly(month, sales, supplierExpenses, overheads, total, yearlyID) VALUES(4, 4000000.0, 4000000.0, 4000000.0, 4000000.0, 2);
INSERT INTO monthly(month, yearlyID) VALUES(5, 2);
INSERT INTO monthly(month, yearlyID) VALUES(1, 3);
INSERT INTO monthly(month, yearlyID) VALUES(2, 3);
INSERT INTO monthly(month, yearlyID) VALUES(3, 3);

INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(1, 1000000.0, 1000000.0, 1000000.0, 1000000.0, 1);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(2, 2000000.0, 2000000.0, 2000000.0, 2000000.0, 1);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(3, 1000000.0, 1000000.0, 1000000.0, 1000000.0, 1);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(4, 2000000.0, 2000000.0, 2000000.0, 2000000.0, 1);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(5, 1000000.0, 1000000.0, 1000000.0, 1000000.0, 2);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(6, 2000000.0, 2000000.0, 2000000.0, 2000000.0, 2);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(7, 2000000.0, 2000000.0, 2000000.0, 2000000.0, 2);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(8, 1000000.0, 1000000.0, 1000000.0, 1000000.0, 2);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(9, 2000000.0, 2000000.0, 2000000.0, 2000000.0, 3);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(10, 1000000.0, 1000000.0, 1000000.0, 1000000.0, 3);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(11, 2000000.0, 2000000.0, 2000000.0, 2000000.0, 3);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(12, 1000000.0, 1000000.0, 1000000.0, 1000000.0, 4);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(13, 2000000.0, 2000000.0, 2000000.0, 2000000.0, 4);
INSERT INTO diary(day, sales, supplierExpenses, overheads, total, monthlyID) VALUES(14, 2000000.0, 2000000.0, 2000000.0, 2000000.0, 5);
INSERT INTO diary(day, monthlyID) VALUES(15, 6);

USE storeaccount;

SELECT * FROM diary;
SELECT * FROM monthly;
SELECT * FROM yearly;

SELECT id, year FROM yearly ORDER BY year DESC;
SELECT * FROM monthly WHERE yearlyID='2' ORDER BY month ASC;

-- SELECT * FROM diary WHERE id='33';
-- DELETE FROM diary WHERE id='33';
