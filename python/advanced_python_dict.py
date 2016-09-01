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
		
print({item: faculty_dict[item] for item in faculty_dict.keys()[:3]})

#Q7.

professor_dict = {}
for i in range(1, len(list_all)):
	full_name = list_all[i][0].split()
	first_last = (full_name[0], full_name[-1])
	list_all[i][1] = list_all[i][1].strip() #removing white space from degree name
	
	list_all[i][2] = list_all[i][2].rsplit(' ', 2)[0] #removing end of title name
	professor_dict[first_last] = ([list_all[i][1], list_all[i][2], list_all[i][3]])

print({item: professor_dict[item] for item in professor_dict.keys()[:3]})

#Q8.

professor_dict = {}
for i in range(1, len(list_all)):
	full_name = list_all[i][0].split()
	first_last = (full_name[0], full_name[-1])
	list_all[i][1] = list_all[i][1].strip() #removing white space from degree name
	list_all[i][2] = list_all[i][2].rsplit(' ', 2)[0] #removing end of title name
	professor_dict[first_last] = ([list_all[i][1], list_all[i][2], list_all[i][3]])

alphabetical = sorted(professor_dict, key = lambda name: name[1])
for item in alphabetical:
	print({item: professor_dict[item]})
