CREATE TABLE branch(
  branch_ID NUMERIC(9),
  street_number INTEGER NOT NULL,
  street_name VARCHAR(20),
  city VARCHAR(20),
  state CHAR(2),
  zip NUMERIC(5),
  PRIMARY KEY (branch_ID)
);

CREATE TABLE employee(
  SSN NUMERIC(9),
  first_name VARCHAR(256),
  last_name VARCHAR(256),
  street_number INTEGER NOT NULL,
  street_name VARCHAR(20),
  apt_number NUMERIC(10),
  city VARCHAR(20),
  state CHAR(2),
  zip NUMERIC(5)
  employee_type VARCHAR(20),
  salary NUMERIC(8,2),
  branch_ID NUMERIC(9),
  PRIMARY KEY (SSN),
  FOREIGN KEY branch_ID references branch(branch_ID),
  CHECK (employee_type = 'teller' OR occupation = 'loan specialist' OR occupation = 'manager')
);

CREATE TABLE customer(
  SSN NUMERIC(9),
  first_name VARCHAR(256),
  last_name VARCHAR(256),
  street_number INTEGER NOT NULL,
  street_name VARCHAR(20),
  apt_number NUMERIC(10),
  city VARCHAR(20),
  state CHAR(2),
  zip NUMERIC(5),
  branch_ID NUMERIC(9),
  PRIMARY KEY (SSN),
  FOREIGN KEY branch_ID references branch(branch_ID),
);

CREATE TABLE account(
  account_num NUMERIC(12),
  account_type VARCHAR(20),
  balance NUMERIC(30,2),
  PRIMARY KEY (account_num)
);

CREATE TABLE loan(
  loan_ID NUMERIC(9),
  account VARCHAR(20),
  runtime INTEGER NOT NULL,
  interest_schedule VARCHAR(256),
  PRIMARY KEY (loan_ID)
);

CREATE TABLE transaction(
  transaction_ID NUMERIC(9),
  transaction_type CHAR(10),
  transaction_amount NUMERIC(30,2),
  description VARCHAR(256),
  PRIMARY KEY (transaction_ID)
);
