DROP TABLE IF EXISTS Unit CASCADE;

CREATE TABLE Unit (
    id SERIAL,
    allowed bit,
    status VARCHAR(255),
    dateManufactured DATE,
    id_Machine VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS MachineType CASCADE;

CREATE TABLE MachineType (
    id SERIAL,
    typeName VARCHAR(255),
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Component CASCADE;

CREATE TABLE Component (
    id SERIAL,
    name VARCHAR NOT NULL,
    quantity INTEGER NOT NULL,
    price INTEGER NOT NULL,
    id_provider INTEGER,
    id_ComponentType INTEGER,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Tool CASCADE;

CREATE TABLE Tool (
    id SERIAL,
    name VARCHAR,
    PRIMARY KEY (id)
);

-- ---
-- Table 'ComponentType'
--
-- ---
DROP TABLE IF EXISTS ComponentType CASCADE;

CREATE TABLE ComponentType (
    id SERIAL,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

-- ---
-- Table 'Composition'
--
-- ---
DROP TABLE IF EXISTS Composition CASCADE;

CREATE TABLE Composition (
    id SERIAL,
    id_Component INTEGER,
    id_Node INTEGER,
    PRIMARY KEY (
        id_Component,
        id_Node
    )
);

-- ---
-- Table 'RequiredTools'
--
-- ---
DROP TABLE IF EXISTS RequiredTools CASCADE;

CREATE TABLE RequiredTools (
    id SERIAL,
    id_Machine VARCHAR(64),
    id_Tool INTEGER,
    PRIMARY KEY (
        id_Machine,
        id_Tool
    )
);

-- ---
-- Table 'ShopType'
--
-- ---
DROP TABLE IF EXISTS ShopType CASCADE;

CREATE TABLE ShopType (
    id SERIAL,
    type VARCHAR,
    PRIMARY KEY (id)
);

-- ---
-- Table 'Shop'
--
-- ---
DROP TABLE IF EXISTS Shop CASCADE;

CREATE TABLE Shop (
    id SERIAL,
    address VARCHAR(255),
    phone VARCHAR,
    id_ShopType INTEGER,
    PRIMARY KEY (id)
);

-- ---
-- Table 'Employee'
--
-- ---
DROP TABLE IF EXISTS Employee CASCADE;

CREATE TABLE Employee (
    id SERIAL,
    name VARCHAR,
    salary INTEGER,
    id_Shop INTEGER,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Shipment CASCADE;

CREATE TABLE Shipment (
    id SERIAL,
    price VARCHAR,
    comment VARCHAR,
    id_Customer INTEGER,
    PRIMARY KEY (id)
);


DROP TABLE IF EXISTS OrderType CASCADE;

CREATE TABLE OrderType (
    id SERIAL,
    name VARCHAR,
    PRIMARY KEY (id)
);

-- ---
-- Table 'Warranty'
--
-- ---
DROP TABLE IF EXISTS Warranty CASCADE;

CREATE TABLE Warranty (
    id SERIAL,
    expireDate DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (id)
);

-- ---
-- Table 'Customer'
--
-- ---
DROP TABLE IF EXISTS Customer CASCADE;

CREATE TABLE Customer (
    id SERIAL,
    name VARCHAR,
    phone VARCHAR,
    email VARCHAR,
    address VARCHAR,
    PRIMARY KEY (id)
);

-- ---
-- Table 'RepairAppl'
--
-- ---
DROP TABLE IF EXISTS RepairAppl CASCADE;

CREATE TABLE RepairAppl (
    id SERIAL,
    comment VARCHAR,
    date DATE,
    status VARCHAR,
    period DATE,
    id_Customer INTEGER,
    id_Machine VARCHAR(255) NOT NULL DEFAULT 'NULL',
    PRIMARY KEY (id)
);

-- ---
-- Table 'User'
--
-- ---
-- ---
-- Table 'UserRoles'
--
-- ---
DROP TABLE IF EXISTS UserRoles CASCADE;

CREATE TABLE UserRoles (
    id SERIAL,
    id_User INTEGER,
    id_Roles INTEGER,
    PRIMARY KEY (id)
);

-- ---
-- Table 'Roles'
--
-- ---
DROP TABLE IF EXISTS Roles CASCADE;

CREATE TABLE Roles (
    id SERIAL,
    name VARCHAR,
    PRIMARY KEY (id)
);

-- ---
-- Table 'Roles'
--
-- ---
DROP TABLE IF EXISTS Users CASCADE;

CREATE TABLE Users (
    id SERIAL,
    password VARCHAR,
    id_Customer INTEGER,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Orders CASCADE;

CREATE TABLE Orders (
    id SERIAL,
    date DATE,
    status VARCHAR,
    id_Employee INTEGER,
    id_Warranty INTEGER,
    id_Customer INTEGER,
    id_OrderType INTEGER,
    PRIMARY KEY (id)
);

-- ---
-- Foreign Keys
-- ---
DROP TABLE IF EXISTS Node CASCADE;

CREATE TABLE Node (
    id SERIAL,
    name VARCHAR,
    blueprint VARCHAR(1024),
    id_Machine VARCHAR(255) NOT NULL DEFAULT 'NULL',
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Machine CASCADE;

CREATE TABLE Machine (
    id VARCHAR(255) UNIQUE NOT NULL DEFAULT 'NULL',
    price INTEGER,
    blueprint VARCHAR(1024) NOT NULL DEFAULT 'NULL',
    description VARCHAR(255),
    id_MachineType INTEGER,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Provider CASCADE;
CREATE TABLE Provider(
    id SERIAL,
    name VARCHAR(255),
    address VARCHAR(255),
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS ProductType CASCADE;
CREATE TABLE ProductType(
    id SERIAL,
    name VARCHAR(255),
    id_provider INTEGER,
    PRIMARY KEY (id)
);

ALTER TABLE
    Machine
ADD
    FOREIGN KEY (id_MachineType) REFERENCES MachineType (id);

ALTER TABLE
    ProductType
ADD
    FOREIGN KEY (id_provider) REFERENCES Provider (id);

ALTER TABLE
    Component
ADD
    FOREIGN KEY (id_provider) REFERENCES Provider (id);

ALTER TABLE
    Unit
ADD
    FOREIGN KEY (id_Machine) REFERENCES Machine (id);

ALTER TABLE
    Node
ADD
    FOREIGN KEY (id_Machine) REFERENCES Machine (id);

ALTER TABLE
    Component
ADD
    FOREIGN KEY (id_ComponentType) REFERENCES ComponentType (id);

ALTER TABLE
    Composition
ADD
    FOREIGN KEY (id_Component) REFERENCES Component (id);

ALTER TABLE
    Composition
ADD
    FOREIGN KEY (id_Node) REFERENCES Node (id);

ALTER TABLE
    RequiredTools
ADD
    FOREIGN KEY (id_Machine) REFERENCES Machine (id);

ALTER TABLE
    RequiredTools
ADD
    FOREIGN KEY (id_Tool) REFERENCES Tool (id);

ALTER TABLE
    Shop
ADD
    FOREIGN KEY (id_ShopType) REFERENCES ShopType (id);

ALTER TABLE
    Employee
ADD
    FOREIGN KEY (id_Shop) REFERENCES Shop (id);

ALTER TABLE
    Orders
ADD
    FOREIGN KEY (id_Employee) REFERENCES Employee (id);

ALTER TABLE
    Orders
ADD
    FOREIGN KEY (id_Warranty) REFERENCES Warranty (id);

ALTER TABLE
    Orders
ADD
    FOREIGN KEY (id_Customer) REFERENCES Customer (id);

ALTER TABLE
    Orders
ADD
    FOREIGN KEY (id_OrderType) REFERENCES OrderType (id);

ALTER TABLE
    Shipment
ADD
    FOREIGN KEY (id_Customer) REFERENCES Customer (id);

ALTER TABLE
    RepairAppl
ADD
    FOREIGN KEY (id_Customer) REFERENCES Customer (id);

ALTER TABLE
    RepairAppl
ADD
    FOREIGN KEY (id_Machine) REFERENCES Machine (id);

ALTER TABLE
    Users
ADD
    FOREIGN KEY (id_Customer) REFERENCES Customer (id);

ALTER TABLE
    UserRoles
ADD
    FOREIGN KEY (id_User) REFERENCES Users (id);

ALTER TABLE
    UserRoles
ADD
    FOREIGN KEY (id_Roles) REFERENCES Roles (id);

-- ---
-- Table Properties
-- ---
-- ALTER TABLE Machine ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Unit ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Node ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE MachineType ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Component ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Tool ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE ComponentType ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Composition ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE RequiredTools ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE ShopType ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Shop ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Employee ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Order ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Shipment ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE OrderType ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Warranty ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Customer ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE RepairAppl ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE User ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE UserRoles ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE Roles ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ---
-- Test Data
-- ---
-- INSERT INTO Machine (model,price,blueprint,description,id_MachineType) VALUES
-- ('','','','','');
-- INSERT INTO Unit (id,allowed,status,dateManufactured,id_Machine) VALUES
-- ('','','','','');
-- INSERT INTO Node (id,name,blueprint,id_Machine) VALUES
-- ('','','','');
-- INSERT INTO MachineType (id,typeName) VALUES
-- ('','');
-- INSERT INTO Component (id,name,quantity,price,provider,id_ComponentType) VALUES
-- ('','','','','','');
-- INSERT INTO Tool (id,name) VALUES
-- ('','');
-- INSERT INTO ComponentType (id,name) VALUES
-- ('','');
-- INSERT INTO Composition (id_Component,id_Node) VALUES
-- ('','');
-- INSERT INTO RequiredTools (id_MachineType,id_Tool) VALUES
-- ('','');
-- INSERT INTO ShopType (id,type) VALUES
-- ('','');
-- INSERT INTO Shop (id,address,phone,id_ShopType) VALUES
-- ('','','','');
-- INSERT INTO Employee (id,name,salary,id_Shop) VALUES
-- ('','','','');
-- INSERT INTO Order (id,date,status,id_Employee,id_Warranty,id_Customer,id_OrderType) VALUES
-- ('','','','','','','');
-- INSERT INTO Shipment (id,price,comment,id_Customer) VALUES
-- ('','','','');
-- INSERT INTO OrderType (id,name) VALUES
-- ('','');
-- INSERT INTO Warranty (id,expireDate) VALUES
-- ('','');
-- INSERT INTO Customer (id,name,phone,email,address) VALUES
-- ('','','','','');
-- INSERT INTO RepairAppl (id,comment,date,status,period,id_Customer,id_Machine) VALUES
-- ('','','','','','','');
-- INSERT INTO User (id,password,id_Customer) VALUES
-- ('','','');
-- INSERT INTO UserRoles (id,id_User,id_Roles) VALUES
-- ('','','');
-- INSERT INTO Roles (id,name) VALUES
-- ('','');

-- SELECT * FROM information_schema.columns WHERE table_name = 'roles'


-- SELECT * FROM requiredtools rt
-- LEFT JOIN machine m
-- ON m.model = rt.id_machine
-- LEFT JOIN tool t
-- ON t.id = rt.id_tool
-- GROUP BY m.model