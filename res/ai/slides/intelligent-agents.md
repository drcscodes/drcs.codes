---
title: Intelligent Agents
author: Artificial Intelligence
institute: Christopher Simpkins
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

## Agents

```{=latex}
\begin{center}
```
![](aima-fig-02_01-agent-environment.pdf)
```{=latex}
\end{center}
```

## Agent Functions

An *agent function* is an external tabulation of the agent's behavior.

```{=latex}
\begin{center}
```
![](aima-fig-02_02-vacuum-world.pdf){height="15%"}
![](aima-fig-02_03-vacuum-function.pdf){height="75%"}
```{=latex}
\end{center}
```

An *agent program* is an implementation of an agent function inside the agent.

## Intelligent Agents Rationality

- Consequentialist: we judge behavior as rational if it leads to desirable consequences.
- Need an external *performance measure* to make this judgment.
- Genie effect: be careful what you wish for.

Example: what if our performance measure is "amount of dirt sucked up?"

> Performance measures should specify desired states of the environment, not preconceived notions of what the agent's behavior should be.

## Rationality

Judgment of rationality depends on:

- The performance measure that defines the criterion of success.
- The agent’s prior knowledge of the environment.
- The actions that the agent can perform.
- The agent’s percept sequence to date.

Definition of rational agent:

> For each possible percept sequence, a rational agent should select an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.

Note that the performance measure is external to the agent, representing a general notion of "success" within an environment that applies to any agent in the environment.

## Omniscience, Rationality, Learning and Autonomy

- Omniscience: for a given state and action, agent knows the result state exactly.
- Omniscience is impossible in practice

> Rationality means choosing the best action given what you know, i.e., the percept sequence to date.

Key idea: how to maximize the usefulness of the agent's percept sequence.

- Information gathering, exploration.
- Learning
- Prior knowledge

The more an agent is able to learn, the more autonomy it has.

## Task Environments

The concept of an environment is both general and limited.  In AI we are usually interested in a particular task within an environment.  We call these *task environments* and they represent the "problems" that an intelligent agent "solves."

Task environment specification: PEAS

- **P**erformance measure
- **E**nvironment dynamics -- what is the result of applying an action
- **A**ctuators to modify the environment
- **S**ensors to perceive the environment


## Taxi Task Environment

```{=latex}
\begin{center}
```
![](aima-fig-02_04-taxi-task-environment.pdf)
```{=latex}
\end{center}
```


## Example Agent Types and Their PEAS Descriptions

```{=latex}
\begin{center}
```
![](aima-fig-02_05-agent-types.pdf){height="90%"}
```{=latex}
\end{center}
```


## Task Environment Design Space

- Fully vs. partially observable
- Single agent vs. multi-agent
  - Competitive vs. cooperative
- Deterministic vs. nondeterministic
  - Stochastic is a specific kind of nondeterminism in which we assign probabilities to outcomes
- Episodic vs. sequential
  - Episodic: current action independent of previous decisions and future decisions
  - Sequential: current action may affect all future actions
- Static vs. dynamic
  Can the environment change while agent is deliberating?
- Discrete vs. continuous
- Known vs. unknown
  - Does the agent know the "physics" of the environment?

## Task Environment Examples

```{=latex}
\begin{center}
```
![](aima-fig-02_06-example-tasks.pdf){height="90%"}
```{=latex}
\end{center}
```

## The Structure of Agents

- An *agent program* is an implementation of an agent function inside the agent.
- An *agent architecture* is the computing device on which the agent runs, including sensors and actuators (which may be virtual).
  - When we put an agent program inside a physical platform, like a robot, we call it *embodied intelligence*.

$$
agent = architecture + program
$$

## Table-driven Agent

A table-driven agent program implements the agent function directly.

```{=latex}
\begin{center}
```
![](aima-fig-02_07-table-driven-agent-program.pdf)
```{=latex}
\end{center}
```

If $\mathcal{P}$ is the set of possible percepts and $T$ is the lifetime of the agent, then the size of the agent table is impossibly large in practice:

```{=latex}
\vspace{-.2in}
$$
\sum_{t=1}^T |\mathcal{P}|^t
$$
```

> Key idea: a full representation of the ideal agent program is usually impossible in practice.  Our job as AI agent developers is to design a compact representation of the ideal agent program.

## Reflex Vacuum Agent

```{=latex}
\begin{center}
```
![](aima-fig-02_02-vacuum-world.pdf)

![](aima-fig-02_08-reflex-vacuum-agent-program.pdf)
```{=latex}
\end{center}
```

## General Reflex Agents

```{=latex}
\begin{flushleft}
```
![](aima-fig-02_10-reflex-agent-program.pdf)
```{=latex}
\end{flushleft}
```

```{=latex}
\vspace{-.2in}
\begin{flushright}
```
![](aima-fig-02_09-reflex-agent-diagram.pdf){height="50%"}
```{=latex}
\end{flushright}
```

## Condition-Action Rules

Condition-action rules (a.k.a. productions or situation-action rules or simply if-then rules) take the form

- **if** *condition* **then** *action*

> Simple reflex agents work only if the correct decision can be made on the basis of just the current percept—that is, only if the environment is fully observable.

Consider the effect of partial observability?

- What if our reflex vacuum agent has a dirt sensor but no location sensor?
- How can randomization help?


## Model-based Agents


An agent can keep track of its state by maintaining a *model* of the environment.  An environment model typically consists of

- a sensor model, which maps percepts to states, and
- a state transition model.

A transition model typically contains

- A set of states, $S$,
- A set of actions the agent can execute in the environment, $A$, and
- A state transition function, $T(s, a, s')$

Note that the state transition function can be deterministic or nondeterministic.  In most of AI, we consider it to be stochastic.

$$
Pr(s, a, s') \text{ or } Pr(s_t | s_{t-1}, a_{t-1})
$$


## Model-based Reflex Agents

```{=latex}
\begin{flushleft}
```
![](aima-fig-02_12-model-based-reflex-agent-program.pdf){height="50%"}
```{=latex}
\end{flushleft}
```

```{=latex}
\vspace{-.3in}
\begin{flushright}
```
![](aima-fig-02_11-model-based-reflex-agent-diagram.pdf){height="45%"}
```{=latex}
\end{flushright}
```

## Model-based Goal-driven Agents

```{=latex}
\begin{center}
```
![](aima-fig-02_13-model-based-goal-driven-agent-diagram.pdf)
```{=latex}
\end{center}
```

Agents select actions that achieve goals by using **search** and **planning** algorithms, which we'll start learning next lecture.

## Model-based Utility-driven Agents

```{=latex}
\begin{center}
```
![](aima-fig-02_14-model-based-utility-driven-agent-diagram.pdf)
```{=latex}
\end{center}
```

## Learning Agents

```{=latex}
\begin{center}
```
![](aima-fig-02_15-learning-agent-diagram.pdf)
```{=latex}
\end{center}
```

## State Representations

```{=latex}
\begin{center}
```
![](aima-fig-02_16-state-representations.pdf)
```{=latex}
\end{center}
```

- Atomic representations are typically used in search-based problem solving.
- Factored representations are used in constraint satisfaction, propositional logic, planning, most probabilistic models (e.g., Bayesian networks), and many machine learning algorithms.
- Structured representations are used in relational databases, first order logic, first-order probability models, and natural language processing.

## Closing Thoughts

This chapter has effectively introduced the entire course, providing a framework for everything else we will learn.
