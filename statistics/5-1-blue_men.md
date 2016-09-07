[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> When we have a normal distribution, if we want to see what percentage of the population falls within a certain range, we can simply find the area under the normal curve to the left of the right end point, and subtract the area from the left end point. With a Z-statistic table, these two values are very easy to look up, and the hardest part of the procedure is really just confirming that our distribution is actually normal. Since we are told that it is, we may proceed by generating a normal distribution with the relevant mean and s.d. values (178 cm and 7.7 cm in this case). We may then figure out the area under the normal curve to the left of 185.4 cm (6'1") and subtract the area under the curve to the left of 177.8 cm (5'10"). After doing so, we get that approximately 34.21% of the population meets the height requirement to be in the blue man group.

Code:
```python
from __future__ import print_function, division
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

dist.mean(), dist.std()

dist.cdf(mu-sigma)

low = dist.cdf(177.8)
high = dist.cdf(185.4)
print(low, high, high-low)
```
