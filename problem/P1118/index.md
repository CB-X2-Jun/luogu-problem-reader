# P1118 P1118 [USACO06FEB] Backward Digit Sums G/S

## 题目描述

`FJ` and his cows enjoy playing a mental game. They write down the numbers from $1$ to$ N(1 \le N  \le 10)$ in a certain order and then sum adjacent numbers to produce a new list with one fewer number.  They repeat this until only a single number is left.  For example, one instance of the game (when $N=4$) might go like this:

```cpp
    3   1   2   4
      4   3   6
        7   9
         16
```
Behind `FJ`'s back, the cows have started playing a more difficult game, in which they try to determine the starting sequence from only the final total and the number $N$.  Unfortunately, the game is a bit above `FJ`'s mental arithmetic capabilities.


Write a program to help `FJ` play the game and keep up with the cows.



## 输入格式

Line 1: Two space-separated integers: N and the final sum.

## 输出格式

Line 1: An ordering of the integers 1..N that leads to the given sum. If there are multiple solutions, choose the one that is lexicographically least, i.e., that puts smaller numbers first.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 16
```

#### 样例输出 #1

```
3 1 2 4
```

## 说明/提示

- For $40\%$ of the data, $1\le n\le 7$;
- For $80\%$ of the data, $1\le n \le 10$;
- For $100\%$ of the data, $1\le n \le 12$, $1\le sum\le 12345$.
