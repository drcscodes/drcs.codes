---
title: Artificial Intelligence
subtitle: Multiagent Systems (AIMA 18.1, MAS 1-2)
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

## Multiagent Systems

- Multiagent environments
- (Noncooperative) game theory

## Multiagent Environments

Dealing with multiagent environments:

- Single agent with other agents considered part of the environment
- Multiple actors, but one decision maker controlling all actors
- Multiple actors, each of which makes its own decisions

## One Decsion Maker

Rests on **benevolent agent assumption**: agents will do what they are told.

Action synchronization:

- Sumultaneous/joint actions
- Mutually exclusive actions executed at different times
- Sequential actions $A$ before $B$ when $A$'s postconditions are $B$'s preconditions

Architectures:

- **Multieffector planning**: multiple concurrently acting effectors
- **Multibody planning**: physically decoupled effectors

    - Centralized planning: sensor information from each body is pooled
    - Decentralized planning: plan execution partially or fully decoupled, explicit communication to share information when possible (e.g., back in comms range)

## Multiple Decision Makers

All agents, a.k.a. **counterparts**, make decisions.  Two categories:

1. Agents have a **common goal**.

    - Agents **coordinate** to accomplish common goal, e.g., workers in a company, players on a team

2. Agents have differeent goals.

    - Goals may be unrelated, diametrically opposed (e.g., zer-sum games), or anythin in between.


## Game Theory

Multiple decision makers pursuing their own preferences.

- An agent must take into account preferences of other agents.
- These other agents also take into account preferences of other agents, and so on.

**Game theory**: the theory of **strategic decision making**.

- *Strategic* because decisions must take into account how other players act.
- Strategic aspect distinguishes game theory from decision theory.

Just as decision theory provides the theoretical foundation for single-agent decision making, game theory provides the theoretical foundation for multiagent decision making.


## Game Theory in AI

In AI, game theory can be used in two main ways:

1. **Agent design**: analyzing decisions in multiagent environments.

    - Enumerate possible decisions
    - Compute expected utility of each decision

2. **Mechanism design**: deisgn multiagent environment in such a way that when agents act selfishly to maximize utility, it has the effect of maximizing some collective good.

    - Example: protocols for Internet routers
    - Example: criminal legal system

## Cooperative vs Noncooperative Games

Two broad categories of game models:

1. Cooperative games:

    - Binding agreement between agents ensuring cooperation.

2. Noncooperative games:

    - Not necessarily competitive.
    - Simply means no binding agreement to cooperate.

Often mix models:

- Package company: centralized planning for routes and trucks, decentralized execution via autonomous decisions of drivers and pilots responsing individually to real-time conditions.
- Company: individual **incentives** for employees designed to bring their behavior into alignment with company's goals.

## Multiagent Planning

Use generic term **actor** for effectors, bodies and agents.  Need to define:

- transition models
- correct plans
- planning algorithms

Agents must take into account the way in which their own actions interact with the actions of other agents.

- Example: Agent $A$'s action might clobber the precoditions of the action Agent $B$ planned to execute.

## Concurrency Models

Three approaches to dealing with concurrency:

1. **Interleaved execution**.  Given Agents $A$ and $B$ with plans $[a_1, a_2]$ and $[b_1, b_2]$ there are six ways to execute them concurrently:

    ```{=latex}
    \begin{align*}
    [a_1,a_2,b_1,b_2]\\
    [b_1,b_2,a_1,a_2]\\
    [a_1,b_1,a_2,b_2]\\
    [b_1,a_1,b_2,a_2]\\
    [a_1,b_1,b_2,a_2]\\
    [b_1,a_1,a_2,b_2]
    \end{align*}
    ```

    - Plans must be correct with respect to all possible interleavings.
    - Popular in OS concurrency on single CPU.
    - Does not model true concurrency, i.e., simultaneous action.
    - Number of sequences grows exponentially with numbers of agents and actions.

2. **True concurrency**: leave plans *partially ordered* and don't create a fully serialized ordering.

3. **Synchronization**: global clock, each action takes one time step, joint actions execute simultaneously, no-ops in case "waiting" is needed.

## Multiagent Transition Models

Deterministic single-agent case: `RESULT(s, a)` with $b$ choices for the action.

Multiagent case: with $n$ actors, joint action $\langle a_1, \dots, a_n \rangle$ where $a_i$ is actoin taken by  $i$th actor.

- Must describe transition model for $b^n$ joint actions.
- Joint planning problem with branching factor of $b^n$.

Standard solution: pretend problems are decoupled and fix the interactions as they arise, i.e., writing action schemas as if actors acted independently.  Let's see how this works with an example ...


## Example: Doubles Tennis Planning

:::: {.columns}
::: {.column width="40%"}

```{=latex}
\begin{center}
```
![](doubles-tennis.jpg)
```{=latex}
\end{center}
```

:::
::: {.column width="60%"}

```{=latex}
\begin{center}
```
![](aima-fig-18_01-doubles-tennis-problem.pdf)
```{=latex}
\end{center}
```

Here's a 2-step **joint plan** that works:

```{=latex}
\begin{align*}
\text{PLAN 1}: &A : [Go(A,RightBaseline),Hit(A,Ball)] \\
               &B : [NoOp(B),NoOp(B)].
\end{align*}
```


:::
::::

## Concurrent Action Constraints


What if both players try to $Hit$ at the same time?  Add a **concurrent action constraint** to prevent:

```{=latex}
\vspace{-.25in}
\begin{align*}
& Action(Hit(actor, Ball),\\
& \hspace{.1in} \text{CONCURRENT:} \forall b, b \neq Actor \implies \neg Hit(b, Ball)\\
& \hspace{.1in} \text{PRECOND:} Approaching(Ball, loc) \land At(actor, loc) \\
& \hspace{.1in} \text{EFFECT:} Returned(Ball))
\end{align*}
\vspace{-.25in}
```

Some tasks require concurrent action, e.g., carrying a large cooler:

```{=latex}
\vspace{-.25in}
\begin{align*}
& Action(Carry(actor, cooler, here, there),\\
& \hspace{.1in} \text{CONCURRENT:} \exists b, b \neq Actor \land Carry(b, cooler, here, there) \\
& \hspace{.1in} \text{PRECOND:} At(actor, here) \land At(cooler, here) \land Cooler(cooler) \\
& \hspace{.1in} \text{EFFECT:} At(actor, there) \land At(cooler, there) \land \neg At(actor, here) \land \neg At(cooler, here)
\end{align*}
\vspace{-.25in}
```

## Cooperation and Coordination

There can be multiple joint plans that acheive the goal:

:::: {.columns}
::: {.column width="50%"}

```{=latex}
\begin{align*}
\text{PLAN 1}: &A : [Go(A,RightBaseline),Hit(A,Ball)] \\
               &B : [NoOp(B),NoOp(B)].
\end{align*}
```

:::
::: {.column width="50%"}

```{=latex}
\begin{align*}
\text{PLAN 2}: &A : [Go(A,LeftNet),NoOp(A)] \\
               &B : [Go(B, RightBaseline), Hit(B, Ball)]
\end{align*}
```

:::
::::

If both agents choose Plan 1 or 2, goal is acheived.  If one agent chooses 1 and other chooses 2, goal is not acheived.  How to coordinate?

- **Convention**: any constraint on selection of joint plans.

    - Example: "stick to your side of the court."
    - Widespread conventions are sometimes called **social laws**.

- **Communication**

    - Example: shout "Mine!" or "Yours!"
    - Can be implicit, based on observation -- **plan recognition**.

## Games with a Single Move: Normal Form Games

All players take action that are chosen simultaneously with no knowledge of other players' choices and the result of the game is based on the profile of actions that are selected in this way.

**Normal form game** defined by:

- **Players** or agents who will be making decisions. Two-player games have received the most attention, although n-player games for $n > 2$ are also common. We give players capitalized names, like $Ali$ and $Bo$ or $O$ and $E$.

- **Actions** that the players can choose. We will give actions lowercase names, like one or testify. The players may or may not have the same set of actions available.

- **Payoff function** that gives the utility to each player for each combination of actions by all the players. For two-player games, the payoff function for a player can be represented by a matrix in which there is a row for each possible action of one player, and a column for each possible choice of the other player: a chosen row and a chosen column define a matrix cell, which is labeled with the payoff for the relevant player. In the two- player case, it is conventional to combine the two matrices into a single **payoff matrix**, in which each cell is labeled with payoffs for both players.


## Example: Two-Finger Morra

Here is the payoff matrix for **two-finger Morra**, a game in which each player displays one or two fingers.

```{=latex}
\begin{center}
\begin{tabular}{|c|c|c|}\hline
       & O: one         & O: two         \\\hline
E: one & E = +2, O = -2 & E = -3, O = +3 \\\hline
E: two & E = -3, O = +3 & E = +4, O = -4 \\\hline
\end{tabular}
\end{center}
```

- $E$ is the **row player**, $O$ is the **column player**.
- Each cell shows the payoffs given the players' actions.

## Solution Concepts

A **solution concept** is a way of choosing actions that take other players' actions into account.  Some important terminology:

- **Strategy**: like a policy, but we must account for the actions of the other players.

- **Pure strategy**: a deterministic strategy/policy.  For a single-move game, a single action.

- **Mixed strategy**: a randomized policy.  The mixed strategy that chooses action $a$ with probability $p$ and action $b$ otherwise is written $[p:a;(1 - p):b]$.

    - Two-finger Morra example: $[0.5:one;0.5:two]$

- **Strategy profile**: an assignment of a strategy to each player.

- **Outcome**: a numeric value for each player.  For mixed strategies, this is expected utility.

Solution concepts define rationality in games.

## Morra Minimax Trees with Pure Strategies

:::: {.columns}
::: {.column width="50%"}

```{=latex}
\begin{center}
```
![](aima-fig-18_02_a-morra-e-minimax-tree-pure-strategy.pdf)
```{=latex}
\end{center}
```

:::
::: {.column width="50%"}

```{=latex}
\begin{center}
```
![](aima-fig-18_02_b-morra-o-minimax-tree-pure-strategy.pdf)
```{=latex}
\end{center}
```

:::
::::

## Morra Minimax Trees with Mixed Strategies

:::: {.columns}
::: {.column width="50%"}

```{=latex}
\begin{center}
```
![](aima-fig-18_02_c-morra-e-parameterized-tree-mixed-strategy.pdf)
```{=latex}
\end{center}
```

:::
::: {.column width="50%"}

```{=latex}
\begin{center}
```
![](aima-fig-18_02_d-morra-o-parameterized-tree-mixed-strategy.pdf)
```{=latex}
\end{center}
```

:::
::::

## Multiagent Systems

```{=latex}
\begin{center}
```
![](aima-fig-18_02_e-second-player-action-prob-mixed-strategy.pdf)
```{=latex}
\end{center}
```

## Multiagent Systems

```{=latex}
\begin{center}
```
![](aima-fig-18_02_f-second-player-action-prob-mixed-strategy.pdf)
```{=latex}
\end{center}
```

## Hawk Strategy in IPD

```{=latex}
\begin{center}
```
![](aima-fig-18_03_a-ipd-hawk-fsm.pdf)
```{=latex}
\end{center}
```

## Dove Strategy in IPD

```{=latex}
\begin{center}
```
![](aima-fig-18_03_b-ipd-dove-fsm.pdf)
```{=latex}
\end{center}
```

## Grim Strategy in IPD

```{=latex}
\begin{center}
```
![](aima-fig-18_03_c-ipd-grim-fsm.pdf)
```{=latex}
\end{center}
```

## Tit for Tat Strategy in IPD

```{=latex}
\begin{center}
```
![](aima-fig-18_03_d-ipd-tit-for-tat-fsm.pdf)
```{=latex}
\end{center}
```

## Tat for Tit Strategy in IPD

```{=latex}
\begin{center}
```
![](aima-fig-18_03_e-ipd-tat-for-tit-fsm.pdf)
```{=latex}
\end{center}
```

## Multiagent Systems

```{=latex}
\begin{center}
```
![](aima-fig-18_04-extensive-form-counterintuitive-nash-equilibrium.pdf)
```{=latex}
\end{center}
```

## Multiagent Systems

```{=latex}
\begin{center}
```
![](aima-fig-18_06-paperclip-game-tree.pdf)
```{=latex}
\end{center}
```
