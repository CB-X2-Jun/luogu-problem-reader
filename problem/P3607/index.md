# P3607 P3607 [USACO17JAN] Subsequence Reversal P

## 题目描述

Farmer John is arranging his $N$ cows in a line to take a photo ($1 \leq N \leq 50$). The height of the $i$th cow in sequence is $a(i)$, and Farmer John thinks it would make for an aesthetically pleasing photo if the cow lineup has a large increasing subsequence of cows by height.

To recall, a subsequence is a subset $a(i_1), a(i_2), \ldots, a(i_k)$ of elements from the cow sequence, found at some series of indices $i_1 < i_2 < \ldots < i_k$. We say the subsequence is increasing if $a(i_1) \leq a(i_2) \leq \ldots \leq a(i_k)$.

FJ would like there to be a long increasing subsequence within his ordering of the cows. In order to ensure this, he allows himself initially to choose any subsequence and reverse its elements.

For example, if we had the list

```
1 6 2 3 4 3 5 3 4
```

We can reverse the chosen elements

```
1 6 2 3 4 3 5 3 4
  ^         ^ ^ ^
```
to get

```
1 4 2 3 4 3 3 5 6
  ^         ^ ^ ^
```
Observe how the subsequence being reversed ends up using the same indices as it initially occupied, leaving the other elements unchanged.

Please find the maximum possible length of an increasing subsequence, given that you can choose to reverse an arbitrary subsequence once.

## 输入格式

The first line of input contains $N$. The remaining $N$ lines contain $a(1) \ldots a(N)$, each an integer in the range $1 \ldots 50$.

## 输出格式

Output the number of elements that can possibly form a longest increasing subsequence after reversing the contents of at most one subsequence.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
9
1
2
3
9
5
6
8
7
4
```

#### 样例输出 #1

```
9
```
