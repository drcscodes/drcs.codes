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
![](./GraphTypes.pdf)
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
![](./GraphProblems.pdf)
```{=latex}
\end{center}
```

## Graph-Level Loss Functions

```{=latex}
\[
Pr(y = 1 | \bm{X}, \bm{A}) = \text{sig}( \beta_K + \frac{\bm{\omega}_K \bm{H}_K \bm{1}}{N} )
\]
```

## Node-Level Loss Functions

```{=latex}
\[
Pr(y^{(n)} = 1 | \bm{X}, \bm{A}) = \text{sig}(\beta_K + \bm{\omega}_K \bm{H}_{K}^{(n)})
\]
```

## Edge Prediction Loss Functions

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
![](./GraphGCN.pdf)
```{=latex}
\end{center}
```

```{=latex}
\[
\textbf{agg} (n, k) = \sum_{m \in \text{ne}(n)} \bm{h}_k^{(m)}
\]
```

```{=latex}
\[
\bm{h}_{k+1}^{(n)} = \bm{a} \big( \bm{\beta}_k + \bm{\Omega}_k \cdot \bm{h}_k^{(n)} + \bm{\Omega}_k \cdot \textbf{agg} (n, k) \big)
\]
```

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

## Choosing Bitches

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

```{=latex}
\[
\bm{H}_{k+1} &= \bm{a} \big( \bm{\beta}_k \bm{1}^T + \bm{\Omega}_k \bm{H}_k ( \bm{A} + \bm{I} ) \big)
\]
```

```{=latex}
\[
\bm{H}_{k+1} &= \bm{a} \big( \bm{\beta}_k \bm{1}^T + \bm{\Omega}_k \bm{H}_k ( \bm{A} + ( 1 + \epsilon_k ) \bm{I} ) \big)
\]
```


## Residual Connections

## Mean Aggregation

## Kipf Normalization

## Max Pooling Aggregation

## Aggregation by Attention


## GCNs and Graph Attention Networks

```{=latex}
\begin{center}
```
![](./GraphTransformer.pdf)
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
