# P3661 P3661 [USACO17FEB] Why Did the Cow Cross the Road I S

## 题目描述

Farmer John's cows are trying to learn to cross the road effectively. Remembering the old "why did the chicken cross the road?" joke, they figure the chickens must be experts on crossing the road, and go off in search of chickens to help them.

As it turns out, chickens are very busy creatures and have limited time to help the cows. There are $C$ chickens on the farm ($1 \leq C \leq 20,000$), conveniently numbered $1 \ldots C$, and each chicken $i$ is only willing to help a cow at precisely time $T_i$. The cows, never in a hurry, have more flexibility in their schedules. There are $N$ cows on the farm ($1 \leq N \leq 20,000$), conveniently numbered $1 \ldots N$, where cow $j$ is able to cross the road between time $A_j$ and time $B_j$. Figuring the "buddy system" is the best way to proceed, each cow $j$ would ideally like to find a chicken $i$ to help her cross the road; in order for their schedules to be compatible, $i$ and $j$ must satisfy $A_j \leq T_i \leq B_j$.

If each cow can be paired with at most one chicken and each chicken with at most one cow, please help compute the maximum number of cow-chicken pairs that can be constructed.

## 输入格式

The first line of input contains $C$ and $N$. The next $C$ lines contain $T_1 \ldots T_C$, and the next $N$ lines contain $A_j$ and $B_j$ ($A_j \leq B_j$) for $j = 1 \ldots N$. The $A$'s, $B$'s, and $T$'s are all non-negative integers (not necessarily distinct) of size at most 1,000,000,000

## 输出格式

Please compute the maximum possible number of cow-chicken pairs.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
5 4
7
8
6
2
9
2 5
4 9
0 3
8 13
```

#### 样例输出 #1

```
3
```
