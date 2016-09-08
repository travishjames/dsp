# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
	string = 'Number of donuts: '
	if count < 10:
		 string += str(count)
	else:
		string += 'many'
	
	return string

def both_ends(s):
    if len(s) < 2:
		return ''
	else:
		return s[:2] + s[len(s)-2:]


def fix_start(s):
	char = s[0]
	string = char
	for x in range(1, len(s)):
		if s[x] == char:
			string += '*'
		else:
			string += s[x]
	return string


def mix_up(a, b):
	str1 = a[:2]
	a = b[:2] + a[2:]
	b = str1 + b[2:]
	return a + ' ' + b


def verbing(s):
	if len(s) < 3:
		return s
	elif s.endswith('ing'):
		return s + 'ly'
	else:
		return s + 'ing'


def not_bad(s):
	if ('not' in s) & ('bad' in s):
		if s.index('not') < s.index('bad'):
			return s[:s.index('not')] + 'good' + s[s.index('bad')+3:]
	return s


def front_back(a, b):
    if len(a)%2 == 0:
		if len(b)%2 == 0:
			return a[:len(a)/2] + b[:len(b)/2] + a[len(a)/2:] + b[len(b)/2:]
		else:
			return a[:len(a)/2] + b[:len(b)/2+1] + a[len(a)/2:] + b[len(b)/2+1:]
	else:
		if len(b)%2 == 0:
			return a[:len(a)/2+1] + b[:len(b)/2] + a[len(a)/2+1:] + b[len(b)/2:]
		else:
			return a[:len(a)/2+1] + b[:len(b)/2+1] + a[len(a)/2+1:] + b[len(b)/2+1:]
    
