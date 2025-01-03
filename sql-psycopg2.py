import psycopg2

# Connect to the database
connection = psycopg2.connect(database="chinook")

# Open a cursor to perform database operations
cursor = connection.cursor()

#Query 1
# cursor.execute('SELECT * FROM "Artist"')

#Query 2
# cursor.execute('SELECT "Name" FROM "Artist"')

#Query 3
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

#Query 4
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

#Query 5
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

#Query 6
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])

#fetch the results
results=cursor.fetchall()

#fetch the result (single)
# results=cursor.fetchone()

connection.close()

for result in results:
    print(result)