# P1797 P1797 【模板】Stern-Brocot 树

## 题目背景

这是一道模板题。（[来源](https://judge.yosupo.jp/problem/stern_brocot_tree)）

为了帮小圆打败魔女之夜，你需要回答 Stern-Brocot 树上的询问。

## 题目描述


约定：

- 本题中，输入/输出的所有分数都必须是既约的。
- 本题中，输入的分数 $\dfrac{p}{q}$ 都满足 $1\le p,q\le 10^9$。



### Task 1：ENCODE_PATH

- 输入格式：`ENCODE_PATH` $p$ $q$；
- 输出格式：$k$ $n_1$ $c_1$ $n_2$ $c_2$ $\cdots$ $n_k$ $c_k$

给定分数 $\dfrac{p}{q}$，你需要按照以下格式输出从 Stern-Brocot 树根走到节点 $\dfrac{p}{q}$ 的路径：

> $k$ $c_1$ $n_1$ $c_2$ $n_2$ $\cdots$ $c_k$ $n_k$

其中 $c_i\in \{\texttt{L},\texttt{R}\}$ 表示走到左儿子或者右儿子，$n_i$ 表示重复 $c_i$ 操作几次。

你需要保证 $\forall 1\le i\lt k$，$c_i\neq c_{i+1}$。

### Task 2：DECODE_PATH

- 输入格式：`DECODE_PATH` $k$ $n_1$ $c_1$ $n_2$ $c_2$ $\cdots$ $n_k$ $c_k$
- 输出格式：$p$ $q$。

给定从 Stern-Brocot 树根出发的路径，格式如 Task 1 所述，输出节点上的分数。

保证答案满足 $1\le p,q\le 10^9$。

### Task 3：LCA

给定 $\dfrac{a}{b},\dfrac{c}{d}$，输出 $\dfrac{a}{b},\dfrac{c}{d}$ 的 LCA 上的分数 $\dfrac{p}{q}$。


- 输入格式：`LCA` $a$ $b$ $c$ $d$；
- 输出格式：$p$ $q$。

### Task 4：ANCESTOR

给定 $\dfrac{a}{b},k$，输出 $\dfrac{a}{b}$ 到根的链上，深度为 $k$ 的节点 $\dfrac{p}{q}$ 的值。如果不存在，输出 $-1$。


- 输入格式：`ANCESTOR` $k$ $a$ $b$；
- 输出格式：$p$ $q$。
- 数据范围：$1\le k\le 10^9$。

### Task 5：RANGE

给定 $\dfrac{p}{q}$，记在 Stern-Brocot 树中，$\dfrac{p}{q}$ 的子树中的所有分数构成的集合为 $S$。输出 $\inf S=\dfrac{a}{b}$ 和 $\sup S=\dfrac{c}{d}$。

特别地，对于 $0$，输出 $0$ $1$；对于 $+\infty$，输出 $1$ $0$。

- 输入格式：`RANGE` $p$ $q$；
- 输出格式：$a$ $b$ $c$ $d$。


## 输入格式

第一行，一个正整数 $T$，表示数据组数；

接下来 $T$ 行，每行若干个整数描述一个任务，格式见【题目描述】。

## 输出格式

输出 $T$ 行，表示对应任务的答案，格式见【题目描述】。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
10
DECODE_PATH 0
DECODE_PATH 3 R 2 L 1 R 2
ENCODE_PATH 1 1
ENCODE_PATH 5 11
LCA 2 3 3 5
LCA 5439 19294 8291 29410
ANCESTOR 10 1 1
ANCESTOR 300 1000000000 1
RANGE 1 1
RANGE 11 8
```

#### 样例输出 #1

```
1 1
11 4
0
2 L 2 R 4
2 3
148 525
-1
301 1
0 1 1 0
4 3 7 5
```

## 说明/提示

- $1\le T\le 10^5$；
- 输入的所有分数都是既约的；
- 输入的分数 $\dfrac{p}{q}$ 都满足 $1\le p,q\le 10^9$。



