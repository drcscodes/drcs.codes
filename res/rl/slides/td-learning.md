---
title: Reinforcement Learning
subtitle: Temporal-Difference Learning (RLbook 6)
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

## TD Prediction

$$
V (S_t) \gets V (S_t) + \alpha \left[ G_t - V(S_t) \right] \tag{6.1}
$$

$$
V (S_t) \gets V (S_t) + \alpha \left[ T_{t+1} + V(S_{t+1}) - \gamma V(S_t) \right]
$$

## Tabular TD(0) Algorithm

```{=latex}
\begin{center}
```
![](rlbook-06-01-tabular-td0-algorithm.pdf)
```{=latex}
\end{center}
```

## TD(0) Backup

```{=latex}
\begin{center}
```
![](rlbook-06-02-td0-backup.pdf)
```{=latex}
\end{center}
```

## Example: Driving Home

```{=latex}
\begin{center}
```
![](rlbook-06-03-fig-06_01-driving-home-mc-vs-td.pdf)
```{=latex}
\end{center}
```

## Example: Random Walk

```{=latex}
\begin{center}
```
![](rlbook-06-04-ex-06_02-mrp.pdf)
```{=latex}
\end{center}
```

## Random Walk State Values

```{=latex}
\begin{center}
```
![](rlbook-06-05-ex-06_02-state-value-plot.pdf)
```{=latex}
\end{center}
```

## Random Walk Error Rates

```{=latex}
\begin{center}
```
![](rlbook-06-06-ex-06_02-episodes-error-plot.pdf)
```{=latex}
\end{center}
```

## TD vs MC Performance

```{=latex}
\begin{center}
```
![](rlbook-06-07-fig-06_02-td-vs-mc-plot.pdf)
```{=latex}
\end{center}
```

## Example: Predicting Returns

Given these 8 episodes:

- $A, 0, B, 0$; $B, 1$; $B, 1$; $B, 1$; $B, 1$; $B, 1$; $B, 1$; $B, 1$;

What are the value estimates for $A$ and $B$?

```{=latex}
\begin{center}
```
![](rlbook-06-08-ex-06_04-markov-process-diagram.pdf)
```{=latex}
\end{center}
```

## Sarsa: On-policy TD Control

```{=latex}
\begin{center}
```
![](rlbook-06-09-episode-state-action-sequence-diagram.pdf)
```{=latex}
\end{center}
```

Sarsa update:

$$
Q(s_t, a_t) \gets Q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(S_t, A_t) \right]
$$

```{=latex}
\begin{center}
```
![](rlbook-06-10-sarsa-backup-diagram.pdf)
```{=latex}
\end{center}
```

## Sarsa Algorithm

```{=latex}
\begin{center}
```
![](rlbook-06-11-sarsa-algorithm.pdf)
```{=latex}
\end{center}
```

## Example: Windy Grid World

```{=latex}
\begin{center}
```
![](rlbook-06-12-ex-06_05-windy-grid-world-plot.pdf)
```{=latex}
\end{center}
```

## Q-Learning: Off-policy TD Control

Sarsa update:

$$
Q(s_t, a_t) \gets Q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(S_t, A_t) \right]
$$

Q-learning update:

$$
Q(s_t, a_t) \gets Q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma \max_{a} Q(s_{t+1}, a) - Q(S_t, A_t) \right]
$$

## Q-Learning Algorithm

```{=latex}
\begin{center}
```
![](rlbook-06-13-q-learning-algorithm.pdf)
```{=latex}
\end{center}
```

## Example: Cliff Walking

```{=latex}
\begin{center}
```
![](rlbook-06-14-ex-06_06-cliff-walking-grid-world.pdf)
```{=latex}
\end{center}
```

## Sarsa vs Q-learning in Cliff Walking

```{=latex}
\begin{center}
```
![](rlbook-06-15-ex-06_06-cliff-walking-sarsa-vs-q-learning-plot.pdf)
```{=latex}
\end{center}
```

## Expected Sarsa

```{=latex}
\begin{align*}
Q(S_t, A_t) &\gets Q(s_t, A_t) + \alpha \left[ R_{t+1} + \gamma \mathbb{E}_{\pi} \left[ Q(S_{t+1}, A_{t+1}) \mid s_{t+1} \right] - Q(S_t, A_t) \right] \\
            &= Q(s_t, A_t) + \alpha \left[ R_{t+1} + \gamma \sum_a \pi (a \mid S_{t+1}) Q(S_{t+1}, a) - Q(S_t, A_t) \right] \tag{6.9}
\end{align*}
```

## Asymptotic Performance of TD Control Methods

```{=latex}
\begin{center}
```
![](rlbook-06-16-fig-06_03-td-control-aymptotic-performance-plots.pdf)
```{=latex}
\end{center}
```

## Q-learning vs Expected Sarsa Backup

```{=latex}
\begin{center}
```
![](rlbook-06-17-fig-06_04-q-learning-backup-diagram.pdf)
```{=latex}
\end{center}
```


```{=latex}
\begin{center}
```
![](rlbook-06-18-fig-06_04-expected-sarsa-backup-diagram.pdf)
```{=latex}
\end{center}
```

## Double Q-learning Performance

```{=latex}
\begin{center}
```
![](rlbook-06-19-fig-06_05-q-learning-vs-double-q-learning-plots.pdf)
```{=latex}
\end{center}
```

## Double Q-learning Algorithm

```{=latex}
\begin{center}
```
![](rlbook-06-20-double-q-learning-algorithm.pdf)
```{=latex}
\end{center}
```

## Games and Afterstates

```{=latex}
\begin{center}
```
![](rlbook-06-21-tic-tac-toe-same-afterposition.pdf)
```{=latex}
\end{center}
```
