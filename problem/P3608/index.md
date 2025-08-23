# P3608 P3608 [USACO17JAN] Balanced Photo G

## 题目描述

Farmer John is arranging his $N$ cows in a line to take a photo ($1 \leq N \leq 100,000$). The height of the $i$th cow in sequence is $h_i$, and the heights of all cows are distinct.

As with all photographs of his cows, FJ wants this one to come out looking as nice as possible. He decides that cow $i$ looks "unbalanced" if $L_i$ and $R_i$ differ by more than factor of 2, where $L_i$ and $R_i$ are the number of cows taller than $i$ on her left and right, respectively. That is, $i$ is unbalanced if the larger of $L_i$ and $R_i$ is strictly more than twice the smaller of these two numbers. FJ is hoping that not too many of his cows are unbalanced.

Please help FJ compute the total number of unbalanced cows.



## 输入格式

The first line of input contains $N$.  The next $N$ lines contain $h_1 \ldots h_N$, each a nonnegative integer at most 1,000,000,000.



## 输出格式

Please output a count of the number of cows that are unbalanced.



## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
7
34
6
23
0
5
99
2
```

#### 样例输出 #1

```
3
```
