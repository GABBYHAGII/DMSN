import csv
import itertools
#"soc-youtube-snap.txt"
#"email-Eu-core.txt"
with open("newmovies.txt", encoding="utf8") as file:
    with open("movies.csv", "w", encoding="utf8") as output:
        data = file.readlines()
        writer = csv.writer(output)

        for d in data:
            d = d.split()
            writer.writerow(d)
