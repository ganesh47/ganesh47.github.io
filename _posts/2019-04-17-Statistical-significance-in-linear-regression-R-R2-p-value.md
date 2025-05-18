---
title: "R, R\u00b2, and p-value: Assessing Linear Regression"
date: 2019-04-17
categories: [blog]
tags: [statistics, python, numpy, linear-regression, r-squared, p-value]
author: Ganesh Raman
---

Linear regression offers a simple way to relate a numeric target with one or more features. Three terms often appear together when evaluating how strong that relation is:

* **R** – the correlation coefficient between predicted and actual values
* **R\u00b2** – the proportion of variance explained by the model
* **p-value** – the probability of observing a slope as extreme as the one estimated if the true slope were zero

The closer |R| is to 1 and the smaller the p-value, the more confident we are that a linear trend truly exists. R\u00b2 is just R squared, so a perfect fit has both R = ±1 and R\u00b2 = 1.

Below is a short Python snippet using `numpy` and `scipy` to illustrate these metrics:

```python
import numpy as np
from scipy import stats

# fake linear data with noise
rng = np.random.default_rng(42)
x = np.arange(50)
y = 2.0 * x + rng.normal(scale=10, size=x.size)

r = np.corrcoef(x, y)[0, 1]
r2 = r ** 2
slope, intercept, r_sc, p_value, _ = stats.linregress(x, y)

print(f"R={r:.3f}, R^2={r2:.3f}, p-value={p_value:.5f}")
```

Sample output might read `R=0.99, R^2=0.98, p-value=0.00000`, clearly indicating a strong and statistically significant linear relationship.

A high R\u00b2 alone isn't enough — we also need a low p-value to claim the slope is statistically different from zero. In practice, you typically look for `p < 0.05` as a conventional threshold for significance. When both R\u00b2 is large and the p-value is tiny, you can be confident your linear model captures a meaningful trend.

These metrics show up in a variety of disciplines whenever a linear association between two variables is tested. The correlation coefficient R quickly summarizes whether variables move together and in which direction, while R\u00b2 describes how much of the target's variability the regression line accounts for. Both statistics provide a sense of how tightly the data hug the line of best fit.

The p-value, on the other hand, stems from a hypothesis test on the slope. It answers the question: if there were no relationship at all, how probable is a slope as extreme as the one we've estimated? A small p-value suggests that chance alone is unlikely to explain the observed correlation, reinforcing that the regression captures a genuine effect. Together, R, R\u00b2, and the p-value indicate not just the quality of the fit but also its statistical reliability.

Further reading:

* [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
* [Coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination)
* [Hypothesis testing](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing)

---

*Published on Apr 17, 2019 — written by Ganesh Raman.*
