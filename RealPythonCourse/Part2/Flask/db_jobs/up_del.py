import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE population SET population = 9000000 WHERE city='New York'")
    c.execute("DELETE from population WHERE city='Phoenix'")

    print("\nNEWDATA:\n")

    c.execute("SELECT * from population")

    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])
