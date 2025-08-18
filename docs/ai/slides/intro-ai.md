---
title: Artificial Intelligence
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

## These people are wrong.

```{=latex}
\begin{center}
```
![](./sam-altman-double-polo.jpg){height="25%"}
![](./dario-amodei.jpg){height="25%"}
![](./geoff-hinton.jpg){height="25%"}
![](./eric-schmidt.jpg){height="25%"}
![](./elon-musk.jpg){height="25%"}
```{=latex}
\end{center}
```

To be fair, there are many, many people who are wrong about AI.  But you probably recognize these guys.

- The emergence of "human-level AI" has been "just a few years away" since 1956.  All of these predictions have been wrong.

*Why does it matter that they're wrong?*

## We are decades, perhaps centuries away from "solving" AI.

- AI is immature.
- Currently, unfortunately, overhyped.

```{=latex}
\begin{center}
```
See my advisor's advisor's dated predictions:

![](rodney-brooks.jpg){height=30%}

https://rodneybrooks.com/my-dated-predictions/
```{=latex}
\end{center}
```

- Most of the truly groundbreaking discoveries in AI are yet to be made.

```{=latex}
\vspace{.25in}
\begin{center}
\LARGE{This makes AI exciting!}
\end{center}
```

## What does this mean for us?

- If most of the breakthroughs are yet to be made, then

    - *we don't even have the right **paradigm** yet*.

- Many AI courses focus on *the current thing*, focusing on statistical machine learning, and neural networks in particular.

    - This does a disservice to students!

- This course the full spectrum of AI so that you're ready to spot and develop promising new directions.

    - We'll spend little time on machine learning, and barely touch on neural networks.

        - We have entire courses for those subjects!

## What is AI?

:::: {.columns}
::: {.column width="50%"}

```{=latex}
\begin{center}
```
![](./simon1996sciences-cover.jpg){height="60%"}[^simon1996sciences]
```{=latex}
\end{center}
```

:::
::: {.column width="50%"}


Artificial

- Man-made.  Syntehetic.

Intelligence

- Problem solving
- Inference
- Decision making
- Learning

Rationality

- Doing the right thing.

:::
::::

[^simon1996sciences]: https://mitpress.mit.edu/9780262691918/the-sciences-of-the-artificial/

## Four Approaches to AI

Decompose AI into thinking and acting, and define standards of performance as fidelity to humans and quanitative rationality.


```{=latex}
\begin{tabular}{lr|cc}\\
     &          & \multicolumn{2}{c}{Standard} \\
     &          & Humanly  & Rationally \\\hline
Mode & Acting   & Acting humanly & Acting rationally \\
     & Thinking & Thinking humanly & Thinking rationally \\
\end{tabular}
```

## Acting humanly

Turing test

- Natural language processing
- Knowledge representation
- Automated reasoning
- Machine learning

Total Turing test

- Computer vision
- Robotics

Nobody cares about Turing tests.

## Rationality

"Doing the right thing."

- Acting rationally - goal maximizing behavior

    - Choosing actions which reach goals with minimal cost
    - Choosing actions which maximize a payoff relative to other agents
    - Choosing actions which maximize long-term expected reward

- Thinking rationally - "laws of thought"

    - Logic
    - Probabilistic inference


> Thinking is nothing more than acting in an imagined space.
>
> -- Konrad Lorenz via Bernhard Schölkopf


## Foundations of AI

- Philosophy
- Mathematics
- Neuroscience
- Psychology
- Computer Engineering
- Control theory and cybernetics
- Linguistics

Such a rich tapestry!

## Philosophy

- Can formal rules be used to draw valid conclusions?
- How does the mind arise from a physical brain?
- Where does knowledge come from?
- How does knowledge lead to action?

## Mathematics

- What are the formal rules to draw valid conclusions?
- What can be computed?
- How do we reason with uncertain information?

- Logic
- Probability and statistics
- Algorithms, computability and complexity
- Optimization


## Economics

Acting rationally

- How should we make decisions in accordance with our preferences?
- How should we do this when others may not go along?
- How should we do this when the payoff may be far in the future?

## Neuroscience

How do brains process information?

![](./aima-fig-01_02-computers-vs-brains.pdf){height="50%"}

## Psychology

How do humans and animals think and act?

- Cognitive modeling
- Behaviorism

    - Operant conditioning
    - "Reinforcement learning"

## Computer Engineering

How can we build an efficient computer?

- High performance computing

    - Today's LLMs take years of compute time to train.

- Quantum computing

## Control theory and cybernetics

How can artifacts operate under their own control?

![](Power-Relay-6.jpg){height="50%"}

[DARPA POWER Program](https://www.darpa.mil/research/programs/power)

## Impact of AI

Turing award winners:

- Marvin Minsky (1969)
- John McCarthy (1971)
- Allen Newell and Herbert Simon (1975)
- Ed Feigenbaum and Raj Reddy (1994)
- Judea Pearl (1994)
- Yoshua Bengio, Geoffrey Hinton, and Yann LeCun (2019)
- Rich Sutton and Andrew Barto (2024)

AI lament: once an AI problem is solved, it's no longer considered AI.

## History of AI

- MucCulloch, Pitts, Hebb (1943-1949)

    - Perceptrons
    - Hebbian learning

- 1956 Dartmouth AI Workshop

    - Organized by John McCarthy, Marvin Minsky, Claude Shannon, Nathaniel Rochester
    - Attendees: Allen Newell and Herbert Simon from Carnegie Tech, Trenchard More from Princeton, Arthur Samuel from IBM, and Ray Solomonoff and Oliver Selfridge from MIT
    - Logic Theorist

- Symbolic AI (1952-1969)

    - Lisp

- First AI Winter (1966-1973)

    - Lighthill report (Lighthill, 1973) -- British government ended most AI funding

- Expert Systems (1969-1986)

- Second AI Winter (1986)

    - Experts systems failed to deliver on their inventors' promises.
    - Knowledge acquisition bottleneck.
    - Adaptability, brittleness.

## Modern AI

- Return of neural networks (1986-present)

    - Symolism vs Connectionism
    - Geoff Hinton, et. al.

- Probabilistic reasoning and machine learning (1987-present)

    - Neats vs scruffies
    - "Physics envy"

- Big data (2001-present)

    - Large data sets -- don't fit on a single machine

- Deep learning (2011-present)

    - You may have heard of it?

## Future of AI

:::: {.columns}
::: {.column width="30%" valign="top" halign="center"}

![](andrew-barto.jpg){height="30%}

[Andrew Barto](https://people.cs.umass.edu/~barto/)

:::
::: {.column width="30%" valign="top"}

![](rich-sutton.jpg){height="30%}
[Rich Sutton](http://incompleteideas.net/)

:::
::: {.column width="30%" valign="top"}

![](david-silver.jpg){height="30%}
[David Silver](https://davidstarsilver.wordpress.com/)

:::
::::

[The Era of Experience](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf)
