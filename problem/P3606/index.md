# P3606 P3606 [USACO17JAN] Building a Tall Barn P

## 题目描述

Farmer John is building a brand new, $N$-story barn, with the help of his $K$ cows ($1 \leq N \leq K \leq 10^{12}$ and $N \leq 10^5$). To build it as quickly as possible, he needs your help to figure out how to allocate work among the cows.

Each cow must be assigned to work on exactly one specific floor out of the $N$ total floors in the barn, and each floor must have at least one cow assigned to it. The $i$th floor requires $a_i$ units of total work, and each cow completes one unit of work per hour, so if $c$ cows work on floor $i$, it will be completed in $a_i / c$ units of time. For safety reasons, floor $i$ must be completed before construction can begin on floor $i+1$.

Please compute the minimum total time in which the barn can be completed, if the cows are allocated to work on floors in an optimal fashion. Output this number rounded to the nearest integer; it is guaranteed that the solution will be more than 0.1 from the boundary between two integers.

## 输入格式

The first line of input contains $N$ and $K$.

The next $N$ lines contain $a_1 \ldots a_N$, each a positive integer of size at most $10^{12}$.

## 输出格式

Please output the minimum time required to build the barn, rounded to the

nearest integer.



## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
2 5
10
4
```

#### 样例输出 #1

```
5
```
