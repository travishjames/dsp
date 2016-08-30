# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

from datetime import datetime

def countdays(d1, d2):
	
	date_format = "%m-%d-%Y"
	a = datetime.strptime(d1, date_format)
	b = datetime.strptime(d2, date_format)
	delta = b - a
	print (delta.days)
	
countdays("01-02-2013", "07-28-2015")

####b)  
date_start = '12312013'  
date_stop = '05282015'  

from datetime import datetime

def countdays(d1, d2):
	
	date_format = "%m%d%Y"
	a = datetime.strptime(d1, date_format)
	b = datetime.strptime(d2, date_format)
	delta = b - a
	print (delta.days)
	
countdays("12312013", "05282015")

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

from datetime import datetime

def countdays(d1, d2):
	
	date_format = "%d-%b-%Y"
	a = datetime.strptime(d1, date_format)
	b = datetime.strptime(d2, date_format)
	delta = b - a
	print (delta.days)
	
countdays("15-Jan-1994", "14-Jul-2015")
