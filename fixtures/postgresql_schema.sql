CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TABLE customers (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    company_name VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);


CREATE TABLE events (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255),
    city varchar(150),
    date TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE orders (
  id VARCHAR(36) PRIMARY KEY,
  amount FLOAT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);


CREATE TRIGGER set_timestamp
BEFORE UPDATE ON orders
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();
