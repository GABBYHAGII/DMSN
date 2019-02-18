import csv
import mysql.connector

# MYSQL logon
mydb = mysql.connector.connect(
  host="localhost",
  user="David",
  passwd="Sword",
  database="DMSN"
)
mycursor = mydb.cursor()

movies=[]

def getMovies():
    global movies
    data=[]
    with open('movies_metadata.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    index = len(data)
    for x in range(index):
        try:
            temp = (data[x][5], data[x][20])
            movies.append(temp)
        except:
            print(x, data[x][8])
    movies = set(tuple(x) for x in movies)
    movies = [ list (x) for x in movies ]
    return

def createMovieTable():
    global mydb
    global mycursor
    global movies

    tupleList = ()
    for x in movies:
        tupleList = tuple(x)
        sql = "INSERT INTO movies (id, movie) VALUES (%s, %s)"
        val = tupleList
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            print("Error Updating this record:")
            print(val)
    return

if __name__== '__main__':
    getMovies()
    createMovieTable()
