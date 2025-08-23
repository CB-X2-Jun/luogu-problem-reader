# P2061 P2061 [USACO07OPEN] City Horizon S

## 题目描述

Farmer John has taken his cows on a trip to the city! As the sun sets, the cows gaze at the city horizon and observe the beautiful silhouettes formed by the rectangular buildings.

The entire horizon is represented by a number line with N (1 ≤ N ≤ 40,000) buildings. Building i's silhouette has a base that spans locations Ai through Bi along the horizon (1 ≤ Ai < Bi ≤ 1,000,000,000) and has height Hi (1 ≤ Hi ≤ 1,000,000,000). Determine the area, in square units, of the aggregate silhouette formed by all N buildings.


## 输入格式

Line 1: A single integer: N
Lines 2..N+1: Input line i+1 describes building i with three space-separated integers: A_i, B_i, and H_i

## 输出格式

Line 1: The total area, in square units, of the silhouettes formed by all N buildings

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4
2 5 1
9 10 4
6 8 2
4 6 3
```

#### 样例输出 #1

```
16
```

## 说明/提示

N<=40000 , a、b、k<=10^9 。

