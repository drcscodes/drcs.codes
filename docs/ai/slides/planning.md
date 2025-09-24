---
title: Artlificial Intelligence
subtitle: Planning
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

## Classical Planning

Classical planning is defined as the task of finding a sequence of actions to accomplish a
goal in a discrete, deterministic, static, fully observable environment.

PDDL: Planning Domain Definition Language

## PDDL

Action schema
precondition
effect

Action schema:
```{=latex}
\begin{align*}
& Action(Fly(p,from,to),\\
& \hspace{.1in} PRECOND:At(p,from) \land Plane(p) \land Airport(from) \land Airport(to)\\
& \hspace{.1in} EFFECT: \neg At(p,from) \land At(p,to))
\end{align*}
```



Ground (variable-free) action:

```{=latex}
\begin{align*}
& Action(Fly(P_1,SFO,JFK), \\
& \hspace{.1in} PRECOND:At(P_1,SFO) \land Plane(P_1) \land Airport(SFO) \land Airport(JFK) \\
& \hspace{.1in} EFFECT: \neg At(P_1,SFO) \land At(P_1,JFK))
\end{align*}
```

## Air Cargo Transport

```{=latex}
\begin{center}
```
![](aima-fig-11_01-pddl-air-cargo.pdf){height="70%"}
```{=latex}
\end{center}
```

<!--

## Spare Tire

```{=latex}
\begin{center}
```
![](aima-fig-11_02-pddl-spare-tire.pdf){height="70%"}
```{=latex}
\end{center}
```
-->

## Blocks World

```{=latex}
\begin{center}
```
![](aima-fig-11_03-blocks-world-diagram.pdf){height="70%"}
```{=latex}
\end{center}
```

## Blocks World PDDL

```{=latex}
\begin{center}
```
![](aima-fig-11_04-pddl-blocks-world.pdf){height="70%"}
```{=latex}
\end{center}
```

## Classical Planning Algorithms

- Forward state space search
- Backward state space search
- SATPlan
- Graphplan
- Situation calculus
- Constraint satisfaction
- Partial-order planning

## Forward and Backward State Space Planning

```{=latex}
\begin{center}
```
![](aima-fig-11_05-forward-backward-search.pdf){height="70%"}
```{=latex}
\end{center}
```

## Heuristics for Planning

```{=latex}
\begin{center}
```
![](aima-fig-11_06-ignore-delete-state-spaces.pdf){height="70%"}
```{=latex}
\end{center}
```

## Hierarchical Planning

:::: {.columns}
::: {.column width="50%"}

Hierarchical task network plans are built from:

- primitive actions, and
- high-level actions (HLA).

HLAs have one or more **refinements**.

- Refinements may contain other HLAs.
- A refinement with only primitive actions is an **implementation**.
- An HLA achieves a goal if at least one of its implementations achieves the goal.


:::
::: {.column width="50%"}

Here are two goal-achieving implementations for the $Go(Home, SFO)$ HLA:

```{=latex}
\begin{center}
\vspace{.05in}
```
![](aima-fig-11_07-a-go-home-refinements.pdf){height="20%"}
```{=latex}
\end{center}
```


Refinements can be produced recursivley, as shown in this vacuum world navigation example:

```{=latex}
\begin{center}
\vspace{.05in}
```
![](aima-fig-11_07-b-vacuum-navigation-recursion.pdf){height="40%"}
```{=latex}
\end{center}
```

:::
::::

## Hierarchical Forward Planning Search

A breadth-first implementation of hierarchical forward planning search. The initial plan supplied to the algorithm is *[Act]*. The REFINEMENTS function returns a set of action sequences, one for each refinement of the HLA whose preconditions are satisfied by the specified state, *outcome*.

```{=latex}
\begin{center}
```
![](aima-fig-11_08-hierarchical-search-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Reachable Sets

```{=latex}
\begin{center}
```
![](aima-fig-11_09-schematic-reachable-sets.pdf){height="70%"}
```{=latex}
\end{center}
```

## Goal Acievement

```{=latex}
\begin{center}
```
![](aima-fig-11_10-goal-achievement.pdf){height="70%"}
```{=latex}
\end{center}
```

## Angelic Search

```{=latex}
\begin{center}
```
![](aima-fig-11_11-angelic-search-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Online Planning

```{=latex}
\begin{center}
```
![](aima-fig-11_12-action-monitoring.pdf){height="70%"}
```{=latex}
\end{center}
```

## Resource Constraints

```{=latex}
\begin{center}
```
![](aima-fig-11_13-pddl-job-shop-scheduling.pdf){height="70%"}
```{=latex}
\end{center}
```

## Temporal Constraints

```{=latex}
\begin{center}
```
![](aima-fig-11_14-temporal-constraints-job-shop-scheduling.pdf){height="70%"}
```{=latex}
\end{center}
```

## Job-Schop Scheduling Solutions

```{=latex}
\begin{center}
```
![](aima-fig-11_15-solution-job-shop-scheduling.pdf){height="70%"}
```{=latex}
\end{center}
```
