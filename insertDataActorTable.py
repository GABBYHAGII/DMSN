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

actors=[]

def getActors():
    global actors
    data=[]
    with open('credits.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    # code below is work in progress to scan string for actor names
    names = data[x][0]
    namesLen = len(names)
    for n in range(namesLen):
        if()
    # code above is work in progress
    
    index = len(data)
    for x in range(index):
        try:
            temp = (data[x][2], data[x][0])
            actors.append(temp)
        except:
            print(x, data[x][2])
    actors = set(tuple(x) for x in actors)
    actors = [ list (x) for x in actors ]

    return

def createActorTable():
    global mydb
    global mycursor
    global actors

    tupleList = ()
    for x in actors:
        tupleList = tuple(x)
        sql = "INSERT INTO actors (id, actor) VALUES (%s, %s)"
        val = tupleList
        #try:
        mycursor.execute(sql, val)
        mydb.commit()
        '''
        except:
            print("Error Updating this record:")
            print(val)
        '''
    return

if __name__== '__main__':
    getActors()
    #createActorTable()
