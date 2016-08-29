# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are very similar in the sense that they are both sequences of values that can be of any type, and are indexed by integers. The key distinction is that tuples are immutable, so their values may not be changed after assignment. With lists, however, one can overwrite an index values and update indices when it is appropriate. Nevertheless, tuples may still be changed if their index values reference a mutable object, such as list.

>> Tuples may be used as keys in dictionaries primarily because Python does not allow one to use lists in such a setting. This is because dictionary keys must be immutable, and for the most part tuple values are immutable and thus may be utilized as keys (as long as every element of the tuple is itself immutable). Thus, we can use a tuple as key that contains integers, strings, and other tuples with references to immutable objects.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Again, sets and lists are sequences of values that can take on any type. They are also both mutable types, and thus can be updated and altered after their creation. One key difference between the two is that sets only allow for unique values, and thus do not contain duplicates. Sets are also unordered, whereas lists are ordered and may be sorted as such. An time when we would prefer to use a set is when we do not care about order, but are concerned with only unique values. An example would be when we are keeping track of peoples contact information. Obviously we don't want more than one entry per person, and could implement a set to ensure that each individual has their own unique value that maps to their information. If we do want duplicates however, and if order matters, we should use a list. An example of when this would be appropriate is when we are keeping track of the frequency of certain purchases, say at the grocery store, over time. In this instance, both allowing for duplicate purchases and keeping track of the order in which items were bought could be of interest, and thus a list would be preferred to a set.

>> When we want to find a specific element, sets are faster than lists because they store elements in a hashtable. Thus, whenever we add an element to a set, its position is determined using the hash of the set. This is simultaneously why sets do not preserve the order of the sequence in question, but also why they are faster than lists in finding a specific element. With a list, the computer must iterate over the entire sequence, while with a set it simply goes directly to the has where the element should be stored and checks to see if it exists.
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





