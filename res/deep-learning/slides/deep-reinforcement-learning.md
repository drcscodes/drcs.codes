---
title: Deep Reinforcement Learning
author: CS 4277 Deep Learning
institute: Kennesaw State University
aspectratio: 1610
fontsize: 10pt
colorlinks: yes
urlcolor: blue
header-includes:
- |
  ```{=latex}
  \input{beamer-common}
  %\titlegraphic{\includegraphics[width = 1in]{chris-simpkins-headshot-320px}}
  \usepackage{framed}
  \usepackage{xcolor}
  \usepackage{tikz,pgfplots}
  \let\oldquote=\quote
  \let\endoldquote=\endquote
  \colorlet{shadecolor}{cyan!15}
  \renewenvironment{quote}{\begin{shaded*}\begin{oldquote}}{\end{oldquote}\end{shaded*}}
  ```
---

## Agents, AI and Machine Learning

An agent is an independent entity that perceives its environment and takes action that changes the state of the environment.

```{=latex}
\begin{center}
```
![](./agent-environment.pdf){height="60%"}[^RussellNorvig2020]
```{=latex}
\end{center}
```

- The fundamental goal of AI is to understand and build *intelligent agents* that choose actions in pursuit of *goals*.
- Most of machine learning is concerned with *pattern recognition*.

[^RussellNorvig2020]: https://aima.cs.berkeley.edu/

## Our Time Has Come!

```{=latex}
\begin{center}
```
![](./barto-sutton-turing-award-2024.png){height="80%"}[^BartoSuttonTurningAward2024]
```{=latex}
\end{center}
```

[^BartoSuttonTurningAward2024]: https://amturing.acm.org/

## Reinforcement Learning

An intelligent agent learns how to behave from experience interacting with the world.

- We represent subsets of the world as *environments* comprised of *states*..
- An *agent* takes an *action* that causes a transition to a new state.
- The agent receives a scalar feedback signal, called a *reward*, from the environment after the transition to a new state.
- The agent maximizes the long-term expected value of cumulative reward.

Reinforcement learning directly addresses the intelligent agent problem.  Its central hypothesis is:

>All of what we mean by goals and purposes can be well thought of as the maximization of the expected value of the cumulative sum of a received scalar signal (called reward).[^SuttonBarto2018]

[^SuttonBarto2018]:http://incompleteideas.net/book/the-book-2nd.html

## Markov Process

A markov process models the world as a set of states and associated transition probability distributions, calles a *transition function*, that models how the world moves from one state to the next.

```{=latex}
\[
Pr(s_{t+1} | s_t)
\]
```

is the probability that the state at time $t+1$ is $s_{t+1}$, given that the previous state is $s_t$.  The fact that the transition probability depends only on the previous state and not the history of all previous states is called the *Markov assumption*.

```{=latex}
\begin{center}
```
![](./ReinforceMDP.pdf){height="40%"}
```{=latex}
\end{center}
```

A sequense of states from a Markov process is called a *trajectory*: $\tau = (s_1, S_2, ...)$.

## Markov Reward Process

A *Markov reward process* adds a reward distribution $Pr(r_{t+1} | s_t)$ (note that this implicitly accompanies a state transition).  Now a trajectory includes the rewards, $\tau = (s_1, r_2, s_2, r_3...)$, and the sum of cumulative discounted future rewards, the *return*, is:

```{=latex}
\[
G_t = \sum_{k = 0}^\infty \gamma^k r_{t+k+1}
\]
```

$\gamma$ is the *discount factor* which says how much we discount future rewards.  With $\gamma < 0$ it decays to zero.

```{=latex}
\begin{center}
```
![](./ReinforceMDP2.pdf){height="40%"}
```{=latex}
\end{center}
```

## Markov Decision Process (MDPs)

A *Markov decision process* (MDP) adds a set of *actions* at each time step.  Now:

- transition probabilities are $Pr(s_{t+1} | s_t, a_t)$.  Sometimes written as $T(s, a, s')$ -- a *transition model* that returns the probability that taking action $a$ in state $s$ results in state $s'$.
- the reward probabilities are $Pr(r_{t+1} | s_t, a_t)$.  This is sometimes written as $r(s, a, s')$
- a trajectory is $\tau = (s_1, a_1, r_2, s_2, a_2, r_3...)$

```{=latex}
\begin{center}
```
![](./ReinforceMDP3.pdf){height="50%"}
```{=latex}
\end{center}
```

## Parially-Observable MDP (POMDP)

In a *partially observable Markov decision process* (POMDP) the state is not fully observable.  The agent receives an observation drawn from a probability distribution $Pr(o_t | s_t)$.  Now a trajectory is $\tau = (s_1, o_1, a_1, r_2, s_2, o_2, r_3...)$

```{=latex}
\begin{center}
```
![](./ReinforcePOMDP.pdf)
```{=latex}
\end{center}
```

## Policy

The goal of a reinforcement learning algorithm is to learn a *policy*: a deterministic or stochastic function mapping states to actions.

- Stationary: $\pi(a | s)$
- Non-stationary: $\pi(a_t | s_t)$

```{=latex}
\begin{center}
```
![](./ReinforceMDPLoop.pdf)
```{=latex}
\end{center}
```

## State and Action Values

- State value function: $v(s_t | \pi) = \mathbb{E} [G_t | s_t, \pi]$
- Action value function: $q(s_t, a_t | \pi) = \mathbb{E} [G_t | s_t, a_t, \pi]$

```{=latex}
\begin{center}
```
![](./ReinforceValueOfAction.pdf)
```{=latex}
\end{center}
```

## Optimal Policy

An optimal policy maximizes the expected return.  Any MDP has a deterministic stationary optimal policy, i.e., it maximizes the value of every state.  Given this policy:

```{=latex}
\[
v^*(s_t ) = \max_{\pi} \big( \mathbb{E} [G_t | s_t, \pi] \big)
\]
```

The optimal action value function is then:

```{=latex}
\[
q^*(s_t, a_t ) = \max_{\pi} \big( \mathbb{E} [G_t | s_t, a_t \pi] \big)
\]
```

If we know $q^*$ we can use it to derive $\pi^*$:

```{=latex}
\[
\pi^*(a_t | s_t ) \leftarrow \argmax_{a_t} \big( q^*(s_t, a_t ) \big)
\]
```

We'll see this idea when we solve MDPs using dynamic programming.

## Consistent State Values

Whatever the values of the states or actions for a given policy, they must be consistent.

```{=latex}
\[
v(s_t ) = \sum_{a_t} \pi(a_t | s_t) q(s_t, a_t)
\]
```

```{=latex}
\begin{center}
```
![](./ReinforceBellman3.pdf)
```{=latex}
\end{center}
```

## Consistent Action Values

The value of an action in a state is the immediate reward plus the value of the resulting next state.  Assuming deterministic reward and  probabilistic transition function:

```{=latex}
\[
q(s_t, a_t) = r(s_t, a_t) + \gamma \sum_{s_{t+1}} Pr(s_{t+1} | s_t, a_t) v(s_{t+1})
\]
```


```{=latex}
\begin{center}
```
![](./ReinforceBellman2.pdf)
```{=latex}
\end{center}
```

## Bellman Equations

If we substitute the action value function into the state value function we get:

```{=latex}
\[
v(s_t ) = \sum_{a_t} \pi(a_t | s_t) \big( r(s_t, a_t) + \gamma \sum_{s_{t+1}} Pr(s_{t+1} | s_t, a_t) v(s_{t+1})  \big)
\]
```

If we substitute the state value function into the action value function we get:

```{=latex}
\[
q(s_t, a_t) = r(s_t, a_t) + \gamma \sum_{s_{t+1}} Pr(s_{t+1} | s_t, a_t) \Huge( \sum_{a_{t+1}} \pi(a_{t+1} | s_{t+1}) q(s_{t+1}, a_{t+1})  \Huge)
\]
```

Thesej two relations are called the *Bellman equations*.  They say that state and action values mult be self-consistent, so when we update the estimated value of a state or actoin, we have to update all the others that depend on the updated value.

## Tabular RL

In classical tabular RL, we represent the policy function as a table.

- Model-based: use the MDP to solve for the best policy.

    - Policy iteration
    - Value iteration

- Model-free: estimate from observed trajectories

    - Tabular Q-Learning and SARSA
    - Function approximation (including deep RL)

*Monte Carlo* methods simulate trajectories (called *rollouts*) under some policy and use the information from the rollouts to improve the policy.

## Dynamic Programming

If we know the MDP, we can find the optimal policy using dynamic programming, where we iteratively update our estimates of state and action values until they converge.

```{=latex}
\begin{center}
```
![](./ReinforceDP.pdf)
```{=latex}
\end{center}
```

## Policy Iteration

Use the Bellman equaiotns to solve the MDP.

**Policy evaluation**: sweep through states $s_t$, updating values:

```{=latex}
\[
v(s_t ) = \sum_{a_t} \pi(a_t | s_t) \Big( r(s_t, a_t) + \gamma \sum_{s_{t+1}} Pr(s_{t+1} | s_t, a_t) v(s_{t+1})  \Big)
\]
```

**Policy improvement**: update policy with greedy action selection:

```{=latex}
\[
\pi(a_t | s_t) =\argmax_{a_t} \Big( r(s_t, a_t) + \gamma \sum_{s_{t+1}} Pr(s_{t+1} | s_t, a_t) v(s_{t+1}) \Big)
\]
```


## Monte Carlo Methods

Sample the MDP via episodes -- a trajectory from a start state to a terminal state using the current policy (also called a *rollout*):

- use the returns for a given $(s, a)$ pair to estimate $q(s, a)$
- use the estimates for each $q(s, a)$ to update the policy:

```{=latex}
\[
\pi(s, a) \leftarrow \argmax_{a} \big( q(s, a) \big)
\]
```

```{=latex}
\begin{center}
```
![](./ReinforceMC.pdf)
```{=latex}
\end{center}
```


## Temporal Difference Methods

Combine the ideas of dynamic programming and Monte Carlo methods.  Instead of generating rollouts to estimate values with which to update the policy, we iteratively update the policy while the agent traverses the MDP.

```{=latex}
\begin{center}
```
![](./ReinforceTD.pdf)
```{=latex}
\end{center}
```

## Q-Learning and SARSA

In typical learning scenarios we don't have the MDP, so we learn a direct mapping from states to actions, an action-value function, a Q-function.

1. $Q \gets$ random initial values
2. For each episode
   1. $s \gets$ world.initialState()
   2. While $s$ is not terminal
      1. $a$ $\gets$ $\epsilon-$greedy action for $s$ from $\pi$ derived from $Q$
      2. Execute $a$, observe effects $r$ and $s'$
      3. $Q(s, a) \gets Q(s, a) + \alpha [R(s) + \gamma \max_{a'} Q(s', a') - Q(s, a)]$
      4. $s \gets s'$

For the Sarsa variant of Q-learning, save $a$ in $a'$ and replace the update in Step 2.2.3 with

\begin{equation}
Q(s, a) \leftarrow Q(s, a) + \alpha [R(s) + \gamma Q(s', a') - Q(s, a))]
\end{equation}

Sarsa is *on-policy* because the temporal difference used in the Q-update is based on the policy being followed by the agent during learning. The standard Q-learning update is *off-policy* because the Q-update is based on the best known next action.

# Deep Reinforcement Learning

## Fitted Q-Learning

Tabular RL is only practical if the state-action space is small.  Such cases are rare in practice, e.g., there are more than $10^{40}$ legal configurations of a chess board (states).

Solution: *fitted Q-learning* -- replace the q-table with a parameterized machine learning model $q(\bm{s}, a_t, \bm{\phi})$ where the state is now a vector, not an index in to a table of states.

Now we can define a least-squares loss based on consistency of adjacent q-values:

```{=latex}
\[
L(\bm{\phi}) = \left( r(\bm{s}_t, a_t) + \gamma \max_a \left( q(\bm{s}_{t+1}, a, \bm{\phi})  \right) - q(\bm{s}_{t}, a_t, \bm{\phi}) \right)^2
\]
```

and turn this into the udate rule:

```{=latex}
\[
\bm{\phi} \gets \bm{\phi} + \alpha \left( r(\bm{s}_t, a_t) + \gamma \max_a \left( q(\bm{s}_{t+1}, a, \bm{\phi})  \right) - q(\bm{s}_{t}, a_t, \bm{\phi}) \right)
    \frac{ \partial q(\bm{s}_t, a_t, \bm{\phi})  }{ \partial \bm{\phi}  }
\]
```

Problem: convergence is no longer guaranteed as it was in tabular RL because changes to $\bm{\phi}$ can change the target return estimate and the q-value predictions -- convergence is a moving target.

## Deep Q-Networks for Playing Atari Games

First big breakthough in Deep RL was a system that learned to play Atari 2600 games "from pixels."

```{=latex}
\begin{center}
```
![](./ReinforceDQL.pdf){height="50%"}
```{=latex}
\end{center}
```

## DQN Architecture

In practice, the frames were downsized to 84x84, used only pixel brightness instead of colors, and 4 frames as a single state to deal with unobservable properties like ball velocity.

```{=latex}
\begin{center}
```
![](./ReinforceDQL2.pdf){height="60%"}
```{=latex}
\end{center}
```

Network takes the sate as input and simultaneously predicts values for all actions.

## DQN Training

Training was modified by:

- Using a constant -1 or +1 to represent score increases or decreases, so that a constant learning rate could be used and the same training procedure for all games, and
- Using *experience replay*: recent $<\bm{s}_t, a_t, r_{t+1}, \bm{s}_{t+1}>$ tuples stored in a buffer, then randomly sampled at each time step to generate a batch.


Fix convergence issue in fitted Q-Networks by fixing target parameters to $\bm{\phi}^-$ and only updading periodically, leading to the updated update rule:

```{=latex}
\[
\bm{\phi} \gets \bm{\phi} + \alpha \left( r(\bm{s}_t, a_t) + \gamma \max_a \left( q(\bm{s}_{t+1}, a, \bm{\phi}^-)  \right) - q(\bm{s}_{t}, a_t, \bm{\phi}) \right)
    \frac{ \partial q(\bm{s}_t, a_t, \bm{\phi})  }{ \partial \bm{\phi}  }
\]
```

## Double Q-Learning and Double Deep Q-Networks

THe update rule in DQN training systematically overestimates action values because the same network selects the target and updates the value.  Double DQN mitigates this problem by training two models simultaneously, randomly assigning updates to one or the other network.

## Double DQN with Target Network

1-9: Initialize learning rate $\alpha$,  $\tau$, number of batches per training step, B number of updates per batch, U, batch size N, experience replay memory with max size K, target network update frequency F, Randomly initialize the network parameters $\theta$, target network parameters $\varphi = \theta$

```{=latex}
\begin{center}
```
![](./ddqn-algo-fdrl.pdf){height="80%"}^[DDQN-algo-FDRL]
```{=latex}
\end{center}
```

[DDQN-algo-FDRL]: https://slm-lab.gitbook.io/foundations-of-deep-rl

## Policy Gradient Methods

```{=latex}
\begin{center}
```
![](./ReinforcePolicyGrad.pdf)
```{=latex}
\end{center}
```

## Actor-Critic Methods

- Actor: policy network
- Critic: value network

## Offline Reinforcement  Learning

```{=latex}
\begin{center}
```
![](./ReinforceDecisionTransformer.pdf)
```{=latex}
\end{center}
```
