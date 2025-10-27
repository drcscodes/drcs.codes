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

- Action: move a single queen to new row within column.  Each state has $8 \cdot 7 = 56$ successor states.
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
- Stochastic hill climbing chooses randomly from uphill moves. Stochastic beam search does this with $k$ states in parallel.
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

- Based on metallurgy -- gradually cool metal to reach low-energy crystalline state.
- Intuition: think of gradient descent instead of gradient ascent -- multiple shallow valleys, one deepest valley.  Shake ball out of shallow valleys into deepest valley.
- Similar to hill climbing, but picks a random move and

    - accepts it if its better,
    - if not better, accept with probability < 1.

- Probability of accepting a worse move depends on:

    - how much worse the move is, $\Delta E$, and
    - the current "temperature," $T$.

If $T$ decreases sufficiently slowly, then the Boltzman distribution, $e^{\frac{\Delta E}{T}}$, ensures that all the probability is concentrated on the global maxima, so the algorithm finds a global maximum with probability approaching 1.

## Evolutionary (Genetic) Algorithms

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

1. Population is generated in (a).
2. Fitness function is applied to population, which is then ranked by fitness score.
3. Highest-scoring candidates are selected for reproduction in (c).
4. Crossover operation is applied to candidates in (c) to produce "children" in (d).
5. In (e) "offspring" are randomly chosen for mutation.  For each chosen candidate, a "gene" is randomly chosen, then that gene is assigned a random "mutated" value.

## Crossover in the 8-queens Problem

Here is a pictorial illustration of the crossover operation in the 8-queens problem:

```{=latex}
\begin{center}
```
![](aima-fig-04_07-8-queens-crossover-diagrams.pdf)
```{=latex}
\end{center}
```

Is the random crossover operation depicted here meaningful for the 8-queens problem?

## Genetic Algorithms and Biological Evolution

Genetic algorithms borrow the language of biological evolution for marketing purposes, but are far more simplistic than biological evolution.  My takes:

- Genetic algorithms are just stochastic beam search with "sexual" successor generation and "mutation."
- If there is no meaningful crossover operation, genetic algorithms are just random walks in the state space graph.

There is an interesting connection between biological evolution and AI, in particular learning.

- Learning is adaptation. With experience an agent adapts to a task, getting better at the task.
- Biological evolution can be seen as a learning process whereby specieses "learn" to perform better in their environments.
- The Baldwin effect: immutable traits vs. online learning ability.

    - Plasticity, or the ability to learn, allows a species to adapt to an environment for which it is ill-suited.  E.g., building shelters, fire, etc. in cold regions.
    - Things that are harder, or impossible, to learn online must be encoded in the genome.  E.g., the way our body uses the air it breathes or the sun.

## Continuous State Spaces -- Airports In Romania


:::: {.columns}
::: {.column width="60%"}

```{=latex}
\begin{center}
```
![](aima-romania-airports.png){height="80%"}
```{=latex}
\end{center}
```

:::
::: {.column width="40%"}

If each airport $\bm{x}_i$ is at location $(x_i, y_i)$ and the set of cities closest to airport $\bm{x}_i$ is $C_i$, then

$$
f(\bm{x}) = f(x_1, y_1, x_2, y_2, x_3, y_3)
$$

and we want to minimize

$$
f(\bm{x}) = \sum_{i=1}^3 \sum_{c \in C_i} (x_i - x_c)^2 + (y_i - y_c)^2
$$

For a globally optimal solution, if the airports move "too much," the sets $C_i$ change.  How to deal with that?

:::
::::

## Local Gradient Descent

The gradient of

$$
f(\bm{x}) = \sum_{i=1}^3 \sum_{c \in C_i} (x_i - x_c)^2 + (y_i - y_c)^2
$$

is

$$
\nabla f = \left( \frac{\partial f}{\partial x_1},
                  \frac{\partial f}{\partial y_1},
                  \frac{\partial f}{\partial x_2},
                  \frac{\partial f}{\partial y_2},
                  \frac{\partial f}{\partial x_3},
                  \frac{\partial f}{\partial y_3} \right)
$$

But that would only work for one airport.  We can decompose it into three local problems:

:::: {.columns}
::: {.column width="33%"}

$$
\frac{\partial f}{\partial x_1} = 2 \sum_{c \in C_1} (x_1 - x_c)
$$
$$
\frac{\partial f}{\partial y_1} = 2 \sum_{c \in C_1} (y_1 - y_c)
$$

:::
::: {.column width="33%"}

$$
\frac{\partial f}{\partial x_2} = 2 \sum_{c \in C_2} (x_2 - x_c)
$$
$$
\frac{\partial f}{\partial y_2} = 2 \sum_{c \in C_2} (y_2 - y_c)
$$

:::
::: {.column width="33%"}

$$
\frac{\partial f}{\partial x_3} = 2 \sum_{c \in C_3} (x_3 - x_c)
$$
$$
\frac{\partial f}{\partial y_3} = 2 \sum_{c \in C_3} (y_3 - y_c)
$$

:::
::::

## Gradient Descent in Action

:::: {.columns}
::: {.column width="40%"}

Given our 3 gradient expressions, we can use the update rule:

$$
\bm{x} \leftarrow \bm{x} + \alpha \nabla f(\bm{x})
$$

where $\alpha$ is a **step size**, or learning rate.

- What if $\alpha$ is "too big?"

- What if $\alpha$ is "too small?"

:::
::: {.column width="60%"}

```{=latex}
\begin{center}
```
![](../../deep-learning/slides/TrainLRMin.pdf){height="80%"}[^UDLBook]
```{=latex}
\end{center}
```

:::
::::

[^UDLBook]: https://udlbook.github.io/udlbook/

## Continuous State Spaces and Convexity

A convex set is a set of points in which a line between any two points lies within the set.  A convex function is a function for which the points above the function form a convex set.

```{=latex}
\begin{center}
```
![](../../deep-learning/slides/TrainConvexProb.pdf)[^UDLBook]
```{=latex}
\end{center}
```

There are mathematical properties of continuous spaces that rule out local minima.  Take my deep learning class to learn about them!

[^UDLBook]: https://udlbook.github.io/udlbook/

## Constrained Optimization via Linear Programming

:::: {.columns}
::: {.column width="30%"}

```{=latex}
\begin{align*}
\text{maximize }    3x_1 + 2x_2  \\
\text{subject to }  -x_1 + 3x_2 &\le  12 \\
                    x_1 + x_2   &\le  8 \\
                    2x_1 - x_2  &\le  10 \\
                    x_1, x_2    &\ge  0
\end{align*}
```

:::
::: {.column width="70%"}

```{=latex}
\begin{center}
```
![](lp-fig-02_01-half-planes.pdf){height="70%"}[^LPBook]
```{=latex}
\end{center}
```

:::
::::

[^LPBook]: https://vanderbei.princeton.edu/LPbook/
