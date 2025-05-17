---
title: "Using `pd.cut` for Stratified Binning in Pandas"
date: 2019-01-28
categories: [blog]
tags: \[pandas, python, stratification, binning, cut, data-prep]
author: Ganesh Raman
---

When preparing data for machine learning or statistical analysis, you often need to **transform continuous variables into categorical bins**. This is where **`pandas.cut`** becomes invaluable.

## What is `pd.cut`?

`pd.cut` is a Pandas utility to segment and sort data values into discrete bins:

```python
import pandas as pd
import numpy as np

ages = pd.Series([5, 12, 17, 24, 35, 45, 52, 63, 78])
binned = pd.cut(ages, bins=[0, 18, 35, 60, 100], labels=["Child", "Young Adult", "Adult", "Senior"])
print(binned)
```

Output:

```
0       Child
1       Child
2       Child
3    Young Adult
4    Young Adult
5         Adult
6         Adult
7         Adult
8        Senior
```

## Why Use `cut`?

* Converts continuous variables into **categorical features**
* Facilitates **stratified sampling** by group
* Makes histograms and frequency plots more interpretable
* Useful for **feature engineering** in ML pipelines

## Stratified Sampling Use Case

Suppose you want to split a population dataset for training/testing with **even age distribution**. You can first bin the data using `cut`:

```python
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 60, 100])
stratified_sample = df.groupby('age_group', group_keys=False).apply(lambda x: x.sample(frac=0.2))
```

This ensures each age group is proportionally represented in your sample — a critical aspect of **stratified sampling**.

## Additional Features

* **Automatic bin calculation** with `bins=int`:

```python
pd.cut(data, bins=5)  # Creates 5 equally spaced bins
```

* **Right-inclusive or not** via `right=True|False`
* **Return bin edges** with `retbins=True`
* Works well with **plotting**:

```python
df['binned'] = pd.cut(df['value'], bins=5)
df['binned'].value_counts().plot(kind='bar')
```

## When Not to Use It

* If bins should have **equal number of observations**, use `pd.qcut` instead (quantile-based)
* If input is **ordinal** but non-numeric, consider mapping directly via `pd.Categorical`

## Final Thoughts

`pd.cut` is a deceptively simple API that solves an essential data preparation need: **turning continuous measurements into stratified or grouped categories**. Whether you're building ML pipelines or preparing reports, it gives you expressive control over how to discretize your data.

> With just one line, `pd.cut` brings structure and clarity to numeric chaos.

---

*Published on Jan 28, 2019 — written by Ganesh Raman.*
