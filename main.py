from collections import defaultdict
import re
bigfile = open('genres.list','r')
movies = bigfile.readlines()
bigfile.close()
genres = defaultdict(lambda:defaultdict(lambda:0))
parser = re.compile(".*\((\d+).*\)[\w {}.:&\'-,!?]*\t*([\w-]+)\n")
fails = []
for movie in movies:
	line = parser.match(movie)
	if line:
		year = line.group(1)
		genre = line.group(2)
		genres[year][genre]+=1
	elif "SUSPENDED" in movie:
		continue
	elif '????' not in movie:
		fails.append(movie)