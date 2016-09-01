import csv
import urllib2

url = "https://raw.githubusercontent.com/travishjames/dsp/master/python/faculty.csv"
response = urllib2.urlopen(url)
cr = csv.reader(response)
list_all = list(cr)

#Q6.

faculty_dict = {}
for i in range(1, len(list_all)):
	list_all[i][0] = list_all[i][0].rsplit(' ', 1)[-1] #removing first name
	list_all[i][1] = list_all[i][1].strip() #removing white space from degree name
	list_all[i][2] = list_all[i][2].rsplit(' ', 2)[0] #removing end of title name
	if list_all[i][0] in faculty_dict:
		faculty_dict[list_all[i][0]].append([list_all[i][1], list_all[i][2], list_all[i][3]])
	else:
		faculty_dict[list_all[i][0]] = [list_all[i][1], list_all[i][2], list_all[i][3]]
		
print(faculty_dict)

#Q7.



#Q8.

