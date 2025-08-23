# P3000 P3000 [USACO10DEC] Cow Calisthenics G

## 题目描述

Farmer John 为了保持奶牛们的健康，让可怜的奶牛们不停在牧场之间的小路上奔跑。这些奶牛的路径集合可以被表示成一个点集和一些连接两个顶点的双向路，使得每对点之间恰好有一条简单路径。简单的说来， 这些点的布局就是一棵树，且每条边等长，都为 $1$。

对于给定的一个奶牛路径集合，精明的奶牛们会计算出任意点对路径的最大值， 我们称之为这个路径集合的直径。如果直径太大，奶牛们就会拒绝锻炼。

Farmer John 把每个点标记为 $1\cdots V(2\le V\le 10^5)$。为了获得更加短的直径，他可以选择封锁一些已经存在的道路，这样就可以得到更多的路径集合， 从而减小一些路径集合的直径。我们从一棵树开始，Farmer John 可以选择封锁 $S(1\le S\le V-1)$ 条双向路，从而获得 $S+1$个路径集合。

你要做的是计算出最佳的封锁方案，使得他得到的所有路径集合直径的最大值尽可能小。Farmer John 告诉你所有 $V-1$ 条双向道路，每条表述为：顶点 $A_i(1\le A_i\le V)$ 和 $B_i(1\le B_i\le V,A_i\ne B_i)$ 连接。

## 输入格式

第 $1$ 行：两个空格分隔的整数：$V$ 和 $S$，

第 $2$ 到 $V$ 行：两个空格分隔的整数：$A_i$ 和 $B_i$。

## 输出格式

一个整数，这是 FJ 用 $s$ 块可以实现的最佳最大路径长度

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
7 2 
6 7 
3 4 
6 5 
1 2 
3 2 
4 5
```

#### 样例输出 #1

```
2
```

## 说明/提示

Consider this rather linear cowpath set (a tree with 7 vertices):

1---2---3---4---5---6---7

If FJ can block two paths, he might choose them to make a map like this:

1---2 | 3---4 | 5---6---7 where the longest pathlength is 2, which would be the answer in this case. He can do no better than this.
