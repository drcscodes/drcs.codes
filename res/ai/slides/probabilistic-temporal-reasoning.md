---
title: Artificial Intelligence
subtitle: Probabilistic Temporal Reasoning
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

## Probabilistic Temporal Reasoning


## First- and Second-Order Markov Processes

```{=latex}
\begin{center}
```
![](aima-fig-14_01-bayes-net-markov-processes.pdf)
```{=latex}
\end{center}
```

## Umbrella World

```{=latex}
\begin{center}
```
![](aima-fig-14_02-bayes-net-umbrella-world.pdf)
```{=latex}
\end{center}
```

## Inference in Temporal Models

- **Filtering**, a.k.a., **state estimation** is
- **Prediction**:
- **Smoothing**:
- **Most likely explanation**:

## Learning Temporal Models

Unknown transition and sensor models can be learned from observations.

- As with static Bayesian networks, dynamic Bayes net learning can be done as a by-product of inference.

- Inference provides an estimate of transitions that actually occurred and the states that generated the sensor readings, and these estimates can be used to learn the models.

- Learning via iterative update algorithm, expectation–maximization or EM, or Bayesian updating of the model parameters given the evidence.

We'll return to these ideas in our lesson on [statistical learning](statistical-learning.pdf).

## Filtering and Prediction



## Probabilistic Temporal Reasoning

```{=latex}
\begin{center}
```
![](aima-fig-14_03-smoothing.pdf)
```{=latex}
\end{center}
```

## Probabilistic Temporal Reasoning

```{=latex}
\begin{center}
```
![](aima-fig-14_)
```{=latex}
\end{center}
```

## Probabilistic Temporal Reasoning

```{=latex}
\begin{center}
```
![](aima-fig-14_)
```{=latex}
\end{center}
```

## Probabilistic Temporal Reasoning

```{=latex}
\begin{center}
```
![](aima-fig-14_)
```{=latex}
\end{center}
```

## Probabilistic Temporal Reasoning

```{=latex}
\begin{center}
```
![](aima-fig-14_)
```{=latex}
\end{center}
```

## Probabilistic Temporal Reasoning

```{=latex}
\begin{center}
```
![](aima-fig-14_)
```{=latex}
\end{center}
```
