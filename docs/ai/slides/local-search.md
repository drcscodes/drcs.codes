---
title: Artificial Intelligence
subtitle: Local Search
author: Christopher Simpkins
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

## Local Search

- Search neighbors of current state, moving to best neighbor.
- Track only current state.
- Uses very little memory.
- Can find reasonable solutions in large or infinite state spaces.
- Often used for **optmization** problems -- finding states that maximize or minimize an **objective function**.


## State Space Landscape

```{=latex}
\begin{center}
```
![](aima-fig-04_01-state-space-landscape.pdf)
```{=latex}
\end{center}
```

## Hill-Climbing Search

```{=latex}
\begin{center}
```
![](aima-fig-04_02-hill-climbing-algorithm.pdf)
```{=latex}
\end{center}
```

- Also known as **greedy local search**

## Hill-Climbing on 8 Queens Problem

```{=latex}
\begin{center}
```
![](aima-fig-04_03-8-queens.pdf)
```{=latex}
\end{center}
```

## Disadvantages of Hill-Climbing

```{=latex}
\begin{center}
```
![](aima-fig-04_04-ridges.pdf)
```{=latex}
\end{center}
```

Susceptible to getting stuck in:

- local maxima
- ridges -- sequences of local maxima
- plateaus, e.g., flat local maxima or shoulders.

How to fix:

- Allow "sideways" moves
- Stochastic hill climbing chooses randomly from uphill moves.
- Random restart hill climbing restarts from multiple initial states.

## Simulated Annealing

```{=latex}
\begin{center}
```
![](aima-fig-04_05-simulated-annealing-algorithm.pdf)
```{=latex}
\end{center}
```

- Based on annealing in metallurgy -- gradually cooling metals or glass to reach a low-energy crystalline state.
- Think in terms of gradient descent.
- Similar to hill climbing, but picks a random move and

    - accepts it if its better,
    - if not better, accept with probability < 1.

- Probability of accepting a worse move depends on:

    - how much worse the move is, $\Delta E$, and
    - the current "temperature," $T$.

If $T$ decreases sufficiently slowly, then the Boltzman distribution, $e^{\frac{\Delta E}{T}}$, ensures that all the probability is concentrated on the global maxima, so the algorithm finds a global maximum with probability approaching 1.

## Genetic Algorithms

A kind of **local beam search**: tracking $k$ states instead of just one.

```{=latex}
\begin{center}
```
![](aima-fig-04_06-genetic-algorithm-8-queens-illustration.pdf)
```{=latex}
\end{center}
```

## Crossover in the 8-queens Problem

```{=latex}
\begin{center}
```
![](aima-fig-04_07-8-queens-crossover-diagrams.pdf)
```{=latex}
\end{center}
```

## An Example Genetic Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-04_08-genetic-algorithm.pdf)
```{=latex}
\end{center}
```
