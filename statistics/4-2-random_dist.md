[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> The exercise asks us to generate 1000 random numbers and see if the generator is in fact "random". The do so, one must visualize the PMF and CDF of the values generated, and see if they follow a uniform distribution. The following two images are the PMF and CDF generated from my python code, respectively:

![PMF Graph](https://github.com/travishjames/dsp/blob/master/img/chap04ex02PMF.png)
![CDF Graph](https://github.com/travishjames/dsp/blob/master/img/chap04ex02CDF.png)

>>As we can see, each value on the x-axis of the PMF is mapped to the same probability of 0.0010, implying that every number has an equal chance of being generated. Looking at the CDF, we have a relatively straight line diagonally increasing from the bottom-left corner, which also implies a uniform distribution of values. Therefore, the random number generator does appear to be creating numbers in a sufficiently random fashion.

Code:
```python
import thinkstats2
import thinkplot
import random

t = [random.random() for _ in range(1000)]
pmf = thinkstats2.Pmf(t)
thinkplot.Pmf(pmf, linewidth = 0.1, label = "PMF(x)")
thinkplot.Show()

cdf = thinkstats2.Cdf(t)
thinkplot.Cdf(cdf, label = "Cumulative Percent")
thinkplot.Show()
```
