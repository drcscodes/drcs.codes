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
3. To train the model, find the network parameters $\bm{\hat{\phi}}$ that minimize the negative log-likelihood loss function over the training data pairs $\{\bm{x}_i, \bm{y}_i\}$:

$$
\bm{\hat{\phi}} = \argmin_{\bm{\phi}}(L(\bm{\phi})) = \argmin_{\bm{\phi}}(-\sum_{i=1}^I log(p(\bm{y}_i | \bm{f}(\bm{x}, \bm{\phi}))
$$

4. To perform inference for a new test example $\bm{x}$, return either the full distribution $P(\bm{y} | \bm{f}(\bm{x}, \bm{\phi}))$ or the value where the distribution is maximized.

Now we see this recipen applied to three common problems: univariate regression, binary classification, and multiclass classification.

## Example 1: Univariate Regression

Goal: predict a single output $y \in \mathbb{R}$ from input $\bm{x}$ using model $f(\bm{x}, \bm{\phi})$.

1. Choose a distribution over output $y$.

$$
p(y|\mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma*2}}\exp(-\frac{(y-\mu)^2}{2\sigma^2})
$$

2. Set the machine learning model $f(\bm{x}, \bm{\phi})$ to compute one or more parameters of the distribution.  Here, we choose only the mean $\mu = f(\bm{x}, \bm{\phi})$:

$$
p(y|f(\bm{x}, \bm{\phi}), \sigma^2) = \frac{1}{\sqrt{2\pi\sigma*2}}\exp(-\frac{(y - f(\bm{x}, \bm{\phi}))^2}{2\sigma^2})
$$

3. Calculate the negative log-likelihood for our chosen parameter(s) to use as the loss function.  We already did this for the Gaussian earlier; here we substitute $f(\bm{x}, \bm{\phi})$ for $\mu$ and $y_i$ for $x_i$ since we're calculating the distribution parameter over the output:

$$
L(\bm{\phi}) = \sum_{i=1}^I \ln(1) - \ln(\sqrt{2 \pi}) - \ln(\sigma) - \frac{(y_i - f(\bm{x}, \bm{\phi}))^2}{2 \sigma^2}
$$

## 3.1: Least-Squares Loss Function

Our negative log-likelihood function is unwieldy, so do some algebraic manipulations.

$$
L(\bm{\phi}) = \sum_{i=1}^I \ln(1) - \ln(\sqrt{2 \pi}) - \ln(\sigma) - \frac{(y_i - f(\bm{x}, \bm{\phi}))^2}{2 \sigma^2}
$$

First, remove terms that don't depend on $\bm{\phi}$:

$$
L(\bm{\phi}) = \sum_{i=1}^I \frac{(y_i - f(\bm{x}, \bm{\phi}))^2}{2 \sigma^2}
$$

Next, remove denominator since it's a positive scaling factor that doesn't affect the position of the minimum:

$$
L(\bm{\phi}) = \sum_{i=1}^I (y_i - f(\bm{x}, \bm{\phi}))^2
$$

And this is the familiar least squares loss function you get when you assume that your outputs $Y$ are i.i.d. and each $y_i \sim \mathcal{N}(y_i|, f(\bm{x}, \bm{\phi}), \sigma^2)$

## 4: Inference

The model doesn't predict $y$ directly, instead it predicts the mean of the Gaussian distributoin assumed to generate $y$.  We turn that into a predicted $y$ with:

$$
\hat{y} = \argmax_y ( p(y|f(\bm{x}, \hat{\bm{\phi}}), \sigma^2) )
$$

Since for the univariate Gaussian the mean $\mu$ is the most likely value, inference is simply

$$
\hat{y} = f(\bm{x}, \hat{\bm{\phi}})
$$

## Heteroscedatic vs Homoscedatic Regression

:::: {.columns}
::: {.column width="60%"}

- In *homoscedatic* regression, the variance is constant across all data points.
- In *heteroscedatic* regression, the variance varies as a function of the input data.

To handle heteroscedatic regression, you can train a network to to compute both mean and variance.

```{=latex}
\begin{align*}
\mu &= f_1(\bm{x}, \bm{\phi})\\
\sigma^2 &= f_2(\bm{x}, \bm{\phi})^2 \tag{Square output to ensure positive}
\end{align*}
```

:::
::: {.column width="40%"}

![](LossHeteroscedastic.pdf)

:::
::::

The loss function is then:

$$
\hat{\bm{\phi}} = \argmin_\phi \left( - \sum_{i=1}^I \left( \log(\frac{1}{\sqrt{2 \pi f_2(\bm{x}, \bm{\phi})^2}}) - \frac{(y_i - f_1(\bm{x}, \bm{\phi}))^2}{2 f_2(\bm{x}, \bm{\phi})^2} \right) \right)
$$

## Example 2: Binary Classification

1. Choose Bernoulli distribution, which is defined over the output space $y \in \{0, 1\}$.  The parameter $\lambda$ represents the probability that $y = 1$.


```{=latex}
\[
p(y | \lambda) =
\begin{cases}
1 - \lambda & y = 0,\\
\lambda     & y = 1
\end{cases}
\]
```

Or, equivalently:

$$
p(y | \lambda) = (1 - \lambda)^{1-y} \lambda^y
$$

```{=latex}
\begin{center}
```
![](LossBern.pdf)
```{=latex}
\end{center}
```

## 2: Predicting $\lambda$

2. Set the network  $f(\bm{x}, \bm{\phi})$ to predict the single parameter $\lambda$.  Since $\lambda$ is a probability, but the network can return a number outside $[0, 1]$, we squash the output to the required range using the *logistic sigmoid* function:

$$
sig(z) = \frac{1}{1 + \exp(-z)}
$$

```{=latex}
\begin{center}
```
![](LossLogisticSigmoid.pdf)
```{=latex}
\end{center}
```

## Binary Loss Function and Inference

3. Calculate the negative log-likelihood for our parameter, $\lambda$, to use as the loss function.

The likelihood function is:

$$
p(y | \bm{x}) = (1 - sig(f(\bm{x}, \bm{\phi})))^{1-y} sig(f(\bm{x}, \bm{\phi}))^y
$$

and the negative log-likelihood loss function is:

$$
L(\bm{\phi}) = \sum_{i=1}^I (1-y_i) \log \left( 1 - sig(f(\bm{x}_i, \bm{\phi})) \right) -y_i \log \left( sig(f(\bm{x}_i, \bm{\phi})) \right)
$$

This is known as *binary cross-entropy loss*.  (More on that later ...)

:::: {.columns}
::: {.column width="30%"}


4. Inference is simply:

```{=latex}
\[
\hat{y} =
\begin{cases}
1 & \text{if } \lambda > 0.5,\\
0 & \text{otherwise}
\end{cases}
\]
```

:::
::: {.column width="70%"}

![](LossBinaryClassification.pdf)

:::
::::

## Example 3: Multiclass Classification

1.  We choose a *categorical distribution* with $K$ parameters $\lambda_1, \lambda_2, \dots, \lambda_K$ representing the probability of each of the corresponding $K$ categories $y \in \{1, 2, \dots, K\}$.

$$
p(y = k) = \lambda_k
$$

2. We set the network $f(\bm{x}, \bm{\phi})$ to predict each of the $K$ parameters for a given input $\bm{x}$.  Since the parameters must sum to 1 to be a valid probability distribution and the network can produce arbitrary values, we pass each output through the *softmax* function:

$$
softmax_k(z) = \frac{\exp(z_k)}{\sum_{k'=1}^K \exp(z_{k'})}
$$

```{=latex}
\begin{center}
```
![](LossMultiClassClassification.pdf){height="30%"}
```{=latex}
\end{center}
```

## Multiclass Loss and Inference

3. Calculate the negative log-likelihood for our parameters, $\lambda_k$, to use as the loss function.

The likelihood function is:

$$
p(y = k | \bm{x}) = softmax_k \left( f(\bm{x}, \bm{\phi}) \right)
$$

The negative log-likelihood loss function is:

```{=latex}
\begin{align*}
L(\bm{\phi}) &= - \sum_{i=1}^I \log \left( softmax_{y_i} \left( f(\bm{x}_i, \bm{\phi}) \right) \right)\\
             &= - \sum_{i=1}^I \left( f_{y_i}(\bm{x}_i, \bm{\phi}) - \log \left( \sum_{k'=1}^K \exp( f_{k'}(\bm{x}_i, \bm{\phi}) ) \right) \right)
\end{align*}
```

where $f_{y_i}(\bm{x}_i, \bm{\phi})$ is the $y_i$th output and $f_{k'}(\bm{x}_i, \bm{\phi})$ is the $k'$th output of the network.

4. Inference is simply the most probable category:

$$
\hat{y} = \argmax_k \left( p(y = k | \bm{f} ( \bm{x}, \hat{\bm{\phi}})) \right)
$$
