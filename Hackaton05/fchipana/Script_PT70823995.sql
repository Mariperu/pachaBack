CREATE DATABASE PT70823995;

CREATE TABLE IF NOT EXISTS Region (
  id_Region numeric PRIMARY KEY,
  Region char(100)
);

CREATE TABLE IF NOT EXISTS Country (
  id_Country numeric PRIMARY KEY,
  CountryName char(100),
  id_Region numeric,
  FOREIGN KEY (id_Region) REFERENCES Region (id_Region)
);

CREATE TABLE IF NOT EXISTS State (
  id_State numeric PRIMARY KEY,
  State char(100),
  id_Region numeric,
  FOREIGN KEY (id_Region) REFERENCES Region (id_Region)
);

CREATE TABLE IF NOT EXISTS "PostalCode-City" (
  PostalCode numeric PRIMARY KEY,
  City char(100),
  id_State numeric,
  FOREIGN KEY (id_State) REFERENCES State (id_State)
);

CREATE TABLE IF NOT EXISTS Category (
  id_Category numeric PRIMARY KEY,
  Category char(100)
);

CREATE TABLE IF NOT EXISTS "Sub-Category" (
  id_Sub_Category numeric PRIMARY KEY,
  "Sub-Category" char(100),
  id_Category numeric,
  FOREIGN KEY (id_Category) REFERENCES Category (id_Category)
);

CREATE TABLE IF NOT EXISTS "Product ID-Product Name" (
  "Product ID" char(100) PRIMARY KEY,
  "Product Name" char(300),
  id_Sub_Category numeric,
  FOREIGN KEY (id_Sub_Category) REFERENCES "Sub-Category" (id_Sub_Category)
);

CREATE TABLE IF NOT EXISTS Segment (
  id_Segment numeric PRIMARY KEY,
  Segment char(300)
);

CREATE TABLE IF NOT EXISTS "Customer ID-Customer Name" (
  "Customer ID" char(100) PRIMARY KEY,
  "Customer Name" char(300),
  id_Segment numeric,
  FOREIGN KEY (id_Segment) REFERENCES Segment (id_Segment)
);

CREATE TABLE IF NOT EXISTS ShipMode (
  id_ShipMode numeric PRIMARY KEY,
  ShipMode char(300)
);

CREATE TABLE IF NOT EXISTS Orders_Tercera_Forma (
  "Row ID" serial PRIMARY KEY,
  "Order ID" char(100),
  "Order Date" date,
  "Ship Date" date,
  id_ShipMode numeric,
  "Customer ID" char(100),
  "Postal Code" numeric,
  "Product ID" char(100),
  Sales double precision,
  Quantity numeric,
  Discount double precision,
  Profit double precision,
  FOREIGN KEY (id_ShipMode) REFERENCES ShipMode (id_ShipMode),
  FOREIGN KEY ("Customer ID") REFERENCES "Customer ID-Customer Name" ("Customer ID"),
  FOREIGN KEY ("Postal Code") REFERENCES "PostalCode-City" (PostalCode),
  FOREIGN KEY ("Product ID") REFERENCES "Product ID-Product Name" ("Product ID")
);