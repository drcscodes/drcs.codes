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

If you don't care about the path to a goal state, you can use **local search**.

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

## The 8 Queens Problem

**Complete-state formulation**: row position for each of 8 columns, e.g., (a) below is `<1, 6, 2, 5, 7, 4, 8, 3>`

```{=latex}
\begin{center}
```
![](aima-fig-04_03-8-queens.pdf){height="50%"}
```{=latex}
\end{center}
```

- Action: move a single queen to new row within column.  Each state has $8 \dot 7 = 56$ successor states.
- Possible heuristic: number of pairs of attacking queens (even if blocked).  (b) above has $h = 17$.

    - Useful to remember: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$


## Disadvantages of Hill-Climbing

:::: {.columns}
::: {.column width="60%"}
Susceptible to getting stuck in:

- local maxima
- ridges -- sequences of local maxima
- plateaus, e.g., flat local maxima or shoulders.

![](aima-fig-04_01-state-space-landscape.pdf){height="30$"}

How to fix:

- Allow "sideways" moves
- Stochastic hill climbing chooses randomly from uphill moves.
- Random restart hill climbing restarts from multiple initial states.

:::
::: {.column width="40%"}

Grid of states superimposed on ridge rising from left to right.

```{=latex}
\begin{center}
```
![](aima-fig-04_04-ridges.pdf)
```{=latex}
\end{center}
```

:::
::::

## Simulated Annealing

```{=latex}
\begin{center}
```
![](aima-fig-04_05-simulated-annealing-algorithm.pdf){height="30%"}
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

Elements of genetic algorithms:

- Fitness function.
- Population size.
- Candidate representation:

    - Typically a string (vector) over a finite alphabet.
    - **Evolution strategies**: sequence of real numbers.
    - **Genetic programming**: computer programs.

- Mixing number, $\rho$: number of "parents" from which to generate new candidates.  When $\rho = 1$, stochastic beam search.
- Selection process for choosing "parents."
- Recombination procedure.
- Mutation rate.
- Composition of next generation.

    - Elitism: choose top-scoring candidates.
    - Culling: eliminate bottom-scoring candidates.


## A Genetic Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-04_08-genetic-algorithm.pdf)
```{=latex}
\end{center}
```

## Genetic Algorithm on 8-Queens Problem

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
