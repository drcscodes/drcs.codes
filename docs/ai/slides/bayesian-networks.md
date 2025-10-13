---
title: Artificial Intelligence
subtitle: Bayesian Networks
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

## Representation of Uncertain Knowledge

AIMA

## Bayesian Network Topology

```{=latex}
\begin{center}
```
![](aima-fig-13_01-bayes-net-weather-cavity.pdf)
```{=latex}
\end{center}
```

## Conditional Probability Tables

The *syntax* of a Bayes net consists of a directed acyclic graph (DAG) with some local probability information attached to each node.

```{=latex}
\begin{center}
```
![](aima-fig-13_02-bayes-net-alarm.pdf)
```{=latex}
\end{center}
```

## Semantics of Bayesian Networks

The *semantics* defines how the syntax -- a DAG with local probabilities -- corresponds to a joint distribution over the variables of the network.

A Bayes net contains:

- $n$ variables, $X_1, \dots , X_n$, and
- (implicit) joint distributions $Pr(X_1 = x_1 \land \dots \land X_n = x_n)$, or $Pr(x_1, \dots, x_n)$.

Each entry in the joint distribution is defined by:

$$
Pr(x_1, \dots, x_n) = \prod_{i=1}^n \theta ( x_i | parents(X_i))
$$

where $parents(X_i)$ denotes the values of $Parents(X_i)$ that appear in $x_1, dots, x_n$.  So each entry in the joint distribution is the rpoduct of appropirate elements of the local CPTs in the Bayes net.


## Constructing Bayesian Networks

First, meet conditions:

TODO: conditions


1. Nodes: First determine the set of variables that are required to model the domain. Now order them, $\{X_1, \dots ,X_n\}$. Any order will work, but the resulting network will be more compact if the variables are ordered such that causes precede effects.

2. Links: For $i = 1$ to $n$ do:

- Choose a minimal set of parents for $X_i$ from $X_1, \dots ,X_{i-1}$, such that Equation (13.3) is satisfied.
- For each parent insert a link from the parent to $X_i$.
- CPTs: Write down the conditional probability table, $P(X_i|Parents(X_i))$.

## Effects of Node Ordering

```{=latex}
\begin{center}
```
![](aima-fig-13_03-bayes-net-structures.pdf)
```{=latex}
\end{center}
```

## Conditional Independence Relations

```{=latex}
\begin{center}
```
![](aima-fig-13_04-markov-blankets.pdf)
```{=latex}
\end{center}
```

## CPTs Under Noisy-or Model

```{=latex}
\begin{center}
```
![](aima-fig-13_05-prob-table-fever.pdf)
```{=latex}
\end{center}
```

## Bybrid Bayesian Networks

Bayesian Networks with Discrete and Continuous Variables

```{=latex}
\begin{center}
```
![](aima-fig-13_06-bayes-net-discrete-continuous.pdf)
```{=latex}
\end{center}
```

## Linear-Gaussian Conditional Distributions

```{=latex}
\begin{center}
```
![](aima-fig-13_07-cost-prob-dist.pdf)
```{=latex}
\end{center}
```

## Soft Thresholding for Continuous Parents

```{=latex}
\begin{center}
```
![](aima-fig-13_08-cost-gaussian-expit-probit-dists.pdf)
```{=latex}
\end{center}
```

## Case Study: Car Insurance

```{=latex}
\begin{center}
```
![](aima-fig-13_09-bayes-net-car-insurance.pdf)
```{=latex}
\end{center}
```
