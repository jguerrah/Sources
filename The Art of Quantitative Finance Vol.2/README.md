# The Art of Quantitative Finance Vol.2

Volume 2 is the second of a 3 volumne series including:

1. Trading, Derivatives and Basic Concepts
2. Volatilities, Stochastic Analysis and Valuation Tools
3. Risk, Optimal Portfolios and Case Studies

Volume 2 contains 3 chapters

The book is kind of informal, so notes will be just listed as bullets

## Chapter 1. Volatilities

### 1.1. Volatility I: Historical Volatility

- Simple and inexact definition: volatility of a financial asset’s price expresses the fluctuation of the (continuous or discrete) returns of that asset’s price

> **Historical volatility of the stock A per time unit dt in the time range [0, T]**
> $$\sigma'_A = \sqrt{ \frac{1}{N} \sum_{i=0}^{N-1} (a_i - \mu'_A)^2 } $$
> where:
>  - $a_i = \log (\frac{A_{i+1}}{A_i})$ for $i = 0, 1, ..., N-1 $
>  - $\mu'_A = \frac{1}{N} \sum_{i=0}{N-1} a_i$
>  - $N$: number of equal parts of $[0, T]$ of lenght $dt$

### 1.2. Volatility II: ARCH Models
