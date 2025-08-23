# P2879 P2879 [USACO07JAN] Tallest Cow S

## 题目描述

FJ's $N(1 \le N \le 10,000)$ cows conveniently indexed $1 \ldots N$ are standing in a line. Each cow has a positive integer height (which is a bit of secret). You are told only the height $H(1 \le H \le 1,000,000)$ of the tallest cow along with the index I of that cow.

FJ has made a list of $R(0 \le R \le 10,000)$ lines of the form "cow 17 sees cow 34". This means that cow 34 is at least as tall as cow 17, and that every cow between 17 and 34 has a height that is strictly smaller than that of cow 17.

For each cow from $1 \ldots N$, determine its maximum possible height, such that all of the information given is still correct. It is guaranteed that it is possible to satisfy all the constraints.

## 输入格式

Line $1$: Four space-separated integers: $N, I, H$ and $R$


Lines $2 \ldots R+1$: Two distinct space-separated integers $A$ and $B(1 \le A, B \le N)$, indicating that cow $A$ can see cow $B$.

## 输出格式

Lines $1 \ldots N$: Line $i$ contains the maximum possible height of cow $i$.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
9 3 5 5
1 3
5 3
4 3
3 7
9 8
```

#### 样例输出 #1

```
5
4
5
3
4
4
5
5
5
```
