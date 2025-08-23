# P3479 P3479 [POI 2009] GAS-Fire Extinguishers

## 题目背景




## 题目描述

Byteasar has had a new palace built. It consists of $n$ chambers and $n-1$ corridors connecting them. Each corridor connects exactly two chambers. The rooms are numbered from $1$ to $n$. There is only a single entrance to the palace, which leads to chamber no. $1$). For each chamber there is exactly one route leading to it from the entrance, without turning back on the way. In other words, the chambers and the corridors form a tree - a connected acyclic graph.

The fire marshal who is to approve the building demands placing fire extinguishers inside.

The following are his exact requirements:

- The fire extinguishers should be placed in (some) chambers, and one chamber  may store any number of extinguishers.
- Each chamber has to be assigned one fire extinguisher, though it may be stored  in another chamber.
- Each fire extinguisher can be assigned to at most $S$ different chambers.
- For each room its assigned extinguisher is within the range of $K$ corridors.

Byteasar has a week spot for lavish palaces, so it is no surprise he has very little money now, right after completion of another splendid palace.

Therefore he is interested in the minimum number of fire extinguishers sufficient  for satisfying fire marshal's demands.



## 输入格式

The first line of the standard input contains three integers $n$, $s$ and $k$ separated by single spaces, $1\le n\le 10^5$, $1\le s\le n$, $1\le k\le 20$.

Each of the following $n-1$ lines holds two integers separated by a single space.

Line no. $i+1$ contains the numbers $x_i,y_i$ denoting the corridor connecting chambers no.$x_i$ and $y_i$.

## 输出格式

The first and only line of the standard output is to hold one integer - the minimum number of fire extinguishers that have to be installed in palace.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
12 3 1
1 12
3 8
7 8
8 9
2 12
10 12
9 12
4 8
5 8
8 11
6 8
```

#### 样例输出 #1

```
4
```

## 说明/提示

$1\leq n,m\leq 100000, 1\leq k \leq 20 , x_i\geq 1$
