---
title: Artificial Intelligence
subtitle: Markov Decision Processes (AIMA 17)
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

## Sequential Decisions


In **sequential decision problems**, the agent's utility depends on a sequence of decisions.

Sequential decision problems incorporate utilities, uncertainty, and sensing, and include search and planning problems as special cases.

- Markov decision processes (MDPs)
- $k$-Armed bandits
- Partially observable MPDs (POMDPs)

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_01-4x3-grid-world-stochastic-actions.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes (MDPs)

A Markov decision process (MDP) is a 4-tuple $\left( S, A, T(s, a, s'), R(s) \right)$, where

- $S$ is a set of states,
- $A$, or $Action(s)$ is a set of actions, and
- $T(s, a, s')$, or $Pr(s' \mid s, a)$, is a transition function which gives the probability that executing action $a$ in state $s$ will result in $s'$.
- $R(s)$ is the reward the world provides to an agent for arriving in state $s$

Some definitions of MDPs include an initialization function, $I(s)$, which specifies the probability the the agent will start in some state $s \in S$, others specify a particular state from $S$ as the start state.


## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_02_a-optimal-policies.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_02_b-optimal-policies-different-rewards.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_03-state-values.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_04-decision-network-robot-mdp.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_05_a-tetris.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_05_b-decision-network-tetris-mdp.pdf)
```{=latex}
\end{center}
```

## Bellman Optimality Equation

```{=latex}
\begin{equation}\label{eqn:bellman-equation}
V(s) = R(s) + \max_{a \in A} \sum_{s'} T(s, a, s') V(s')
\end{equation}
```

This equation is called the Bellman optimality equation \cite{bellman1957dynamic,bertsekas2012dynamic}. There is one Bellman equation for each state -- $n$ equations in $n$ unknowns (the values) for a state space of size $n$. However, since the $max$ operator is nonlinear we cannot solve the system of simultaneous Bellman equations using linear algebra. One solution is to use an iterative dynamic programming approach: value iteration.

## Bellman Value Update Rule

The value iteration algorithm initializes each state's value to a random value, then iteratively update these values by turning the Bellman equation into an update rule (the Bellman update):

```{=latex}
\begin{equation}\label{eqn:bellman-update}
V_{i+1}(s) \leftarrow R(s) + \max_{a \in A} \sum_{s'} T(s, a, s') V_i(s')
\end{equation}
```

These updates are applied at the same time for all states, i.e., the values in iteration $i+1$ are calculated from the values in iteration $i$. The value iteration algorithm is shown in Algorithm \ref{alg:value-iteration}.

```{=latex}
\begin{algorithm}[H]
  \caption{Value Iteration}\label{alg:value-iteration}
  \begin{algorithmic}
    \State $V \gets$ random initial values
    \Repeat
      \State $V' \gets V$
      \For{each $s \in S$}
        \State $V'(s) \gets R(s) + \max_{a \in A} \sum_{s'} T(s, a, s') V(s')$
      \EndFor
      \State $V \gets V'$
    \Until $V$ changes by a sufficiently small amount
  \end{algorithmic}
\end{algorithm}
```

## Value Iteration Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-17_06-value-iteration-algorithm.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_07_a-value-estimates-vs-iterations-plot.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_07_b-required-iterations-vs-gamma-plot.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_08-policy-loss-vs-iterations-plot.pdf)
```{=latex}
\end{center}
```

## Policy Iteration

In policy iteration \cite{howard1960dynamic} we start with a random initial values and policy and alternate between two steps for each iteration $i$:

- **Policy evaluation.** Use policy $\pi_i$ to calculate the values of each state using the discounted current values of their successor states. Since we are calculating the values under a particular policy, we drop the $\max$ operator:

    \begin{equation}
    V_{i+1}(s) = R(s) + \gamma \sum_{s'} T(s, a, s') V(s')
    \end{equation}

- **Policy improvement.** Calculate policy $p_{i+1}$ using the values calculated in the previous step.

When policy improvement does not change the policy, an optimal policy has been found and policy iteration terminates.

Note that since the update equation used in policy evaluation is linear, we can use linear algebra to solve the set of simultaneous linear equations in $O(n^3)$. This method works fine for smaller state spaces but may be too expensive for large state spaces. A solution to this problem is known as modified policy iteration \cite{van-nunen1976set,puterman1978modified}, which combines policy iteration with value iteration by using a bounded number of Bellman updates to perform the policy evaluation step.


## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_09-policy-iteration-algorithm.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_10-mdp-expectimax-tree.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_11-uct-performance-plot.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_12-bandits.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_13-switch-mdp-restart-mdp.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_14-bernoulli-bandit.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_15-plan-values-belief-state-b.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_16-pomdp-value-iteration-algorithm.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_17-pomdp-expectimax-tree.pdf)
```{=latex}
\end{center}
```

## Markov Decision Processes

```{=latex}
\begin{center}
```
![](aima-fig-17_18-pomdp-belief-state-sequence.pdf)
```{=latex}
\end{center}
```
