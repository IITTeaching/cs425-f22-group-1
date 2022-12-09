CREATE TABLE branch(
  branch_ID INT,
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
  street_name VARCHAR(20) NOT NULL,
  apt_number NUMERIC(10),
  city VARCHAR(20),
  state CHAR(2),
  zip NUMERIC(5),
  employee_type VARCHAR(20),
  salary NUMERIC(8,2),
  branch_ID INT,
  PRIMARY KEY (SSN),
  FOREIGN KEY (branch_ID) references branch(branch_ID),
  CHECK (employee_type = 'teller' OR employee_type = 'loan specialist' OR employee_type = 'manager')
);

CREATE TABLE customer(
  SSN NUMERIC(9),
  first_name VARCHAR(256),
  last_name VARCHAR(256),
  street_number INTEGER NOT NULL,
  street_name VARCHAR(20) NOT NULL,
  apt_number NUMERIC(10),
  city VARCHAR(20),
  state CHAR(2),
  zip NUMERIC(5),
  branch_ID INT,
  monthly_statement VARCHAR(20),
  pending_transaction VARCHAR(20),
  balance INT,
  fees INT,
  PRIMARY KEY (SSN),
  FOREIGN KEY (branch_ID) references branch(branch_ID)
);

CREATE TABLE account3(
  account_num serial,
  account_type VARCHAR(20),
  balance NUMERIC(30,2),
  customerssn NUMERIC(9),
  branch_account INT,
  PRIMARY KEY (account_num)
);

CREATE TABLE loan(
  loan_ID NUMERIC(9),
  account VARCHAR(20),
  runtime INTEGER NOT NULL,
  interest_schedule VARCHAR(256),
  PRIMARY KEY (loan_ID)
);

CREATE TABLE tran(
  transaction_ID NUMERIC(9),
  transaction_type CHAR(10),
  transaction_amount NUMERIC(30,2),
  description VARCHAR(256),
  PRIMARY KEY (transaction_ID)
);

insert into branch values('24',55,'South Temple','Chicago','IL','60616');
insert into branch values('25',56,'South Temple','Chicago','IL','60616');

insert into employee values(123456789,'John','Smith',45,'South Temple',5,'Chicago','IL','60616','manager',70000,25);
insert into employee values(987654321,'Abby','Smith',45,'South Temple',5,'Chicago','IL','60616','teller',70000,25);

insert into customer values(246812340,'Julie','Smith',45,'South Temple',5,'Chicago','IL','60616',25,'April','pending transfer',50,20);

-- Database: bankingsystem

-- DROP DATABASE IF EXISTS bankingsystem;