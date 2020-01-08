CREATE TABLE customers (
    id BINARY(16) PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    company_name VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);


CREATE TABLE event (
    id BINARY(16) PRIMARY KEY,
    name VARCHAR(255),
    city varchar(150),
    date TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE orders (
  id BINARY(16) PRIMARY KEY,
  amount FLOAT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE now()
);
