from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import pymysql


password1 = os.getenv("KEY")
user1 = os.getenv("USER")
host1 = os.getenv("HOST")
# MySQL connection URL without specifying the database name
SQLALCHEMY_DATABASE_URL = f"mysql://{user1}:{password1}@{host1}/"

database_name = 'Kanye'

# Create a connection to the MySQL server without specifying a database
connection = pymysql.connect(
    host= host1,
    user= user1,
    password= password1
)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Execute SQL query to create the database if it doesn't exist
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")

# Close the cursor and the connection
cursor.close()
connection.close()

# Add the database name to the connection URL
SQLALCHEMY_DATABASE_URL += database_name

# Create the engine with the database specified
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()