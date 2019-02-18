import mysql.connector
import csv

# MYSQL logon
mydb = mysql.connector.connect(
  host="localhost",
  user="David",
  passwd="Sword",
  database="twitch"
)
mycursor = mydb.cursor()

'''
mycursor.execute("SELECT name FROM top_games")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#print(len(myresult))

mycursoor.execute("SELECT ")
'''

sql = "SELECT \
    top_games.name AS game, \
    streams.viewer_count AS views \
    FROM top_games \
    JOIN streams ON top_games.id = streams.game_id"

mycursor.execute(sql)

myresult = mycursor.fetchall()
#myresult = list(myresult)
streamIndex = len(myresult)
games = set()
for x in range(streamIndex):
    games.add(myresult[x][0])

games = list(games)
gameIndex = len(games)
##print(myresult[1][1])
gameTotalViews = []

for x in range(gameIndex):
    game = str(games[x])
    totalViews = 0
    for n in range(streamIndex):
        game2 = str(myresult[n][0])
        if (game in game2):
            views = myresult[n][1]
            totalViews = totalViews + views
    temp = game, totalViews
    gameTotalViews.append(temp)

with open('streamViewCount', 'w', encoding='utf-8-sig') as f:
    w = csv.writer(f, gameTotalViews)
    w.writerow(['game', 'total_views'])
    for x in gameTotalViews:
        w.writerow(x)
