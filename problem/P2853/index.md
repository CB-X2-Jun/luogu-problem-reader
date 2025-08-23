# P2853 P2853 [USACO06DEC] Cow Picnic S

## 题目描述

The cows are having a picnic! Each of Farmer John's K (1 ≤ K ≤ 100) cows is grazing in one of N (1 ≤ N ≤ 1,000) pastures, conveniently numbered 1...N. The pastures are connected by M (1 ≤ M ≤ 10,000) one-way paths (no path connects a pasture to itself).

The cows want to gather in the same pasture for their picnic, but (because of the one-way paths) some cows may only be able to get to some pastures. Help the cows out by figuring out how many pastures are reachable by all cows, and hence are possible picnic locations.

## 输入格式

Line 1: Three space-separated integers, respectively: K, N, and M

Lines 2..K+1: Line i+1 contains a single integer (1..N) which is the number of the pasture in which cow i is grazing.

Lines K+2..M+K+1: Each line contains two space-separated integers, respectively A and B (both 1..N and A != B), representing a one-way path from pasture A to pasture B.

## 输出格式

Line 1: Three space-separated integers, respectively: K, N, and M

Lines 2..K+1: Line i+1 contains a single integer (1..N) which is the number of the pasture in which cow i is grazing.

Lines K+2..M+K+1: Each line contains two space-separated integers, respectively A and B (both 1..N and A != B), representing a one-way path from pasture A to pasture B.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
2 4 4
2
3
1 2
1 4
2 3
3 4
```

#### 样例输出 #1

```
2
```

## 说明/提示

The cows can meet in pastures 3 or 4.
