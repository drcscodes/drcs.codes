---
title: Graph Neural Networks
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

## Graphs in the Real World

```{=latex}
\begin{center}
```
![](./GraphRealWorld.pdf)
```{=latex}
\end{center}
```

## Types of Graphs

```{=latex}
\begin{center}
```
![](./GraphTypes.pdf){height="80%"}
```{=latex}
\end{center}
```

## Graph Represenatation

```{=latex}
\begin{center}
```
![](./GraphNodeEdgeAdjacency.pdf)
```{=latex}
\end{center}
```

## Adjacency Matrices

```{=latex}
\begin{center}
```
![](./GraphAdjacencyMultiply.pdf)
```{=latex}
\end{center}
```

## Permuting Node Indices

```{=latex}
\begin{center}
```
![](./GraphNodeEquiv.pdf)
```{=latex}
\end{center}
```

## Graph Network Tasks

```{=latex}
\begin{center}
```
![](./GraphProblems.pdf){height="80%"}
```{=latex}
\end{center}
```

##  Loss Functions for Supervised Graph Problems

Supervised graph problems typically in three categories:

1. Graph-level tasks: assign label or estimate a value from the whole graph.

```{=latex}
\[
Pr(y = 1 | \bm{X}, \bm{A}) = \text{sig}( \beta_K + \frac{\bm{\omega}_K \bm{H}_K \bm{1}}{N} )
\]
```

2. Node-level tasks: assign a label or value to each node in the graph.

Loss functions are defined in the same way as for graph-level tasks, except that now this is done independently at each node n:

```{=latex}
\[
Pr(y^{(n)} = 1 | \bm{X}, \bm{A}) = \text{sig}(\beta_K + \bm{\omega}_K \bm{H}_{K}^{(n)})
\]
```


3. Edge-prediction tasks: predict the probability that an edge should exist between nodes.

Like binary classification, map node embeddings to single number representing the probability that nodes should be connected.

```{=latex}
\[
Pr(y^{(mn)} = 1 | \bm{X}, \bm{A}) = \text{sig}( \bm{h}^{(m)T} \bm{h}^{(n)}  )
\]
```


## Graph-Level Loss Functions


```{=latex}
\[
Pr(y = 1 | \bm{X}, \bm{A}) = \text{sig}( \beta_K + \frac{\bm{\omega}_K \bm{H}_K \bm{1}}{N} )
\]
```

## Node-Level Loss Functions

Loss functions are defined in the same way as for graph-level tasks, except that now this is done independently at each node n:

```{=latex}
\[
Pr(y^{(n)} = 1 | \bm{X}, \bm{A}) = \text{sig}(\beta_K + \bm{\omega}_K \bm{H}_{K}^{(n)})
\]
```

## Edge Prediction Loss Functions

Like binary classification, map node embeddings to single number representing the probability that nodes should be connected.

```{=latex}
\[
Pr(y^{(mn)} = 1 | \bm{X}, \bm{A}) = \text{sig}( \bm{h}^{(m)T} \bm{h}^{(n)}  )
\]
```


## Graph Convolutional Networks

```{=latex}
\begin{align*}
\bm{H}_1 &= \bm{F} ( \bm{X}, \bm{A}, \bm{\phi}_0 )\\
\bm{H}_2 &= \bm{F} ( \bm{H}_1, \bm{A}, \bm{\phi}_1 )\\
\bm{H}_3 &= \bm{F} ( \bm{H}_2, \bm{A}, \bm{\phi}_2 )\\
\vdots &= \vdots\\
\bm{H}_K &= \bm{F} ( \bm{H}_{K-1}, \bm{A}, \bm{\phi}_{K-1} )
\end{align*}
```

## Equivariance and Invariance

```{=latex}
\[
\bm{H}_{k+1} \bm{P} = \bm{F} ( \bm{H}_k \bm{P}, \bm{P}^T \bm{A} \bm{P}, \bm{\phi}_k )
\]
```

```{=latex}
\[
y = \text{sig}( \beta_K + \frac{\bm{\omega}_K \bm{H}_K \bm{1}}{N} ) = \text{sig}( \beta_K + \frac{\bm{\omega}_K \bm{H}_K \bm{P} \bm{1}}{N} )
\]
```

## Parameter Sharing

- Convolutional layers for images process each pixel identically
- Convolution updates variables by taking weighted sum of information from neighbors
- Could do similar for graph networks by using same parameters at every node
- Challenge: nodes have differeing numbers of neighbors

## Example Graph Convolutional Network (GCN) Layer

```{=latex}
\begin{center}
```
![](./GraphGCN.pdf){height="50%"}
```{=latex}
\end{center}
```

Aggregate information from neighboring nodes by summing their embeddings:

```{=latex}
\[
\textbf{agg} (n, k) = \sum_{m \in \text{ne}(n)} \bm{h}_k^{(m)}
\]
```

where $\text{ne}(n)$ is the set of indices of the nieghbors of node $n$.

Then apply linear transform $\bm{\Omega}_k$ to embedding $\bm{h}^{(n)}_k$, add bias $\bm{\beta}_k$ and pass through nonlinear activation function.

```{=latex}
\[
\bm{h}_{k+1}^{(n)} = \bm{a} \big( \bm{\beta}_k + \bm{\Omega}_k \cdot \bm{h}_k^{(n)} + \bm{\Omega}_k \cdot \textbf{agg} (n, k) \big)
\]
```

If we collect node embeddings into $D \times N$ matrix $\bm{H}_k$ and post-multiply by adjacency matrix $\bm{A}$, the $n^{th}$ column of this result is $\textbf{agg}(n, k)$, leading to the compact matrix formulatoin for note updates:

```{=latex}
\begin{align*}
\bm{H}_{k+1} &= \bm{a} \big( \bm{\beta}_k \bm{1}^T + \bm{\Omega}_k \bm{H}_k + \bm{\Omega}_k \bm{H}_k \bm{A} \big)\\
\bm{H}_{k+1} &= \bm{a} \big( \bm{\beta}_k \bm{1}^T + \bm{\Omega}_k \bm{H}_k ( \bm{A} + \bm{I} ) \big)
\end{align*}
```

## Example: Graph Classification

```{=latex}
\begin{align*}
\bm{H}_{1} &= \bm{a} \big( \bm{\beta}_0 \bm{1}^T + \bm{\Omega}_0 \bm{X} ( \bm{A} + \bm{I} ) \big)\\
\bm{H}_{2} &= \bm{a} \big( \bm{\beta}_1 \bm{1}^T + \bm{\Omega}_0 \bm{H}_1 ( \bm{A} + \bm{I} ) \big)\\
\vdots     &= \vdots\\
\bm{H}_{K} &= \bm{a} \big( \bm{\beta}_{K-1} \bm{1}^T + \bm{\Omega}_{K-1} \bm{H}_{K-1} ( \bm{A} + \bm{I} ) \big)\\
f ( \bm{X}, \bm{A}, \bm{\Phi} ) &= \text{sig} \big( \beta_K + \frac{\bm{\omega}_K \bm{H}_K \bm{1}}{N} \big)
\end{align*}
```

## Training with Batches

Given I training graphs $\{\bm{X}_i,\bm{A}_i\}$ and their labels $y_i$, the parameters $\bm{\Phi} = \{ \bm{\beta}_k, \bm{\Omega}_k  \}_{k=0}^K$
can be learned using SGD and the binary cross-entropy loss (equation 5.19). Fully connected networks, convolutional networks, and transformers all exploit the parallelism of modern hardware to process an entire batch of training examples concurrently. To this end, the batch elements are concatenated into a higher-dimensional tensor.  However, each graph may have a different number of nodes. Hence, the matrices Xi and Ai have different sizes, and there is no way to concatenate them into 3D tensors.

Luckily, a simple trick allows us to process the whole batch in parallel. The graphs
in the batch are treated as disjoint components of a single large graph. The network can
then be run as a single instance of the network equations. The mean pooling is carried
out only over the individual graphs to make a single representation per graph that can
be fed into the loss function.


## Inductive vs. Transductive Models

```{=latex}
\begin{center}
```
![](./GraphInductiveTransductive.pdf)
```{=latex}
\end{center}
```

## Example: Node Classification

```{=latex}
\[
f ( \bm{X}, \bm{A}, \bm{\Phi} ) = \text{sig} \big( \beta_K \bm{1}^T + \bm{\omega}_K \bm{H}_K \big)
\]
```

## Choosing Batches

```{=latex}
\begin{center}
```
![](./GraphReceptiveField.pdf)
```{=latex}
\end{center}
```

## Neighborhood Sampling

```{=latex}
\begin{center}
```
![](./GraphSampling.pdf)
```{=latex}
\end{center}
```

## Graph Partitioning

```{=latex}
\begin{center}
```
![](./GraphPartitioning.pdf)
```{=latex}
\end{center}
```

## Layers for GCNs

Approaches to both (i) the combination of the current embedding with the aggregated neighbors and (ii) the aggregation process itself.

- Combining current node and aggregated neighbors
- Residual connections
- Mean aggregation
- Kipf normalization
- Max pooling aggregation
- Aggregation by attention

## Combining Current Node and Aggregated Neighbors

In the example GCN layer above, we combined the aggregated neighbors HA with the current nodes H by just summing them:

```{=latex}
\[
\bm{H}_{k+1} = \bm{a} \big( \bm{\beta}_k \bm{1}^T + \bm{\Omega}_k \bm{H}_k ( \bm{A} + \bm{I} ) \big) \tag{13.13}
\]
```

Another option is to multiply the current node by a factor of $(1 + \epsilon_k)$, where $\epsilon_k$ is a learned scalar that is different for each layer.  This is called *diagonal enhancement*:

```{=latex}
\[
\bm{H}_{k+1} = \bm{a} \big( \bm{\beta}_k \bm{1}^T + \bm{\Omega}_k \bm{H}_k ( \bm{A} + ( 1 + \epsilon_k ) \bm{I} ) \big) \tag{13.14}
\]
```

A third option is to apply a different linear transform $\Phi_k$ to the current node:

```{=latex}
\begin{align*}
\bm{H}_{k+1} &= \bm{a} ( \bm{\beta}_k \bm{1}^T + \bm{\Omega}_k \bm{H}_k \bm{A} + \bm{\Phi}_k \bm{H}_k )\\
\bm{H}_{k+1} &= \bm{a} \big( \bm{\beta}_k \bm{1}^T + [ \bm{\Omega}_k \bm{\Phi}_k ] \genfrac{[}{]}{0pt}{}{\bm{H}_k \bm{A} }{ \bm{H}_k } \big)\\
\bm{H}_{k+1} &= \bm{a} \big( \bm{\beta}_k \bm{1}^T + \bm{\Omega'}_k \genfrac{[}{]}{0pt}{}{\bm{H}_k \bm{A} }{ \bm{H}_k } \big) \tag{13.15}
\end{align*}
```

where $\bm{\Omega'}_k = \bm{\Omega}_k \bm{\Phi}_k$.


## Residual Connections

With residual connections, the aggregated representation from the neighbors is transformed and passed through the activation function before summation or concatenation with the current node. For the latter case, the associated network equations are:

```{=latex}
\[
\bm{H}_{k+1} =  \genfrac{[}{]}{0pt}{}{ \bm{a} ( \bm{\beta}_k \bm{1}^T + \bm{\Omega}_k \bm{H}_k \bm{A} ) }{ \bm{H}_k } \tag{13.16}
\]
```

## Mean Aggregation

Average of neighbors instead of sum:

```{=latex}
\[
\textbf{agg}(n) = \frac{ 1 }{ |\text{ne}(n)| } \sum_{m \in \text{ne}(n)} \bm{h}_m \tag{13.17}
\]
```

If we introduce an $N \times N$ matrix $\bm{D}$ in which each non-zero element contains the number of neighbors for the associated node, then each diagonal element in $\bm{D}^{-1}$ contains the denominator from Equation 13.17.  Then the new GCN layer is:


```{=latex}
\[
\bm{H}_{k+1} = \bm{a} \big( \bm{\beta}_k \bm{1}^T + \bm{\Omega}_k \bm{H}_k ( \bm{A} \bm{D}^{-1} + \bm{I} ) \big) \tag{13.18}
\]
```

## Kipf Normalization

Include the current node with its neighbors.  Sum of node representations normalized as:

```{=latex}
\[
\textbf{agg}(n) = \sum_{m \in \text{ne}(n)} \frac{ \bm{h}_m }{ \sqrt{|\text{ne}(n)| |\text{ne}(m)|} }   \tag{13.19}
\]
```

The logic: information from nodes with many neighbors should be down-weighted since connections provide less unique information.

## Max Pooling Aggregation

```{=latex}
\[
\textbf{agg}(n) = \textbf{max}_{m \in \text{ne}(n)} ( \bm{h}_m ) \tag{13.21}
\]
```


## GCNs and Graph Attention Networks

The last form of aggregation we'll discuss is aggregation by attention, summarized here:

```{=latex}
\begin{center}
```
![](./GraphTransformer.pdf){height="80%"}
```{=latex}
\end{center}
```

## Edge Graphs

```{=latex}
\begin{center}
```
![](./GraphAdjoint.pdf)
```{=latex}
\end{center}
```

## Closing Thoughts

Boom!
