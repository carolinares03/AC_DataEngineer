-- Crear base de datos y seleccionarla
CREATE DATABASE IF NOT EXISTS SalesDB;
USE SalesDB;

-- Eliminar tablas si existen (ordenando por dependencias para evitar errores en fk)
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

-- Tabla: countries
CREATE TABLE countries (
    CountryID INT PRIMARY KEY,
    CountryName VARCHAR(45),
    CountryCode VARCHAR(2)
);

-- Tabla: cities
CREATE TABLE cities (
    CityID INT PRIMARY KEY,
    CityName VARCHAR(45),
    zipcode VARCHAR(10),
    countries_CountryID INT,
    FOREIGN KEY (countries_CountryID) REFERENCES countries(CountryID)
);

-- Tabla: categories
CREATE TABLE categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(45)
);

-- Tabla: products
CREATE TABLE products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10,4),
    CategoryID INT,
    Class VARCHAR(45),
    ModifyDate VARCHAR(20), -- formato "hh:mm.ss"
    Resistant VARCHAR(45),
    IsAllergic VARCHAR(10),
    VitalityDays INT,
    FOREIGN KEY (CategoryID) REFERENCES categories(CategoryID)
);

-- Tabla: customers
CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(45),
    MiddleInitial VARCHAR(1),
    LastName VARCHAR(45),
    CityID INT,
    Address VARCHAR(90),
    FOREIGN KEY (CityID) REFERENCES cities(CityID)
);

-- Tabla: employees
CREATE TABLE employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(45),
    MiddleInitial VARCHAR(1),
    LastName VARCHAR(45),
    BirthDate DATETIME,
    Gender VARCHAR(1),
    CityID INT,
    HireDate DATETIME,
    FOREIGN KEY (CityID) REFERENCES cities(CityID)
);

-- Tabla: sales
CREATE TABLE sales (
    SalesID INT PRIMARY KEY,
    SalesPersonID INT,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    Discount DECIMAL(10,2),
    TotalPrice DECIMAL(10,2),
    SalesDate VARCHAR(20), -- formato "mm:ss.ms"
    TransactionNumber VARCHAR(255),
    FOREIGN KEY (SalesPersonID) REFERENCES employees(EmployeeID),
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES products(ProductID)
);
