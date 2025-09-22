---
title: Artificial Intelligence
subtitle: Logical AI
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

## Logic and AI

In AI, **knowledge-based** agents use a process of **reasoning** over an internal **representation** of knowledge to decide what actions to take.

- **Knowledge base**: a set of sentences.
- **Sentence**: an assertion about the world expressed in a **knowledge represeantation language**, like propositional logic.
- **Axioms**:  sentences taken as given -- not derived from other sentences, assumptions.
- **Inference**: deriving new sentences from old sentences.
- **Background knowledge**: sentences present in an agent's knowledge base before it starts perceiving and acting.

## Knowledge-Based Agents

- MAKE-PERCEPT-SENTENCE constructs sentence asserting that agent perceived the given percept at the given time.
- MAKE-ACTION-QUERY constructs sentence that asks what action  to take at current time.
- MAKE-ACTION-SENTENCE constructs sentence asserting chosen action was executed.

```{=latex}
\begin{center}
```
![](aima-fig-07_01-kb-agent.pdf){height="40%"}
```{=latex}
\end{center}
```

- Logical agents are described at the **knowledge level** using **declarative** statements of knowledge and goals.
- At the **implemetation level** we use a **procedureal** approach, encoding behaviors directly in program code.


## The Wumpus World

:::: {.columns}
::: {.column width="30%"}

```{=latex}
\begin{center}
```
![](aima-fig-07_02-wumpus-world.pdf){height="30%"}
```{=latex}
\end{center}
```


:::
::: {.column width="70%"}


A cave that you can drop into or climb out of at square [1, 1].

- **Performance measure**: +1000 for climbing out of the cave with the gold, –1000 for falling into a pit or being eaten by the wumpus, –1 for each action taken, –10 for using the arrow. The game ends either when the agent dies or when the agent climbs out of the cave.

:::
::::

- **Environment**: A 4×4 grid of rooms, agent always starts at [1,1], facing east. Gold and the wumpus placed uniformly randomly from the squares other than the start square. Each non-start square can be a pit with probability 0.2.

- **Actuators**: Forward, TurnLeft by $90^\circ$, or TurnRight by $90^\circ$. The agent dies if it enters pit or a live wumpus square.  Moves into walls have no effect.  Grab picks up gold if agent in gold square. Shoot can fires arrow in direction agent is facing. The arrow continues until it either hits (and hence kills) the wumpus or hits a wall. The agent has only one arrow, so only the first Shoot action has any effect. Climb climbs out of the cave if at [1,1].

## First Steps Wumpus World

- **Sensors**: The agent has five sensors, each of which gives a single bit of information:

    - In squares directly (not diagonally) adjacent to wumpus, agent perceives a Stench.
    - In squares directly adjacent to a pit, the agent perceives a Breeze.
    - In the square with gold, agent perceives a Glitter.
    - When an agent walks into a wall, it perceives a Bump.
    - When the wumpus is killed, it emits a Scream perceivable anywhere in the cave.

Percepts encoded as list of five symbols indicating presense or absence (by None) of: [Stench,Breeze,Glitter,Bump,Scream] (a bit vector).


```{=latex}
\begin{center}
```
![](aima-fig-07_03-first-step-wumpus-world.pdf){height="40%"}
```{=latex}
\end{center}
```

- (a) after percept [None,None,None,None,None]
- (b) after moving to [2,1] and perceiving [None,Breeze,None,None,None]

## Later Steps Wumpus World

```{=latex}
\begin{center}
```
![](aima-fig-07_04-later-steps-wumpus-world.pdf){height="70%"}
```{=latex}
\end{center}
```

## Logic

Basics:

- **Syntax** specifies the form of sentences.

    - $x + y = 4$ is *well-formed*, but $x4y+=$ is not.

- **Semantics** specifies the meaning of sentences.

    - $x + y = 4$ is **true** in a world where $x = 1$ and $y = 3$.

- **Model**: a formal specification of a *possible world*, that is, a set of assignments of values to the variables in the sentences of a knowledge base.

    - Given a model {$x = 3$, $y = 2$}, the sentence $x + y = 4$ is false.

Satisfaction:

- "$m$ satisfies $\alpha$": sentence $\alpha$ is true in model $m$, also "$m$ is a model of $\alpha$."
- $M(\alpha)$ the set of all models of $\alpha$, i.e., the set of all models in which $\alpha$ is true.

Entailment: $\alpha \models \beta$: $\beta$ *follows logically* from $\alpha$

Formal definition of entailment:

$$
\alpha \models \beta \text{ if and only if } M(\alpha) \subseteq M(\beta)
$$

## Possible Models of Pits in Wumpus World

The presence of pits in squares [1, 2], [2, 2] and [3, 1] gives rise to $2^3 = 8$ possible models.

```{=latex}
\begin{center}
```
![](aima-fig-07_05-possible-models-pits.pdf){height="40%"}
```{=latex}
\end{center}
```

Solid line delineates KB based on percept [None, None, None, None, None] in [1,1].

- (a). $\alpha_1$ = "There is no pit in [1, 2]."  Here, $KB \models \alpha_1$
- (b). $\alpha_2$ = "There is no pit in [2, 2]."  Here, $KB \nvDash \alpha_2$

Logical inference via model checking: because of (b), cannot conclude $\alpha_2$ (or $\neg \alpha_2$).

- $M(KB) \models \alpha_1$ but  $M(KB) \nvDash \alpha_2$

## Inference Algorithms

If an inference algorithm $i$ can derive $\alpha$ from $KB$, we write

$$
KB \vdash_i \alpha
$$

which is pronounced "$\alpha$ is derived from $KB$ by $i$" or "$i$ derives $\alpha$ from $KB$."

**Important properties of inference algorithms**:

- An inference algorithm that derives only entailed sentences is called **sound** or **truth-preserving**.

- An inference algorithm is **complete** if it can derive any sentence that is entailed.

## Representation vs World

If KB is true in the real world, then any sentence $\alpha$ derived from KB by a sound inference procedure is also true in the real world?

```{=latex}
\begin{center}
```
![](aima-fig-07_06-representation-vs-world.pdf){height="40%"}
```{=latex}
\end{center}
```

**Grounding**: connection between logical reasoning and the real environment.  How do we know that KB is true in the real world.

- Subject of volumes of philosophical investigation.
- For us: if agent perceives it, it is true.

## Propositional Logic

- **Atomic** sentences consist of a single proposition symbol.
- Proposition symbol stands for a proposition that can be true or false.

    - We use symbols that start with uppercase letter and may contain other letters or subscripts, e.g., : P, Q, R, $W_{1,3}$ and FacingEast
    - True and False have fixed meanings

- **Complex sentence**: one or more atomic sentences constructed from **logical connectives**.

- $\neg$ (not) Unary connective.  $\neg W_{1,3}$ is the **negation** of $W_{1,3}$

    - A **positive literal** is an atomic sentence.
    - a ** negative literal** is a negated atomic sentence.

- $\land$ (and).  Binary connective.  **Conjunction**, e.g., $W_{1,3} \land P_{3,1}$

- $\lor$ (or).  Binary connective.  **Disjunction**, e.g., $(W_{1,3} \land P_{3,1}) \lor W_{2,2}$

- $\implies$ (implies).  Binary connective.  **Implication**, e.g., $(W_{1,3} \land P_{3,1}) \implies \neg W_{2,2}$

    - $(W_{1,3} \land P_{3,1})$ is the **premise** or **antecedent**.
    - $\neg W_{2,2}$ is the **conclusion** or **consequent**.
    - Also known as rules or if-then statements.
    - Some authors use $\supset$ or $\rightarrow$

- $\iff$ (if and only if).  Binary connective. $W_{1,3} \iff \neg W_{2,2}$ is a **biconditional**

## Grammar of Propositional Logic

```{=latex}
\begin{center}
```
![](aima-fig-07_07-grammar-of-popositional-logic.pdf){height="70%"}
```{=latex}
\end{center}
```

## Semantics of Propositional Logic

```{=latex}
\begin{center}
```
![](aima-fig-07_08-truth-tables-logical-connectives.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Theorem Proving

So far we've done **model checking**: enumerating models and showing that the sentence must hold in all models.

Now we turn to **theorem proving**: applying rules of inference directly to the sentences in our knowledge base to construct a proof of the desired sentence without consulting models.

Some basic concepts:

- **Logical equivalence**: two sentences $\alpha$ and $\beta$ are logically equivalent if they are true in the same set of models.  $\alpha \equiv \beta$

    - $\alpha \equiv \beta$ if and only if $\alpha \models \beta$ and $\beta \models \alpha$

- **Validity**: A sentence is valid if it is true in all models. For example, the sentence $P \land \neg P$ is valid. Valid sentences are also known as **tautologies**.

**Deduction theorem**:

$$
\text{For any sentences $\alpha$ and $\beta$ }, \alpha \models \beta \text{ if and only iff the sentence } (\alpha \implies \beta) \text{ is valid.}
$$

## Inference Rules

General form:

$$
\frac{Givens}{Conclusions}
$$


Modus ponens


## Propositional Theorem Proving

```{=latex}
\begin{center}
```
![](aima-fig-07_09-truth-table-knowledge-base.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Theorem Proving

```{=latex}
\begin{center}
```
![](aima-fig-07_10-tt-entails-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Theorem Proving

```{=latex}
\begin{center}
```
![](aima-fig-07_11-logical-equivalences.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Theorem Proving

```{=latex}
\begin{center}
```
![](aima-fig-07_12-grammar-of-cnf.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Theorem Proving

```{=latex}
\begin{center}
```
![](aima-fig-07_13-pl-resolution-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Theorem Proving

```{=latex}
\begin{center}
```
![](aima-fig-07_14-pl-resolution-application.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Theorem Proving

```{=latex}
\begin{center}
```
![](aima-fig-07_15-pl-fc-entails-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Theorem Proving

```{=latex}
\begin{center}
```
![](aima-fig-07_16-horn-clauses-and-or-graph.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Model Checking

```{=latex}
\begin{center}
```
![](aima-fig-07_17-dpll-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Model Checking

```{=latex}
\begin{center}
```
![](aima-fig-07_18-walksat-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Propositional Model Checking

```{=latex}
\begin{center}
```
![](aima-fig-07_19-dpll-vs-walksat.pdf){height="70%"}
```{=latex}
\end{center}
```

## Agents Based on Propositional Logic

```{=latex}
\begin{center}
```
![](aima-fig-07_20-hybrid-wumpus-agent-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Agents Based on Propositional Logic

```{=latex}
\begin{center}
```
![](aima-fig-07_21-1-cnf-belief-state.pdf){height="70%"}
```{=latex}
\end{center}
```

## Agents Based on Propositional Logic

```{=latex}
\begin{center}
```
![](aima-fig-07_22-satplan-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

<!--

## Representation

```{=latex}
\begin{center}
```
![](aima-fig-08_01-ontological-epistemological-commitments.pdf){height="70%"}
```{=latex}
\end{center}
```

## Syntax and Semantics of First-Order Logic

```{=latex}
\begin{center}
```
![](aima-fig-08_02-person-king-model.pdf){height="70%"}
```{=latex}
\end{center}
```

## Syntax and Semantics of First-Order Logic

```{=latex}
\begin{center}
```
![](aima-fig-08_03-syntax-of-fol.pdf){height="70%"}
```{=latex}
\end{center}
```

## Syntax and Semantics of First-Order Logic

```{=latex}
\begin{center}
```
![](aima-fig-08_04-simple-example-models.pdf){height="70%"}
```{=latex}
\end{center}
```

## Syntax and Semantics of First-Order Logic

```{=latex}
\begin{center}
```
![](aima-fig-08_05-simple-example-models-database-semantics.pdf){height="70%"}
```{=latex}
\end{center}
```

## Using First-Order Logic

Foo

## Knowledge Engineering in First-Order Logic

```{=latex}
\begin{center}
```
![](aima-fig-08_06-digital-circuit.pdf){height="70%"}
```{=latex}
\end{center}
```



## Propositional vs. First-Order Logc

Foo

## Unification and First-Order Inference

```{=latex}
\begin{center}
```
![](aima-fig-09_01-unification-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Unification and First-Order Inference

```{=latex}
\begin{center}
```
![](aima-fig-09_02-subsumption-lattice.pdf){height="70%"}
```{=latex}
\end{center}
```

## Forward Chaining

```{=latex}
\begin{center}
```
![](aima-fig-09_03-fol-fc-ask-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Forward Chaining

```{=latex}
\begin{center}
```
![](aima-fig-09_04-proof-tree-fc-crime.pdf){height="70%"}
```{=latex}
\end{center}
```

## Forward Chaining

```{=latex}
\begin{center}
```
![](aima-fig-09_05-constraint-graph-australia.pdf){height="70%"}
```{=latex}
\end{center}
```

## Backward Chaining

```{=latex}
\begin{center}
```
![](aima-fig-09_06-fol-bc-ask-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Backward Chaining

```{=latex}
\begin{center}
```
![](aima-fig-09_07-proof-tree-bc-crime.pdf){height="70%"}
```{=latex}
\end{center}
```

## Logic Programming

```{=latex}
\begin{center}
```
![](aima-fig-09_08-prolog-infinite-loop.pdf){height="70%"}
```{=latex}
\end{center}
```

## Logic Programming

```{=latex}
\begin{center}
```
![](aima-fig-09_09-infinite-proof-tree.pdf){height="70%"}
```{=latex}
\end{center}
```

## Resolution

```{=latex}
\begin{center}
```
![](aima-fig-09_10-resolution-proof-criminal.pdf){height="70%"}
```{=latex}
\end{center}
```

## Resolution

```{=latex}
\begin{center}
```
![](aima-fig-09_11-resolution-proof-curiosity.pdf){height="70%"}
```{=latex}
\end{center}
```

## Completeness

```{=latex}
\begin{center}
```
![](aima-fig-09_12-structure-completeness-proof.pdf){height="70%"}
```{=latex}
\end{center}
```

## G{\"o}del's Incompleteness Theorem

Foo

## Ontological Engineering

```{=latex}
\begin{center}
```
![](aima-fig-10_01-upper-ontology-world.pdf){height="70%"}
```{=latex}
\end{center}
```

## Categories and Objects

Foo

## Events

```{=latex}
\begin{center}
```
![](aima-fig-10_02-predicates-time-intervals.pdf){height="70%"}
```{=latex}
\end{center}
```

## Fluents

```{=latex}
\begin{center}
```
![](aima-fig-10_03-schematic-object-president.pdf){height="70%"}
```{=latex}
\end{center}
```

## Mental Objects and Modal Logic

Foo

## Reasoning Systems for Categories

```{=latex}
\begin{center}
```
![](aima-fig-10_04-semantic-network-4-objects.pdf){height="70%"}
```{=latex}
\end{center}
```

## Reasoning Systems for Categories

```{=latex}
\begin{center}
```
![](aima-fig-10_05-semantic-network-assertion-fly-event.pdf){height="70%"}
```{=latex}
\end{center}
```

## Description Logics

```{=latex}
\begin{center}
```
![](aima-fig-10_06-syntax-of-classic-description-logic.pdf){height="70%"}
```{=latex}
\end{center}
```

## Reasoning with Default Information

Truth maintenance systems

-->
