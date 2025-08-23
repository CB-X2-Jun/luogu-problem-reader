# P2918 P2918 [USACO08NOV] Buying Hay S

## 题目描述

Farmer John is running out of supplies and needs to purchase H (1 <= H <= 50,000) pounds of hay for his cows.

He knows N (1 <= N <= 100) hay suppliers conveniently numbered 1..N. Supplier i sells packages that contain P\_i (1 <= P\_i <= 5,000) pounds of hay at a cost of C\_i (1 <= C\_i <= 5,000) dollars. Each supplier has an unlimited number of packages available, and the packages must be bought whole.

Help FJ by finding the minimum cost necessary to purchase at least H pounds of hay.

约翰的干草库存已经告罄，他打算为奶牛们采购 $H(1 \leq H \leq 50000)$ 磅干草。

他知道 $N(1 \leq N\leq 100)$ 个干草公司，现在用 $1$ 到 $N$ 给它们编号。第 $i$ 公司卖的干草包重量为 $P_i (1 \leq P_i \leq 5,000)$ 磅，需要的开销为 $C_i (1 \leq C_i \leq 5,000)$ 美元。每个干草公司的货源都十分充足， 可以卖出无限多的干草包。

帮助约翰找到最小的开销来满足需要，即采购到至少 $H$ 磅干草。

## 输入格式

\* Line 1: Two space-separated integers: N and H

\* Lines 2..N+1: Line i+1 contains two space-separated integers: P\_i and C\_i

第 $1$ 行：两个整数： $N$ 与 $H$ ，以空格分隔。

第 $2$ 行至第 $N+1$ 行：其中第 $i+1$ 行包含两个整数： $P_i$ 与 $C_i$ ，以空格分隔。

## 输出格式

\* Line 1: A single integer representing the minimum cost FJ needs to pay to obtain at least H pounds of hay.

一个整数，表示 FJ 至少采购到 $H$ 磅干草所需的最少花费。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
2 15 
3 2 
5 3
```

#### 样例输出 #1

```
9
```

## 说明/提示

FJ can buy three packages from the second supplier for a total cost of 9.

FJ 可以在第二家公司买 $3$ 包干草，共花费 $9$ 美元。
