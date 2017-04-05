import sqlite3

# create db connection
conn = sqlite3.connect("new.db")
# create cursor to work with database
cursor = conn.cursor()

# execute SQL query
cursor.execute("INSERT INTO population VALUES('New York City', \
    'NY', 8400000)"
               )


# commit changes to database
conn.commit()
# close connection to db after we are done working with it
conn.close()
