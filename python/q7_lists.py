# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
	count = 0
	for x in words:
		if len(x) > 1:
			if x[0] == x[len(x)-1]:
				count+=1
	return count


def front_x(words):
	words = sorted(words, key=lambda x: x.split()[0])
	list = []
	for i in words:
		if i[0] == 'x':
			list.append(i)
	for j in words:
		if j[0] != 'x':
			list.append(j)
	return list


def sort_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])


def remove_adjacent(nums):
	list = []
	if len(nums) > 0:
		for i in range(0, len(nums)-1):
			if nums[i] != nums[i+1]:
				list.append(nums[i])
		list.append(nums[len(nums)-1])
	return list


def linear_merge(list1, list2):
	list1.extend(list2)
	return sorted(list1, key=lambda x: x.split()[0])
