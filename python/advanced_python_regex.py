Q1. 
import csv
import urllib2
import re

url = "https://raw.githubusercontent.com/travishjames/dsp/master/python/faculty.csv"
response = urllib2.urlopen(url)
cr = csv.reader(response)
list_all = list(cr)

total_degrees = [item[1] for item in list_all]
unique_degrees = {}
for i in range(1, len(total_degrees)):
	faculty_cred = total_degrees[i].split()
	for j in faculty_cred:
		j = re.sub('[^\w]+', '', j)
		if j in unique_degrees:
			unique_degrees[j] += 1
		else:
			unique_degrees[j] = 1
		
print(unique_degrees)
print(len(unique_degrees))

Q2.

import csv
import urllib2
import re

url = "https://raw.githubusercontent.com/travishjames/dsp/master/python/faculty.csv"
response = urllib2.urlopen(url)
cr = csv.reader(response)
list_all = list(cr)

total_titles = [item[2] for item in list_all]
unique_titles = {}
for t in range(1, len(total_titles)):
	title = total_titles[t].rsplit(' ', 2)[0] #cutting off final two words from title since redundant and irrelevant
	if title in unique_titles:
		unique_titles[title] += 1
	else:
		unique_titles[title] = 1

print(unique_titles)
print(len(unique_titles))

Q3.


Q4.

