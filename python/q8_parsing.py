import csv
import urllib2

url = "https://raw.githubusercontent.com/thisismetis/dsp/master/python/football.csv"
response = urllib2.urlopen(url)
cr = csv.reader(response)
list = list(cr)
goal_diff = {}

for x in range(1, len(list)):
	goal_diff[list[x][0]] = abs(int(list[x][5]) - int(list[x][6]))

print(min(goal_diff, key = goal_diff.get))

##The team with the smallest difference in for and against goals in Aston Villa.

