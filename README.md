# cs425-f22-group-1
Andrijana Sajic, Akina Castellano, Julia Ivaniv

To execute:
The python code was run in Jupyter notebook. The final code is called FinalCode.py
Please make sure tkinter and psycopg2 are installed
Change the top lines of code:

conn = psycopg2.connect(user="postgres",
                                  password="Kirbygenius2022",
                                  host="localhost",
                                  port="5433",
                                  database="bankingsystem")
         
Change the user, password, host, and port accordingly

The sql database is called bankingsystem. Please use the code called Final_DDL_Script.sql in pgAdmin to 
load our database and test tables. View the tables in order to use the test data. 
