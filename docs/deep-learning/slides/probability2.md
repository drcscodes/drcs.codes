
## Probability Densities

```{=latex}
\begin{center}
```
![](bishop-dl-fig2.6.pdf){height="60%"}
```{=latex}
\end{center}
```

## Distributions

```{=latex}
\begin{center}
```
![](bishop-dl-fig2.7.pdf){height="60%"}
```{=latex}
\end{center}
```

- Red is uniform over $(-1, 1)$
- Blue is exponential with $\lambda = 1$
- Green is Laplace with $\mu = 1$ and $\gamma = 1$

## Uniform Distribution

2.2.1

## Exponential Distribution

2.2.1

## Lapace Distribution

2.2.1

## Dirac Delta Function

2.2.1

## Expectations

2.2.2

The *expected value* or *mean* or *forst moment* of a random variable $X$ is the weighted average of the

## Covariances

2.2.2

## The Gaussian Distribution

2.3

Why the Gaussian is so widely used:

- Two easily interpretable parameters: mean and variance
- By Central Limit Theorem, sum of independent variables have ~ Gaussian distribution
    - Makes a good choice for modeling noise
- Given a mean and variance, Gaussian makes least number of assumptions, i.e., has maximum entropy
- Simple mathematical form -- easily to implement but usually highly effective

## The Gaussian Distribution

2.3

## Mean and Variance

2.3.1

## Likelihood Function

2.3.2

## Maximum Likelihood

2.3.2

Why log:

- Log of a function monotonically increasing and concave -- $\argmax ln(f) = \argmax f$
- Log easy to work with: $\ln(ab) = \ln(a) + \ln(b)$, $\ln(\frac{a}{b}) = \ln(a) - \ln(b)$
- Multiplying probabilities can underflow -- summing logs avoids this problem

## Bias of Maximum Likelihood

2.3.3

## Linear Regression

2.3.4

## Transformation of Densities

2.4

Maybe save for the Normalizing Flows lesson

## Multivariate Distributions

2.4.1

Maybe save for the Normalizing Flows lesson

## Information THeory

2.5

## Entropy

2.5.1

## Physics Perspective

2.5.2

## Differential Entropy

2.5.3

## Maximum Entropy

2.5.4

## Kullback-Leibler Divergence

2.5.5

## Conditional Entropy

2.5.6

## Mutual Information

2.5.7

## Bayesian Probabilities

2.6

## Model Parameters

2.6.1

## Regularization

2.6.2

Maximum Aposteriori (MAP) estimate

## Bayesian Machine Learning

2.6.3

## Closing Thoughts

Boom!

