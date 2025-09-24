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

Classical planning is the task of finding a sequence of actions to accomplish a goal in a discrete, deterministic, static, fully observable environment.  Two previous approaches:

- Graph search, e.g., $A^*$
- Hybrid propositional logical agent

Two limitations:

- Require ad-hoc heuristics
- Require explicit representation of exponentially large state space.

Planning Domain Definition Language solves these problems using a factored representation based on first-order logic.

- A **state** is a conjunction of ground atomic fluents -- single predicates containing no variables.

    - $At(Truck_1,Melbourne)$ is a ground atomic fluent, $At(t_1, from)$ is not.

- PDDL uses **database semantics**, or the **closed-world assumption**: any fluents not mentioned are false, and unique names represent distinct objects.


## Planning Domain Definition Language (PDDL)

Action schema is a family of ground actions.

- Action name and list of variables
- Precondition: conjunction of literals

    - Action $a$ is **applicable** in state $s$ if $s \models a.precondition$

- Effect: conjunction of literals

    - **Result** of executing action $a$ in state $s$ is $s'$ is applying delete list and add list to $s$:

        - $DEL(a)$, delete list: remove negative literals in action's effects.
        - $ADD(a)$, add list: add positive literals in action's effects.


Action schema:
```{=latex}
\vspace{-.25in}
\begin{align*}
& Action(Fly(p,from,to),\\
& \hspace{.1in} PRECOND:At(p,from) \land Plane(p) \land Airport(from) \land Airport(to)\\
& \hspace{.1in} EFFECT: \neg At(p,from) \land At(p,to))
\end{align*}
\vspace{-.25in}
```

Ground (variable-free) action:

```{=latex}
\vspace{-.25in}
\begin{align*}
& Action(Fly(P_1,SFO,JFK), \\
& \hspace{.1in} PRECOND:At(P_1,SFO) \land Plane(P_1) \land Airport(SFO) \land Airport(JFK) \\
& \hspace{.1in} EFFECT: \neg At(P_1,SFO) \land At(P_1,JFK))
\end{align*}
\vspace{-.25in}
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
- SATPlan -- boolean satisfiability planning

    - Translate PDDL into propositional form, use a SAT solver

- Graphplan

    - Encode constraints related to preconditions and effects in a **planning graph**.

- Situation calculus
- Constraint satisfaction
- Partial-order planning

    - $Remove(Spare,Trunk)$ and $Remove(Flat,Axle)$ must come before $PutOn(Spare,Axle)$, but removals can happen in any order.


## Forward and Backward State Space Planning

- Forward search: unify current state against preconditions of each action schema -- **applicable** actions.

- Backward search: unify goal states against effects of action schemas -- **relevant** actions.

```{=latex}
\begin{center}
```
![](aima-fig-11_05-forward-backward-search.pdf){height="60%"}
```{=latex}
\end{center}
```

<!--

## Heuristics for Planning

```{=latex}
\begin{center}
```
![](aima-fig-11_06-ignore-delete-state-spaces.pdf){height="70%"}
```{=latex}
\end{center}
```

-->

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

<!--

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

-->

## Closing Thoughts

- Fun to create toy worlds and solve them.

    - Look up "Monkey and bananas" problem.

- Still have knowledge-acquisition bottleneck.
- Still have problem of specifying large number of rules and facts for non-trivial problems.
- Still have problem of uncertainty -- nondeterministic actions and partial observability.

In rest of course, we address these issues with uncertain reasoning and machine learning.
