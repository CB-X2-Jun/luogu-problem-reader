# P3184 P3184 [USACO16DEC] Counting Haybales S

## 题目描述

Farmer John has just arranged his $N$ haybales ($1 \leq N \leq 100,000$) at various points along the one-dimensional road running across his farm.  To make sure they are spaced out appropriately, please help him answer $Q$ queries ($1 \leq Q \leq 100,000$), each asking for the number of haybales within a specific interval along the road.

## 输入格式

The first line contains $N$ and $Q$.

The next line contains $N$ distinct integers, each in the range $0 \ldots 1,000,000,000$, indicating that there is a haybale at each of those locations.

Each of the next $Q$ lines contains two integers $A$ and $B$($0 \leq A \leq B \leq 1,000,000,000$) giving a query for the number of haybales between $A$ and $B$, inclusive.

## 输出格式

You should write $Q$ lines of output.  For each query, output the number of haybales in its respective interval.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 6
3 2 7 5
2 3
2 4
2 5
2 7
4 6
8 10
```

#### 样例输出 #1

```
2
2
3
4
1
0
```
