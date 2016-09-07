[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> According to the Cohen's d coefficient, it appears that first babies are lighter than others. The coefficient value came out as -0.0887, which implies that babies that are born first are on average lighter than those born afterwards, properly weighted by the pooled standard deviation. In addition, first babies appear to have longer pregnancy lengths than those born after, with a Cohen's d coefficient of pregnancy length between the two groups of 0.0289. Therefore, it seems that first born babies in a family stay in the womb longer, but are lighter at birth than their siblings. This could possibly be explained by a mother's diet between first and second birth, and that they may be more comfortable giving birth after the first experience.

>>Code:
```python
from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2

def CohenEffectSize(group1, group2):

    diff = group1.mean() - group2.mean()

    n1, n2 = len(group1), len(group2)
    var1 = group1.var()
    var2 = group2.var()

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
    
d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print('Cohen d', d)
preg_length = thinkstats2.CohenEffectSize(firsts.prglngth, others.prglngth)
print('Cohen d preg', preg_length)
```
