
import csv

data = []
with open('movies_metadata.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

index = len(data)
mData = []
for x in range(index):
    genre = data[x][3]
    genLen = len(genre)
    start = 0
    finish = 0
    for n in range(genLen):
        if(genre[n].isupper()):
            start = n
        if("'" in genre[n]):
            finish = n
    newGenre = (genre[start:finish])
    if (newGenre == ""):
        newGenre = "Unknown"
    try:
        temp = (data[x][20], newGenre)
        mData.append(temp)
    except:
        print(x, data[x][8])

mData =[x for x in mData if x!= []]

with open("movie_genres.csv", "w", newline='', encoding="utf8") as output:
    writer = csv.writer(output)
    for d in mData:
        writer.writerow(d)
