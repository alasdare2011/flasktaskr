import sqlite3 #sqlite database library
from _config import DATABASE_PATH #get database location from config file
    
with sqlite3.connect(DATABASE_PATH) as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
        status INTEGER NOT NULL)""")

    #insert dummy data into text
    c.execute(
        'INSERT INTO tasks(name, due_date, priority, status)'
        'VALUES("FINISH THIS TUTORIAL", "03/25/2015", 10, 1)'
    )

    c.execute(
        'INSERT INTO tasks(name, due_date, priority, status)'
        'VALUES("Finish Real Python Course 2", "03/25/2015", 10, 1)'
    )


