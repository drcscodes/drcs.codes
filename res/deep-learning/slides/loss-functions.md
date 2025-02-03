---
title: Loss Functions
author: CS 4277 Deep Learning
institute: Kennesaw State University
aspectratio: 1610
fontsize: 10pt
colorlinks: yes
urlcolor: blue
header-includes:
- |
  ```{=latex}
  \input{beamer-common}
  %\titlegraphic{\includegraphics[width = 1in]{chris-simpkins-headshot-320px}}
  \usepackage{framed}
  \usepackage{xcolor}
  \usepackage{tikz,pgfplots}
  \let\oldquote=\quote
  \let\endoldquote=\endquote
  \colorlet{shadecolor}{cyan!15}
  \renewenvironment{quote}{\begin{shaded*}\begin{oldquote}}{\end{oldquote}\end{shaded*}}
  ```
---

## Loss Functions

The goal of a (eager) machine learning algorithm is to find the parameters of a model that produces the best possible mapping from inputs to outputs.

- We do this using a training data set $\{\bm{x}_i, \bm{y}_i\}_{i=1}^N$
- Training uses feedback from the mismatch betweeen the model's predicted $\hat{y}$s and the ground truth $y$s.
- A *loss function* returns a single number that represents this mismatch.
- So finding the best possible mapping from inputs to outputs reeduces to minimizing the loss function.


## Density Estimation

Say we have $N$ observations of a scalar $x$ which we denote with $\textbf{x} = (x_1, \dots, x_N)$.

- Estimating the distribution given the data is known as *density estimation*.
- We must assume a distribution, so we're estimating the parameters of the distribution.
- We assume data points are drawn independently and are identically-distributed.
    - This is known as the i.i.d. assumption


### Example: Likelihood of the Gaussian

Since our data set is i.i.d., the probability of the data set is

$$
p(\textbf{x}|\mu, \sigma^2) = \prod_{n=1}^N \mathcal{N}(x_n|\mu, \sigma^2)
$$

This is known as the *likelihood function* for the Gaussian.

## Maximum Likelihood

Finding the parameters of a distribution that maximize the probability of the observed data is known as *maximum likelihood estimation* (MLE).

In pracice, we transform likelihood functions into log likelihood functions.

Why log:

- Log of a function monotonically increasing and concave -- $\argmax \ln(f) = \argmax f$
- Log easy to work with: $\ln(ab) = \ln(a) + \ln(b)$, $\ln(\frac{a}{b}) = \ln(a) - \ln(b)$, $\ln e^x = x$
- Multiplying probabilities can underflow -- summing logs avoids this problem

```{=latex}
\begin{center}
```
![](LossLog.pdf){height="40%"}
```{=latex}
\end{center}
```


## Log Likelihood of Gaussian

For the Gaussian likelihood function we saw earlier, the log likelihood

```{=latex}
\begin{align*}
p(\textbf{x}|\mu, \sigma^2) &= \prod_{n=1}^N \mathcal{N}(x_n|\mu, \sigma^2)\\
p(\textbf{x}|\mu, \sigma^2) &= \prod_{n=1}^N \frac{1}{(2 \pi \sigma^2)^{\frac{1}{2}}} \exp(-\frac{1}{2 \sigma^2} (x_n - \mu)^2)\\
\ln p(\textbf{x}|\mu, \sigma^2) &= \sum_{n=1}^N \ln(\frac{1}{(2 \pi \sigma^2)^{\frac{1}{2}}} \exp(-\frac{1}{2 \sigma^2} (x_n - \mu)^2))\\
\ln p(\textbf{x}|\mu, \sigma^2) &= \sum_{n=1}^N \ln(1) - \ln(\sqrt{2 \pi}) - \ln(\sigma) - \frac{(x_i - \mu)^2}{2 \sigma^2}
\end{align*}
```

## Maximum Likelihood of Gaussian

If we take the partial derivative of the Gaussian log likelihood function with respect to $\mu$, set it to zero, and solve for $\mu$ we get:

$$
\mu_{ML} = \frac{1}{N} \sum_{n=1}^N x_n
$$

If we take the partial derivative with respect to $\sigma^2$ we get:

$$
\sigma^2_{ML} = \frac{1}{N} \sum_{n=1}^N (x_n - \mu_{ML})^2
$$

These should look familiar.  They are the sample mean and sample variance of the Gaussian.

## Loss Functions and Machine Learning Models

We seek a model $\bm{f}(\bm{x}, \bm(\phi))$ that computes a $\hat{\bm{y}}$ given an $\bm{x}$.

- We can recast this problem as the computation of a conditional probability $p(\bm{y}_i \ \bm{x}_i)$.
- Minimizing the loss corresponds to maximizing this conditional probability.

```{=latex}
\begin{center}
```
![](LossDataTypes.pdf){height="70%"}
```{=latex}
\end{center}
```

## General Maximum Likelihood Criterion

We choose a parametric distribution defined over the output domain $\bm{y}$ then train our model to compute the paramters, $\bm{\theta}$ of this distribution.

- If we choose a Gaussian distribution, then $\bm{\theta} = \{\mu, \sigma^2\}$.

We want to find the parameters of the model $\bm{\hat{\phi}}$ that maximize the conditional probability distribution $P(\bm{y}_i|\bm{\theta}_i)$ for all $\bm{y}_i$s.

```{=latex}
\begin{align*}
\bm{\hat{\phi}} &= \argmax_{\bm{\phi}}(\prod_{i=1}^I p(\bm{y}_i | \bm{x}_i))\\
\bm{\hat{\phi}} &= \argmax_{\bm{\phi}}(\prod_{i=1}^I p(\bm{y}_i | \bm{\theta}_i)\\
\bm{\hat{\phi}} &= \argmax_{\bm{\phi}}(\prod_{i=1}^I p(\bm{y}_i | \bm{f}(\bm{x}, \bm{\phi}))
\end{align*}
```

## Maximizing Log-Likelihood

Recalling that the total likelihood of the training data is:

$$
P(\bm{y}_1, \dots, \bm{y}_I | \bm{x}_1, \dots, \bm{x}_I) = \prod_{i=1}^I p(\bm{y}_i | \bm{x}_i)
$$

which is impractical due to underflow, so we prefer to maximize the log-likelihood:

```{=latex}
\begin{align*}
\bm{\hat{\phi}} &= \argmax_{\bm{\phi}}(\prod_{i=1}^I p(\bm{y}_i | \bm{f}(\bm{x}, \bm{\phi}))\\
\bm{\hat{\phi}} &= \argmax_{\bm{\phi}}(\log(\prod_{i=1}^I p(\bm{y}_i | \bm{f}(\bm{x}, \bm{\phi}))\\
\bm{\hat{\phi}} &= \argmax_{\bm{\phi}}(\sum_{i=1}^I log(p(\bm{y}_i | \bm{f}(\bm{x}, \bm{\phi}))
\end{align*}
```

## Minimizing Negative Log-Likelihood

By convention we minimize the loss function.  We can turn a maximization problem into a minimization problem by multiplying by -1.

```{=latex}
\begin{align*}
\bm{\hat{\phi}} &= \argmin_{\bm{\phi}}(-\sum_{i=1}^I log(p(\bm{y}_i | \bm{f}(\bm{x}, \bm{\phi}))\\
\bm{\hat{\phi}} &= \argmin_{\bm{\phi}}(L(\bm{\phi}))
\end{align*}
```

Which is the final form of our loss function $L(\bm{\phi})$

## Inference

Our network now computes a probability distribution over $\bm{y}$ instead of predicting $\hat{y}$.  To get a prediction, we return the maximum of the distribution:

$$
\bm{\hat{y}} = \argmax_{y}(p(\bm{y} | \bm{f}(\bm{x}, \bm{\phi}))
$$

This is often computed in terms of the parameters $\bm{\theta}$ predicted by the model.  E.g., for Gaussian the maximum is at $\mu$

## Recipe for Constructing and Using Loss Functions


Now that we understand MLE for loss functions, we can create a recipe for constructing loss functions for training data $\{\bm{x}_i, \bm{y}_i\}_{i=1}^I$ using the maximum likelihood approach:

1. Choose a suitable probability distribution $P(\bm{y} | \bm{\theta})$ defined over the predictions (output domain) $\bm{y}$ with distributoin parameters $\bm{\theta}$.
2. Set the machine learning model  $\bm{f}(\bm{x}, \bm{\phi})$ to predict one or more of these parameters, so $\bm{\theta} = \bm{f}(\bm{x}, \bm{\phi})$ and $P(\bm{y} | \bm{\theta}) = P(\bm{y} | \bm{f}(\bm{x}, \bm{\phi}))$.
3. To train the model, find the network paramters $\bm{\hat{\phi}}$ that minimize the negative log-likelihood loss function over the training data pairs $\{\bm{x}_i, \bm{y}_i\}$:

$$
\bm{\hat{\phi}} = \argmin_{\bm{\phi}}(L(\bm{\phi})) = \argmin_{\bm{\phi}}(-\sum_{i=1}^I log(p(\bm{y}_i | \bm{f}(\bm{x}, \bm{\phi}))
$$

4. To perform inference for a new test example $\bm{x}$, return either the full distribution $P(\bm{y} | \bm{f}(\bm{x}, \bm{\phi}))$ or the value where the distribution is maximized.
