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



## Time and Uncertainty



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



## Smoothing

```{=latex}
\begin{center}
```
![](aima-fig-14_03-smoothing.pdf)
```{=latex}
\end{center}
```

## Forward-Backward Smoothing Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-14_04-forward-backward-algorithm.pdf)
```{=latex}
\end{center}
```

## Finding the Most Likely Sequence

```{=latex}
\begin{center}
```
![](aima-fig-14_05-rain-state-sequences.pdf)
```{=latex}
\end{center}
```

## Hidden Markov Models (HMMs)

An HMM is a temporal probabilis- tic model in which the state of the process is described by a single, discrete random variable.

## HMM Matrix Formulation

```{=latex}
\[
\bm{T}_{ij} = Pr(X_t = j \mid X_{t-1} = i)
\]
```

```{=latex}
\begin{center}
```
![](aima-fig-14_02-bayes-net-umbrella-world.pdf)
```{=latex}
\end{center}
```


```{=latex}
\[
\bm{T}_{ij} = Pr(X_t \mid X_{t-1}) =
\begin{bmatrix}
0.7 & 0.3 \\
0.3 & 0.7
\end{bmatrix}
\]
```




## Fixed Lag Smoothing Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-14_06-fixed-lag-smoothing-algorithm.pdf)
```{=latex}
\end{center}
```

## Localization with HMMs

```{=latex}
\begin{center}
```
![](aima-fig-14_07-posterior-robot-location.pdf)
```{=latex}
\end{center}
```

## HMM Performance

```{=latex}
\begin{center}
```
![](aima-fig-14_08-hmm-localization-performance-plots.pdf)
```{=latex}
\end{center}
```
