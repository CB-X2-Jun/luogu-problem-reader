# P1607 P1607 [USACO09FEB] Fair Shuttle G

## 题目描述

Although Farmer John has no problems walking around the fair to collect prizes or see the shows, his cows are not in such good shape; a full day of walking around the fair leaves them exhausted. To help them enjoy the fair, FJ has arranged for a shuttle truck to take the cows from place to place in the fairgrounds.

FJ couldn't afford a really great shuttle, so the shuttle he rented traverses its route only once (!) and makes N (1 <= N <= 20,000) stops (conveniently numbered 1..N) along its path. A total of K (1 <= K <= 50,000) groups of cows conveniently numbered 1..K wish to use the shuttle, each of the M\_i (1 <= M\_i <= N) cows in group i wanting to ride from one stop S\_i (1 <= S\_i < E\_i) to another stop E\_i (S\_i < E\_i <= N) farther along the route.

The shuttle might not be able to pick up an entire group of cows (since it has limited capacity) but can pick up partial groups as appropriate.

Given the capacity C (1 <= C <= 100) of the shuttle truck and the descriptions of the groups of cows that want to visit various sites at the fair, determine the maximum number of cows that can ride the shuttle during the fair.


## 输入格式

The first line: contains three integers: $K, N$ and $C$, separated by spaces.

The second line to the $K+1$ line: in the $i+1$ line, it will tell you the information of the $i$th group of cows: $S_i, E_i$ and $M_i$, separated by spaces.

## 输出格式

First row: The maximum number of cows that can take the bus.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
8 15 3
1 5 2
13 14 1
5 8 3
8 14 2
14 15 1
9 12 1
12 15 2
4 6 1
```

#### 样例输出 #1

```
10
```

## 说明/提示

The shuttle bus can take $2$ cows from $1$ to $5$, $3$ cows from $5$ to $8$, $2$ cows from $8$ to $14$, $1$ cows from $9$ to $12$, $1$ cows from $13$ to $14$, and $1$ cows from $14$ to $15$.
