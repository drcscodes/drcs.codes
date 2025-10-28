---
title: Artificial Intelligence
subtitle: Probabilistic Temporal Reasoning (AIMA 14.1-14.2)
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

## Probabilistic Temporal Reasoning

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

- Blood sugar levels and their measurements can change rapidly over time, depending on recent food intake, insulin doses, metabolic activity, the time of day, and so on.

- To assess the current state from the history of evidence and predict the outcomes of treatment actions, we must model these changes.


Other examples:

- Robot location tracking
- Tracking national economic activity
- Interpreting written or spoken sequences of words

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

- Problem: $\bm{X}_{0:t-1}$ is unbounded -- size increases as $t$ increases.
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

## Full Joint Distribution Over All Variables in a Temporal Model

For the initial state of the system at time $0$ we specify a prior $Pr(\bm{x}_0)$.  Now we can use Equation 13.2

$$
Pr(x_1, \dots, x_n) = \prod_{i=1}^n Pr( x_i | parents(X_i)) \tag{13.2}
$$

applied to the temporal variables in the dynamic version:

$$
Pr(\bm{X}_{0:t}, \bm{E}_{1:t}) = \underbrace{Pr(\bm{X}_0)}_{\text{Initial state model}} \prod_{i=1}^t \underbrace{Pr(\bm{X}_i \mid \bm{X}_{i-1})}_{\text{Transition model}} \underbrace{Pr(\bm{E}_i \mid \bm{X}_i)}_{\text{Sensor model}} \tag{14.3}
$$

Standard Bayes nets can only represent a finite set of variables.  Dynamic Bayes nets overcome this limitation by:

- defining infinite sets by integer indices, and
- using implicit universal quantification to define sensor and transition models for every time step.

## Markov Model Considerations

Sometimes Markov assumption is valid, sometimes it's only an approximation.  Two ways to improve the approximation:

1. Increase the order of the Markov process model.  E.g., In Palo Alto, CA, rarely rains more than two days in a row.  A 2nd-order Markov model could express this fact: $Pr(r_t \mid r_{t-1}, r_{t-2}) \ll Pr(r_t \mid r_{t-1}, \neg r_{t-2})$.

2. Add additional state variables.  E.g., add $Season_t$ for hisotircal records, or $Temperature_t$, $Humidity_t$, and $Pressure_t$ to use a physical model of rainy conditions.

**Example: Battery drainage in mobile robot.**  Two state variables: velocity and position.  Use Newton's laws of motion to calculate new positions.  Add probabilistic error (e.g., Gaussian noise) to account for uncertainty in velocity due to terrain, wind, etc.

Problems:

- Battery level affects velocity as it drains.
- Battery level depends on power used in all previous movements, violating the Markov assumption.

Solution: Add a state variable for battery level.  Track level in one of two ways:

1. Decrease level at each time step in response to movement executed in previous step.
2. Better: add a new sensor for battery level.


## Inference in Temporal Models

Given the general structure of a probabilistic temporal model, we can perform basic inference tasks:

- **Filtering**, a.k.a., **state estimation** is the task of computing the **belief state** $Pr(\bm{X}_t \mid \bm{e}_{1:t})$ -- the posterior distribution over the most recent state given all the evidence to date.

- **Prediction** is the task of computing the posterior distribution over the future state, given all evidence to date: $Pr(\bm{X}_{t+k} \mid \bm{e}_{1:t})$ for some $k > 0$.

- **Smoothing** is the task of computing the posterior distribution over a past state, given all evidence up to the present: $Pr(\bm{X}_k \mid \bm{e}_{1:t})$ for some $k$ such that $0 \le k < t$.

- **Most likely explanation**: Given a sequence of observations, we might wish to find the sequence of states that is most likely to have generated those observations: $\argmax_{x_{1:t}} Pr(\bm{x}_{1:t} \mid \bm{e}_{1:t})$.


## Learning Temporal Models

Unknown transition and sensor models can be learned from observations.

- As with static Bayesian networks, dynamic Bayes net learning can be done as a by-product of inference.

- Inference provides an estimate of transitions that actually occurred and the states that generated the sensor readings, and these estimates can be used to learn the models.

- Learning via iterative update algorithm, expectation–maximization or EM, or Bayesian updating of the model parameters given the evidence.

We'll return to these ideas in our lesson on [statistical learning](statistical-learning.pdf).

## Filtering

**Filtering**, a.k.a., **state estimation** is the task of computing the **belief state** $Pr(\bm{X}_t \mid \bm{e}_{1:t})$ -- the posterior distribution over the most recent state given all the evidence to date.

- Umbrella example: compute probability of rain today given all umbrella observations so far.
- Rational agent estimates its current state to enable rational decisions.
- Nearly identical calculation provides likelihood of evidence sequence $Pr(\bm{e}_{1:t})$
- The term "filtering" comes from signal processing, which sees the problem of state estimation as "filtering out the noise" in a signla to estimate its underlying properties.

A useful filtering algorithm needs to maintain a current state estimate and update it, rather than going back over the entire history of percepts for each update.

- Otherwise, the cost of each update increases as time goes by.

In other words, given the result of filtering up to time $t$, the agent needs to compute the result for $t + 1$ from the new evidence $\bm{e}_{t+1}$.  For some function $f$:

$$
Pr(\bm{X}_{t+1} \mid f \left( \bm{e}_{t+1}, Pr(\bm{X}_t \mid \bm{e}_{1:t}) \right)
$$

## Recursive State Estimation

We can view the calculation as being composed of two parts: first, the current state distribution is projected forward from $t$ to $t + 1$; then it is updated using the new evidence $\bm{e}_{t+1}$. This two-part process emerges quite simply when the formula is rearranged:

```{=latex}
\vspace{-.25in}
\begin{align*}
Pr(\bm{X}_{t+1} \mid \bm{e}_{1:t+1}) &= Pr(\bm{X}_{t+1} \mid \bm{e}_{1:t}, \bm{e}_{t+1}) \tag{Divide the evidence}\\
                                     &= \alpha Pr(\bm{e}_{t+1} \mid \bm{X}_{t+1}, e_{1:t}) Pr(\bm{X}_{t+1} \mid \bm{e}_{1:t}) \tag{Bayes rule, given $\bm{e}_{1:t}$}\\
                                     &= \alpha \underbrace{Pr(\bm{e}_{t+1} \mid \bm{X}_{t+1})}_{\text{update}} \underbrace{Pr(\bm{X}_{t+1} \mid \bm{e}_{1:t})}_{\text{prediction}} \tag{Sensor Markov assumption}
\end{align*}
```

Now plug in an expression for one-step prediction $Pr(\bm{X}_{t+1} \mid \bm{e}_{1:t})$ conditioned on the current state $\bm{X}_t$ to obtain the central result in probabilistic temoral reasoning:

```{=latex}
\vspace{-.25in}
\begin{align*}
Pr(\bm{X}_{t+1} \mid \bm{e}_{1:t+1}) &= \alpha Pr(\bm{e}_{t+1} \mid \bm{X}_{t+1}) \sum_{\bm{X}_t} Pr(\bm{X}_{t+1} \mid \bm{x}_t, \bm{e}_{1:t}) Pr(\bm{x}_t \mid \bm{e}_{1:t}) \\
                                     &= \alpha \underbrace{Pr(\bm{e}_{t+1} \mid \bm{X}_{t+1})}_{\text{sensor model}} \sum_{\bm{X}_t} \underbrace{Pr(\bm{X}_{t+1} \mid \bm{x}_t)}_{\text{transition model}} \underbrace{Pr(\bm{x}_t \mid \bm{e}_{1:t})}_{\text{recursion}} \tag{14.5}
\end{align*}
```

The last step applies the Markov assumption in the transition model.  All the terms come either from the model or from the previous state estimate.
Hence, we have the desired recursive formulation.

## Forward Message Propagation

```{=latex}
\vspace{-.2in}
\[
Pr(\bm{X}_{t+1} \mid \bm{e}_{1:t+1}) = \alpha \underbrace{Pr(\bm{e}_{t+1} \mid \bm{X}_{t+1})}_{\text{sensor model}} \sum_{\bm{X}_t} \underbrace{Pr(\bm{X}_{t+1} \mid \bm{x}_t)}_{\text{transition model}} \underbrace{Pr(\bm{x}_t \mid \bm{e}_{1:t})}_{\text{recursion}} \tag{14.5}
\]
```

We can think of the filtered estimate $Pr(\bm{X}_t \mid \bm{e}_{1:t})$ as a "message" $\bm{f}_{1:t}$ that is propagated forward along the sequence, modified by each transition and updated by each new observation. The process is given by

$$
\bm{f}_{1:t+1} = \text{FORWARD}(\bm{f}_{1:t}, \bm{e}_{t+1})
$$

where

- FORWARD implements the update in Equation 14.5 and
- the process begins with $\bm{f}_{1:0} = Pr(\bm{X}_0)$.

When all the state variables are discrete, the time for each update is constant (i.e., independent of $t$), and the space required is also constant. (The constants depend, of course, on the size of the state space and the specific type of the temporal model in question.)

- *The time and space requirements for updating must be constant if a finite agent is to keep track of the current state distribution indefinitely*.

## Example: Filtering in the Umbrella World


:::: {.columns}
::: {.column width="45%"}

Compute $Pr(R_2 \mid u_{1:2})$:

- Day 0: no observations, only prior beliefs: $Pr(R_0) = \langle 0.5, 0.5 \rangle$
- Day 1: umbrealla appears, $U_1 = true$.  Prediction from $t=0:1$:

    ```{=latex}
    \vspace{-.2in}
    \begin{align*}
    Pr(R_1) &= \sum_{r_0} Pr(R_1 \mid r_0) Pr(r_0) \\
            &= \langle 0.7, 0.3 \rangle \cdot 0.5 + \langle 0.3, 0.7 \rangle \cdot 0.5 \\
            &= \langle 0.5, 0.5 \rangle
    \end{align*}
    ```

    Then update step incorporates evidence for $t=1$ and normalizes:

    ```{=latex}
    \vspace{-.2in}
    \begin{align*}
    Pr(R_1 \mid u_1) &= \alpha Pr(u_1 \mid R_1) Pr(R_1) \\
                     &= \alpha \langle 0.9, 0.2 \rangle \langle 0.5, 0.5 \rangle \\
                     &= \alpha \langle 0.45, 0.1 \rangle \\
                     &\approx \langle 0.818, 0.182 \rangle
    \end{align*}
    ```

:::
::: {.column width="55%"}

```{=latex}
\vspace{-.2in}
\begin{center}
```
![](aima-fig-14_02-bayes-net-umbrella-world.pdf){height="25%"}
```{=latex}
\end{center}
```

- Day 2: umbrella appears, $U_2 = true$.  Prediction from $t=1:2$:

    ```{=latex}
    \vspace{-.2in}
    \begin{align*}
    Pr(R_2 \mid u_1) &= \sum_{r_1} Pr(R_2 \mid r_1) Pr(r_1 \mid u_1) \\
                     &= \langle 0.7, 0.3 \rangle \cdot 0.818 + \langle 0.3, 0.7 \rangle \cdot 0.182 \\
                     &\approx \langle 0.627, 0.373 \rangle
    \end{align*}
    ```

    Then update step incorporates evidence for $t=2$:

    ```{=latex}
    \vspace{-.2in}
    \begin{align*}
    Pr(R_2 \mid u_1, u_2) &= \alpha Pr(u_2 \mid R_2) Pr(R_2 \mid u_1) \\
                          &= \alpha \langle 0.9, 0.2 \rangle \langle 0.627, 0.373 \rangle \\
                          &= \alpha \langle 0.565, 0.075 \rangle \\
                          &\approx \langle 0.883, 0.117 \rangle
    \end{align*}
    ```


:::
::::


## Prediction

**Prediction** is the task of computing the posterior distribution over the future state, given all evidence to date: $Pr(\bm{X}_{t+k} \mid \bm{e}_{1:t})$ for some $k > 0$.

- Umbrella example: compute probability of rain three days from now, given all the observations to date.
- Prediction is useful for evaluating possible courses of action based on their expected outcomes.


Prediction can be seen simply as filtering without the addition of new evidence.  Filtering already includes a one-step prediciton.  So we can take Equation 14.5:

```{=latex}
\vspace{-.1in}
\[
Pr(\bm{X}_{t+1} \mid \bm{e}_{1:t+1}) = \alpha \underbrace{Pr(\bm{e}_{t+1} \mid \bm{X}_{t+1})}_{\text{sensor model}} \sum_{\bm{X}_t} \underbrace{Pr(\bm{X}_{t+1} \mid \bm{x}_t)}_{\text{transition model}} \underbrace{Pr(\bm{x}_t \mid \bm{e}_{1:t})}_{\text{recursion}} \tag{14.5}
\]
```

remove the sensor model and extend the prediction to $t + k + 1$:

```{=latex}
\vspace{-.1in}
\[
Pr(\bm{X}_{t+k+1} \mid \bm{e}_{1:t}) =  \sum_{\bm{X}_{t+k}} \underbrace{Pr(\bm{X}_{t+k+1} \mid \bm{x}_{t+k})}_{\text{transition model}} \underbrace{Pr(\bm{x}_{t+k} \mid \bm{e}_{1:t})}_{\text{recursion}} \tag{14.6}
\]
```

## Stationary Distributions

As we try to predict further and further into the future, the predicted distribution for rain converges to a fixed point $\langle 0.5,0.5 \rangle$, after which it remains constant for all time.

- This is the **stationary distribution** of the Markov process defined by the transition model.

- The **mixing time** is the time it takes to reach the fixed point.

- Prediction usually only effective for $k \ll$ mixing time.

The more the uncertainty in the transition model, the shorter will be the mixing time and the more the future is obscured.

## Smoothing

**Smoothing** is the task of computing the posterior distribution over a past state, given all evidence up to the present: $Pr(\bm{X}_k \mid \bm{e}_{1:t})$ for some $k$ such that $0 \le k < t$.


```{=latex}
\begin{center}
```
![](aima-fig-14_03-smoothing.pdf)
```{=latex}
\end{center}
```


- Umbrella example: compute the probability that it rained last Wednesday, given all the observations of the umbrella carrier made up to today.
- Smoothing provides a better estimate of the state at time $k$ than was available at that time, because it incorporates more evidence.

    - When tracking a moving object with inaccurate position observations, smoothing gives a smoother
estimated trajectory than filtering -- hence the name

## Recursive Message Passing for Smoothing

Split the computation into two parts -- the evidence up to $k$ and the evidence from $k + 1$ to $t$:

```{=latex}
\vspace{-.2in}
\begin{align*}
Pr(\bm{X}_{k} \mid \bm{e}_{1:t}) &= Pr(\bm{X}_{k} \mid \bm{e}_{1:k}, \bm{e}_{k+1:t}) \\
                                 &= \alpha Pr(\bm{X}_k \mid \bm{e}_{1:k}) Pr(\bm{e}_{k+1:t} \mid \bm{X}_k, \bm{e}_{1:k}) \tag{using Bayes' Rule, given $\bm{e}_{1:k}$} \\
                                 &= \alpha Pr(\bm{X}_k \mid \bm{e}_{1:k}) Pr(\bm{e}_{k+1:t} \mid \bm{X}_k) \tag{using conditional indepenence} \\
                                 &= \alpha \bm{f}_{1:k} \odot \bm{b}_{k+1:t} \tag{14.8}
\end{align*}
```

$\odot$ is elementwise multiplication, a.k.a. Hadamard product.

The "forward" message, $\bm{f}_{1:k}$ can be computed by filtering forward using Equation 14.5.

## Backward Message for Smoothing

The backward message, $\bm{b}_{k+1:t}$ can be computed by a recursive process that runs backward from $t$:

```{=latex}
\vspace{-.2in}
\begin{align*}
Pr(\bm{e}_{k+1:t} \mid \bm{X}_k) &= \sum_{\bm{x}_{k+1}} Pr(\bm{e}_{k+1:t} \mid \bm{X}_k, \bm{x}_{k+1}) Pr(\bm{x}_{k+1} \mid \bm{X}_k) \tag{conditioning on $\bm{X}_{k+1}$} \\
                                 &= \sum_{\bm{x}_{k+1}} Pr(\bm{e}_{k+1:t} \mid \bm{x}_{k+1}) Pr(\bm{x}_{k+1} \mid \bm{X}_k) \tag{by conditional independence} \\
                                 &= \sum_{\bm{x}_{k+1}} Pr(\bm{e}_{k+1}, \bm{e}_{k+2:t} \mid \bm{x}_{k+1}) Pr(\bm{x}_{k+1} \mid \bm{X}_k) \\
                                 &= \sum_{\bm{x}_{k+1}} \underbrace{Pr(\bm{e}_{k+1} \mid \bm{x}_{k+1})}_{sensor model} \underbrace{Pr(\bm{e}_{k+2:t} \mid \bm{x}_{k+1})}_{recursion} \underbrace{Pr(\bm{x}_{k+1} \mid \bm{X}_k)}_{transition model} \tag{14.9}
\end{align*}
```

The last step follows by the conditional independence of $\bm{e}_{k+1}$ and $\bm{e}_{k+2:t}$, given $\bm{x}_{k+1}$.

Equation 14.9 in message form is

$$
\bm{b}_{k+1:t} = \text{BACKWARD}(\bm{b}_{k+2:t}, \bm{e}_{k+1}).
$$

$\bm{e}_{t+1:t}$ is an empty sequence, so we initialize the backward phase with $\bm{b}_{t+1:t} = Pr(\bm{e}_{t+1:t} \mid \bm{X}_t) = \bm{1}$, where $\bm{1}$ is a vector of 1s.


## Example: Smoothing Umbrella World State Estimates

Beginning on Page 487

## Forward-Backward Smoothing Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-14_04-forward-backward-algorithm.pdf)
```{=latex}
\end{center}
```

## Finding the Most Likely Sequence

**Most likely explanation**: Given a sequence of observations, we might wish to find the sequence of states that is most likely to have generated those observations: $\argmax_{x_{1:t}} Pr(\bm{x}_{1:t} \mid \bm{e}_{1:t})$.

- Umbrella example: if umbrella appears on each of the first three days and is absent on the fourth, then the most likely explanation is that it rained on the first three days and did not rain on the fourth.
- MLE algorithms are useful for speech recognition -- where the aim is to find the most likely sequence of words, given a series of sounds, reconstruction of bit strings transmitted over a noisy channel, and many others.


```{=latex}
\begin{center}
```
![](aima-fig-14_05-rain-state-sequences.pdf)
```{=latex}
\end{center}
```

## Viterbi Algorithm




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

-->
