[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> The following graph shows the actual and biased distribtions of the responses to the survey of the number of children per household. The biased group includes the responses of the children themselves, which leaves out important data of families who have zero children, and inflates the number of large families as children with many siblings are more likely to respond to the survey.

![Actual vs Biased Distributions](https://github.com/travishjames/dsp/blob/master/img/chap03ex01actual_biased.png)

>>As we can see, the biased data is biased towards each respondent being from a larger family. The hump in the distribution is clearly located to the right of that of the actual distribution, and thus the data is inflated towards larger values than are actually present in the true data. When, computing the means of both sets of data, I get that the average number of children per family is 1.024 for the actual data and 2.404 for the biased data. This reinforces the finding from the distribution plot that the biased data is incorrectly inflated upwards, and shows how misleading findings from biased data can be.

Code:

```python
import thinkstats2
import thinkplot
import chap01soln

resp = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label = "actual")

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
    
biased = BiasPmf(pmf, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()

print(pmf.Mean())
print(biased.Mean())
```
