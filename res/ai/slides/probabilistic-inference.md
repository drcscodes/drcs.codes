---
title: Artificial Intelligence
subtitle: Probabilistic Inference
author: Christopher Simpkins
institute: Kennesaw State University
aspectratio: 1610
fontsize: 10pt
colorlinks: yes
urlcolor: blue
header-includes:
- |
    ```{=latex}
    \input{beamer-common}
    ```
---

## Exact Inference in Bayesian Networks

Most common task in probabilistic inference: compute the *posterior probability* of a set of **query variables** given some **event** represented as a set of **evidence variables**.

Notation:

- Query variable: $X$
- Set of evidence variables: $\bm{E} = \{E_1, \dots, \E_m$
- Particular observed event: $\bm{e}$
- Hidden (nonevidence, nonquery variables) $\bm{Y} = \{Y_1, \dots, Y_l\}$
- Typical query: $Pr(X \mid e)$

Example:

$$
Pr(Buglary \mid JohnCalls = true, MaryCalls = true) = <0.284, 0.716>.
$$

- $X$ is the boolean random variable $Burglary$
- $\bm{E} = \{JohnCalls, MaryCalls\}$
- $\bm{e} = \{JohnCalls = true, MaryCalls = true\}$
- $\bm{Y} = \{EarthQuake, Alarm\}$


## Inference by Enumeration



## Enumeration Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-13_11-bayes-net-enumeration-algorithm.pdf)
```{=latex}
\end{center}
```

## Repeated Calculations

```{=latex}
\begin{center}
```
![](aima-fig-13_10-prob-expression-tree.pdf)
```{=latex}
\end{center}
```

## Pointwise Products

```{=latex}
\begin{center}
```
![](aima-fig-13_12-pointwise-multiplication.pdf)
```{=latex}
\end{center}
```

## Variable Elimination Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-13_13-bayes-net-variable-elimination-algorithm.pdf)
```{=latex}
\end{center}
```

## Complexity of Exact Inference

```{=latex}
\begin{center}
```
![](aima-fig-13_14-bayes-net-3cnf.pdf)
```{=latex}
\end{center}
```

## Clustering Algorithms

aka joint trees.

```{=latex}
\begin{center}
```
![](aima-fig-13_15-lawn-routine-clustered-bayes-net.pdf)
```{=latex}
\end{center}
```

## Direct Sampling Methods



## Prior Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_16-bayes-net-prior-sample-algorithm.pdf)
```{=latex}
\end{center}
```

## Rejection Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_17-bayes-net-rejection-sampling-algorithm.pdf)
```{=latex}
\end{center}
```

## Importance Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_18-bayes-net-likelihood-weighting-algorithm.pdf)
```{=latex}
\end{center}
```

## Rejection vs. Importance Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_19-performance-plot-rejection-sampling-likelihood-weighting.pdf)
```{=latex}
\end{center}
```

## Markov Chain Monte Carlo (MCMC) Algorithms

Instead of generating each sample from scratch, MCMC algorithms generate a sample by making a random change to the preceding sample. Think of an MCMC algorithm as being in a particular current state that specifies a value for every variable and generating a next state by making random changes to the current state.

## Gibbs Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_20-bayes-net-gibbs-sampling-algorithm.pdf)
```{=latex}
\end{center}
```

## Markov Chains

```{=latex}
\begin{center}
```
![](aima-fig-13_21-markov-chain.pdf)
```{=latex}
\end{center}
```

## Gibbs Sampling vs. Importance Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_22-performance-plots-gibbs-sampling-likelihood-weighting.pdf)
```{=latex}
\end{center}
```
