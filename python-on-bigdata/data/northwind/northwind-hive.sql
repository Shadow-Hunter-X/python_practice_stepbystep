CREATE database if not exists northwind;

CREATE TABLE  Categories(
	   CategoryID    string,
	   CategoryName  string,
	   Description   string,
	   Picture       string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
	
LOAD DATA INPATH '/northwind/Categories.csv' OVERWRITE INTO TABLE Categories ;		
	
--------------------------------------------------------------

CREATE TABLE  CustomerCustomerDemo(
	   CustomerID   string,
	   CustomerTypeID  string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
		  
--------------------------------------------------------------

CREATE TABLE CustomerDemographics   (
	   CustomerTypeID   string,
	   CustomerDesc     string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
	
--------------------------------------------------------------

CREATE TABLE    Customers(
	   CustomerID   string,
	   CompanyName  string,
	   ContactName  string,
	   ContactTitle string,
	   Address      string,
	   City       string,
	   Region     string,
	   PostalCode  string,
	   Country     string,
	   Phone       string,
	   Fax         string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
	
LOAD DATA INPATH '/northwind/Customers.csv' OVERWRITE INTO TABLE Customers ;	
		
--------------------------------------------------------------

CREATE TABLE Employees   (
	   EmployeeID   string,
	   LastName     string,
	   FirstName    string,
	   Title        string,
	   TitleOfCourtesy   string,
	   BirthDate      string,
	   HireDate       string,
	   Address       string,
	   City       string,
	   Region       string,
	   PostalCode     string,
	   Country       string,
	   HomePhone       string,
	   Extension       string,
	   Photo      string,
	   Notes      string,
	   ReportsTo     string,
	   PhotoPath     string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
	
LOAD DATA INPATH '/northwind/Employees.csv' OVERWRITE INTO TABLE Employees ;		

--------------------------------------------------------------

CREATE TABLE  EmployeeTerritories   (
	   EmployeeID   string,
	   TerritoryID  string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
	
LOAD DATA INPATH '/northwind/EmployeeTerritories.csv' OVERWRITE INTO TABLE EmployeeTerritories ;		
	
--------------------------------------------------------------

CREATE TABLE    OrderDetails   (
	   OrderID     string,
	   ProductID   string,
	   UnitPrice   string,
	   Quantity    string,
	   Discount    string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
	
LOAD DATA INPATH '/northwind/OrderDetails.csv' OVERWRITE INTO TABLE OrderDetails ;		

--------------------------------------------------------------

CREATE TABLE    Orders   (
	   OrderID    string,
	   CustomerID  string,
	   EmployeeID  string,
	   OrderDate   string,
	   RequiredDate  string,
	   ShippedDate    string,
	   ShipVia    string,
	   Freight    string,
	   ShipName   string,
	   ShipAddress   string,
	   ShipCity     string,
	   ShipRegion    string,
	   ShipPostalCode    string,
	   ShipCountry    string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;

LOAD DATA INPATH '/northwind/Orders.csv' OVERWRITE INTO TABLE Orders ;	
		  
--------------------------------------------------------------

CREATE TABLE    Products(
	   ProductID   string,
	   ProductName     string,
	   SupplierID     string,
	   CategoryID       string,
	   QuantityPerUnit   string,
	   UnitPrice      string,
	   UnitsInStock    string,
	   UnitsOnOrder     string,
	   ReorderLevel     string,
	   Discontinued     string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
		  
LOAD DATA INPATH '/northwind/Products.csv' OVERWRITE INTO TABLE Products ;	

--------------------------------------------------------------

CREATE TABLE    Region(
	   RegionID    string,
	   RegionDescription   string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
		  
		  
LOAD DATA INPATH '/northwind/Region.csv' OVERWRITE INTO TABLE Region ;	

--------------------------------------------------------------

CREATE TABLE    Shippers   (
	   ShipperID  string,
	   CompanyName  string,
	   Phone   string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
	
LOAD DATA INPATH '/northwind/Shippers.csv' OVERWRITE INTO TABLE Shippers ;	
	
--------------------------------------------------------------

CREATE TABLE  Suppliers   (
	   SupplierID   string,
	   CompanyName  string,
	   ContactName  string,
	   ContactTitle  string,
	   Address     string,
	   City      string,
	   Region    string,
	   PostalCode   string,
	   Country     string,
	   Phone      string,
	   Fax       string,
	   HomePage    string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;
	

LOAD DATA INPATH '/northwind/Suppliers.csv' OVERWRITE INTO TABLE Suppliers ;	

--------------------------------------------------------------

CREATE TABLE  Territories(
	   TerritoryID      string,
	   TerritoryDescription   string,
	   RegionID   string
)ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  LINES TERMINATED BY '\n'
		  STORED AS TEXTFILE;

LOAD DATA INPATH '/northwind/Territories.csv' OVERWRITE INTO TABLE Territories ;
--------------------------------------------------------------