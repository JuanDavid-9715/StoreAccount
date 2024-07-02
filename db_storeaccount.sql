CREATE DATABASE IF NOT EXISTS storeaccount;
USE storeaccount;

-- DROP TABLE yearly;
-- DROP TABLE monthly;
-- DROP TABLE diary;

CREATE TABLE yearly(
	id INT AUTO_INCREMENT PRIMARY KEY,
    sales DOUBLE,
    supplierExpenses DOUBLE,
	overheads DOUBLE,
    total DOUBLE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE monthly(
	id INT AUTO_INCREMENT PRIMARY KEY,
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
    sales DOUBLE,
    supplierExpenses DOUBLE,
	overheads DOUBLE,
    total DOUBLE,
    creationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updateDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    monthlyID INT,
    FOREIGN KEY (monthlyID) REFERENCES monthly(id)
);


INSERT INTO yearly(sales, supplierExpenses, overheads, total) VALUES(1000000.0, 1000000.0, 1000000.0, 1000000.0);
INSERT INTO yearly(sales, supplierExpenses, overheads, total) VALUES(2000000.0, 2000000.0, 2000000.0, 2000000.0);
INSERT INTO yearly() VALUES();

INSERT INTO monthly(sales, supplierExpenses, overheads, total, yearlyID) VALUES(1000000.0, 1000000.0, 1000000.0, 1000000.0, 1);
INSERT INTO monthly(sales, supplierExpenses, overheads, total, yearlyID) VALUES(2000000.0, 2000000.0, 2000000.0, 2000000.0, 1);
INSERT INTO monthly(sales, supplierExpenses, overheads, total, yearlyID) VALUES(2000000.0, 2000000.0, 2000000.0, 2000000.0, 2);
INSERT INTO monthly(yearlyID) VALUES(2);

INSERT INTO diary(sales, supplierExpenses, overheads, total, monthlyID) VALUES(1000000.0, 1000000.0, 1000000.0, 1000000.0, 1);
INSERT INTO diary(sales, supplierExpenses, overheads, total, monthlyID) VALUES(2000000.0, 2000000.0, 2000000.0, 2000000.0, 1);
INSERT INTO diary(sales, supplierExpenses, overheads, total, monthlyID) VALUES(1000000.0, 1000000.0, 1000000.0, 1000000.0, 2);
INSERT INTO diary(sales, supplierExpenses, overheads, total, monthlyID) VALUES(2000000.0, 2000000.0, 2000000.0, 2000000.0, 2);
INSERT INTO diary(sales, supplierExpenses, overheads, total, monthlyID) VALUES(1000000.0, 1000000.0, 1000000.0, 1000000.0, 3);
INSERT INTO diary(sales, supplierExpenses, overheads, total, monthlyID) VALUES(2000000.0, 2000000.0, 2000000.0, 2000000.0, 3);
INSERT INTO diary(sales, supplierExpenses, overheads, total, monthlyID) VALUES(2000000.0, 2000000.0, 2000000.0, 2000000.0, 4);
INSERT INTO diary(monthlyID) VALUES(4);

SELECT * FROM diary;
SELECT * FROM monthly;
SELECT * FROM yearly;
