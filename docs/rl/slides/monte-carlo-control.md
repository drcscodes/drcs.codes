---
title: Reinforcement Learning
subtitle: Monte Carlo Control (RLAI 5)
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

## Monte Carlo Control

Monte Carlo methods are ways of solving the reinforcement learning problem based on averaging sample returns.

- Monte carlo prediction of $v_{\pi}$ and $q_{\pi}$ values
- Policy improvement via monte carlo estimation of action values
- Monte carlo control via approximate policy and action-value functions



## First Visit Monte Carlo Prediction of State Values

```{=latex}
\begin{center}
```
![](rlbook-05-01-first-visit-mc-prediction-algorithm.pdf)
```{=latex}
\end{center}
```

## Example: Blackjack

```{=late x }
\begin{cards}
\crdpair{\crdKs}{\crdtenh}%
\end{cards}
```

## Monte Carlo Prediction of Action Values

Foo

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-02-fig-05_01-blackjack-state-value-functions.pdf)
```{=latex}
\end{center}
```

## Value Backups

:::: {.columns}
::: {.column width="60%"}

In dynamic programming MDP solution, values are backed up from each possible successor states:

$$
v_{\pi} = \sum_a \pi (a \mid s) \sum_{s',r} p(s', r \mid s, a) \left[ r + \gamma v_{\pi} (s') \right]
$$



:::
::: {.column width="45%"}

```{=latex}
\begin{center}
```
![](rlbook-03-05-one-step-all-successors-backup.pdf)
```{=latex}
\end{center}
```

DP one-step, all successors value backup

```{=latex}
\begin{center}
```
![](rlbook-05-03-monte-carlo-full-trajectory-backup.pdf)
```{=latex}
\end{center}
```

MC full single trajectory backup

:::
::::

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-04-ex05_02-soap-bubble.pdf)
```{=latex}
\end{center}
```

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-05-evaluation-improvement-loop.pdf)
```{=latex}
\end{center}
```

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-06-monte-carlo-es-algorithm.pdf)
```{=latex}
\end{center}
```

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-07-fig-05_02-blackjack-monte-carlo-es.pdf)
```{=latex}
\end{center}
```

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-08-on-policy-first-visit-mc-control-algorithm.pdf)
```{=latex}
\end{center}
```

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-09-fig-05_03-importance-sampling-plots.pdf)
```{=latex}
\end{center}
```

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-10-fig-05_04-unstable-importance-sampling-off-policy-first-visit-mc.pdf)
```{=latex}
\end{center}
```

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-11-off-policy-mc-prediction-algorithm.pdf)
```{=latex}
\end{center}
```

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-12-off-policy-mc-control-algorithm.pdf)
```{=latex}
\end{center}
```

## Monte Carlo Control

```{=latex}
\begin{center}
```
![](rlbook-05-13-fig-05_05-racetrack-right-turns.pdf)
```{=latex}
\end{center}
```
