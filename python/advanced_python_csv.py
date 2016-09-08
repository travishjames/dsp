import csv
import urllib2

url = "https://raw.githubusercontent.com/travishjames/dsp/master/python/faculty.csv"
response = urllib2.urlopen(url)
cr = csv.reader(response)
list_all = list(cr)

emails = [list_all[item][3] for item in range(1, len(list_all))]
with open('emails_metisdsp.csv', 'w') as csvfile:
	fieldname = ['email']
	writer = csv.DictWriter(csvfile, fieldnames = fieldname)
	for item in emails:
		writer.writerow({'email': item})
