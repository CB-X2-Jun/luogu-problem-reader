# P1467 P1467 [USACO2.2] 循环数 Runaround Numbers

## 题目描述

循环数是那些不包括 $0$ 且没有重复数字的正整数（比如 $81362$），并且还应同时具有一个有趣的性质——

如果你从最左边的数字开始（在 $\color{red}{8}\color{black}1362$ 中是 $8$）向右数这个数字对应都次数（如果数到了最右边就回到最左边；在 $\color{red}{8}\color{black}1362$ 中是 $8$ 次），你会停止在另一个新的数字（在 $\color{red}{8}\color{black}1362$ 中是 $\color{red}8\color{black}\to 1\to 3\to 6\to 2\to 8\to 1\to 3\to \color{red}6$；如果停在一个相同的数字上，这个数就不是循环数）。

重复这样做，如果能在经过每个数位恰好一次后回到最左边，那么这个正整数就是循环数。

仍然以 $81362$ 为例，以下模拟过程证明了 $81362$ 是循环数：

$$\color{red}8\color{black}\to 1\to 3\to 6\to 2\to 8\to 1\to 3\to \color{red}6$$  
$$\color{red}6\color{black}\to 2\to 8\to 1\to 3\to 6\to \color{red}2$$   
$$\color{red}2\color{black}\to 8\to \color{red}1$$  
$$\color{red}1\color{black}\to \color{red}3$$  
$$\color{red}3\color{black}\to 6\to 2\to  \color{red}8$$  

**任务：**

给你一个正整数 $m$，找出最小的比 $m$ 大的循环数 $m'$。

数据保证 $m' \le 2^{32}-1$。

## 输入格式

仅仅一行, 包括 $m$。

## 输出格式

仅仅一行，输出小的比 $m$ 大的循环数 $m'$。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
81361
```

#### 样例输出 #1

```
81362
```

## 说明/提示

对于 $100\%$ 的数据，$1\le m \le 10^9$。

USACO 2.2
