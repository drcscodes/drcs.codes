---
title: Artificial Intelligence
subtitle: Probabilistic Temporal Reasoning
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

## Probabilistic Temporal Reasoning (AIMA 14.1-14.3)

Recall belief state maintenance from the Kindergarten vacuum world (square not being actively cleaned can become dirty):

```{=latex}
\begin{center}
```
![](aima-fig-04_17-vacuum-prediction-update-cycles.pdf){height="30%"}
```{=latex}
\end{center}
```

- Most real-world environments partially observable.  Belief state maintenance is core task.
- Also known as **monitoring**, **filtering**, and **state estimation**.

$$
b' = Update(Predict(b,a),o).
$$

- Equation above is called a recursive state estimator because it computes the new belief state from the previous one rather than by examining the entire percept sequence.

Previous methods allowed us to represent belief states as sets of possible worlds, but could not compute or represent how likely each state were.  In this lesson we use the tools of probability theory to quantify our degree of belief in elements of the belief state.

## Elements of Stochastic Temporal Models

A changing world is modeled using

- a variable for each aspect of the world state at each point in time,

- a transition model describing the probability distribution of the variables at time $t$, given the state of the world at past times, and

- a sensor model (a.k.a. observation model) describing the probability of each percept at time $t$, given the current state of the world.

## Time and Uncertainty

Static worlds: each random variable has a single fixed value.

Example: car repair.  Car stays broken during diagnosis.

Dynamic worlds: each random variable has a value for each time step which depends on the values of other random variables in previous time steps.

Example: Diabetes.

- Task is to assess current state of the patient -- blood sugar and insulin levels -- in order to choose patient's food intake and insulin dose.

- Blood sugar levels and measurements thereof can change rapidly over time, depending on recent food intake and insulin doses, metabolic activity, the time of day, and so on.

- To assess the current state from the history of evidence and to predict the outcomes of treatment actions, we must model these changes.


Other examples:

- Robot location tracking
- Tracking national economic activity
- Interpreting written or spoken sequences of words.

## Discrete-Time Models

In **Discrete-time** models:

- World is a series of snapshots or **time slices**.
- Time slices numbered $0, 1, 2, \dots$
- Time interval $\Delta$ between slides assumed to be the saem for every interval.
- Particular applications use particular choices of $\Delta$, e.g., $\frac{1}{30}$ of a second.
- Choice of $\Delta$ should reflect rates of change.

    - E.g., blood glucose can change siginificantly in 10 minutes, so $\Delta = 1$ minute might be appropriate.

Discrete vs continuous time:

- Continuous time systems can be modeled by stochastic differential equations (SDEs).
- Descrete-time models presented here are approximations to SDEs.

## States and Observations

Each time slice contains a set of random variables:

- $\bm{X}_t$ is a set of unobservable state variables at time $t$.
- $\bm{E}_t$ is a set of observable evidence variables at time $t$.

Observation at time $t$ is $\bm{E}_t = \bm{e}_t$ for some set of values $\bm{e}_t$.

**Example: Security guard in underground facility.**  You are stuck inside with no access to outside world.  Each morning you observe a person walking in with or without an umbrella.

- $\Delta$ is one day, each $t$ is a day.
- $\bm{E}_t$ contains a single evidence variable, $Umbrella_t$ or $U_t$ for short.
- $\bm{X}_t$ contains a single state variable, $Rain_t$ or $R_t$ for short.

**Example: diabetes**.

- $\bm{E}_t = \{ MeasuredBloodSugar_t, PulseRate_t \}$
- $\bm{X}_t = \{ BloodSugar_t, StomacheContents_t \}$

A few assumptions about $t$:

- State sequence starts at time $t = 0$. (In umbrella world, $\bm{X} = \{R_0, R_1, R_2, \dots \}$.)
- Evidence starts arriving at time $t = 1$. (In umbrella world, $\bm{E} = \{U_1, U_2, \dots \}$.)
- $\bm{X}_{a:b}$ denotes set of variables from $\bm{X}_a$ to $\bm{X}_b$, inclusive.

    - Note: inclusive, unlike Python where `U[1:3]` includes only `U[1]` and `U[2]`


## Transition Models

The transition model specifies the probability distribution over the latest state variables, given previous values: $Pr(\bm{X}_t \mid \bm{X}_{0:t-1})$

- Problem: $\bm{X}_{0:t-1})$ is unbounded -- size increases as $t$ increases.
- Solution: **Markov assumption** -- current state depends on a finite fixed number of previous states.

    - First studied by Andrei Markov (1856-1922), now called **Markov processes** or **Markov chains**.

In these Bayes nets:

```{=latex}
\begin{center}
```
![](aima-fig-14_01-bayes-net-markov-processes.pdf)
```{=latex}
\end{center}
```

- (a) First-order Markov process: $Pr(\bm{X}_t \mid \bm{X}_{0:t-1}) = Pr(\bm{X}_t \mid \bm{X}_{t-1})$
- (b) Second-order Markov process: $Pr(\bm{X}_t \mid \bm{X}_{0:t-1}) = Pr(\bm{X}_t \mid \bm{X}_{t-2}, \bm{X}_{t-1})$

## Time-Homogeneous Processes

Problem:

- Inifintely many values of $t$.
- Could be different distributions for each variable at each time step.

Solution: assume **time homogeneity**, i.e., state changes caused by laws that don't change over time.

Example: Umbrella world

- $Pr(R_t \mid R_{t-1})$ is the same for all $t$
- Only need one conditional probability table.

## Sensor Models

**Sensor Markov assumption**: state alone is sufficient to generate current sensor values.

$$
Pr(\bm{E}_t \mid \bm{X}_{0:t}, \bm{E}_{1:t-1}) = Pr(\bm{E}_t \mid \bm{X}_t) \tag{14.2}
$$

```{=latex}
\begin{center}
```
![](aima-fig-14_02-bayes-net-umbrella-world.pdf){height="40%"}
```{=latex}
\end{center}
```

- Transition model is $Pr(Rain_t \mid Rain_{t-1})$.
- Sensor model is $Pr(Umbrella_t \mid Rain_t)$.
- Arrows go from actual state to sensor values: states *cause* sensor values.

    - Inference goes in other direction: given sensor values, what are the state values.

## Full Joint Over All Variables in a Temporal Model

For the initial state of the system at time $0$ we specify a prior $Pr(\bm{x}_0)$.  Now we can use Equation 13.2 ($Pr(x_1, \dots, x_n) = \prod_{i=1}^n Pr( x_i | parents(X_i))$):

$$
Pr(\bm{X}_{0:t}, \bm{E}_{1:t}) = \underbrace{Pr(\bm{X}_0)}_{\text{Initial state model}} \prod_{i=1}^t \underbrace{Pr(\bm{X}_i \mid \bm{X}_{i-1})}_{\text{Transition model}} \underbrace{Pr(\bm{E}_i \mid \bm{X}_i)}_{\text{Sensor model}}
$$

Standard Bayes nets can only represent a finite set of variables.  Dynamic bayesian networks overcome this limitation by:

- defining infinite sets by integer indices, and
- using implicit universal quantification to define sensor and transition models for every time step.

## Markov Model Considerations

Sometimes Markov assumption is valid, sometimes it's only an approximation.  Two ways to improve the approximation:

1. Increase the order of the Markov process model.  E.g., In Palo Alto, CA, rarely rains more than two days in a row.  A 2nd-order Markov model could express this fact: $Pr(r_t \mid r_{t-1}, r_{t-2}) \ll Pr(r_t \mid r_{t-1}, \neg r_{t-2})$.

2. Increase the set of state variables.  E.g., add $Season_t$ for hisotircal records, or $Temperature_t$, $Humidity_t$, and $Pressure_t$ to use a physical model of rainy conditions.

Battery example (p. 483)

## Inference in Temporal Models

- **Filtering**, a.k.a., **state estimation** is
- **Prediction**:
- **Smoothing**:
- **Most likely explanation**:

## Learning Temporal Models

Unknown transition and sensor models can be learned from observations.

- As with static Bayesian networks, dynamic Bayes net learning can be done as a by-product of inference.

- Inference provides an estimate of transitions that actually occurred and the states that generated the sensor readings, and these estimates can be used to learn the models.

- Learning via iterative update algorithm, expectation–maximization or EM, or Bayesian updating of the model parameters given the evidence.

We'll return to these ideas in our lesson on [statistical learning](statistical-learning.pdf).

## Filtering and Prediction



## Smoothing

```{=latex}
\begin{center}
```
![](aima-fig-14_03-smoothing.pdf)
```{=latex}
\end{center}
```

## Forward-Backward Smoothing Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-14_04-forward-backward-algorithm.pdf)
```{=latex}
\end{center}
```

## Finding the Most Likely Sequence

```{=latex}
\begin{center}
```
![](aima-fig-14_05-rain-state-sequences.pdf)
```{=latex}
\end{center}
```

## Hidden Markov Models (HMMs)

An HMM is a temporal probabilis- tic model in which the state of the process is described by a single, discrete random variable.

## HMM Matrix Formulation

```{=latex}
\[
\bm{T}_{ij} = Pr(X_t = j \mid X_{t-1} = i)
\]
```

```{=latex}
\begin{center}
```
![](aima-fig-14_02-bayes-net-umbrella-world.pdf)
```{=latex}
\end{center}
```


```{=latex}
\[
\bm{T}_{ij} = Pr(X_t \mid X_{t-1}) =
\begin{bmatrix}
0.7 & 0.3 \\
0.3 & 0.7
\end{bmatrix}
\]
```




## Fixed Lag Smoothing Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-14_06-fixed-lag-smoothing-algorithm.pdf)
```{=latex}
\end{center}
```

## Localization with HMMs

```{=latex}
\begin{center}
```
![](aima-fig-14_07-posterior-robot-location.pdf)
```{=latex}
\end{center}
```

## HMM Performance

```{=latex}
\begin{center}
```
![](aima-fig-14_08-hmm-localization-performance-plots.pdf)
```{=latex}
\end{center}
```
