# P2739 P2739 [USACO4.4] 棋盘游戏 Shuttle Puzzle

## 题目描述

大小为 $3$ 的棋盘游戏里有 $3$ 个白色棋子，$3$ 个黑色棋子，和一个有 $7$ 个格子一线排开的木盒子。$3$ 个白棋子被放在一头，$3$ 个黑棋子被放在另一头，中间的格子空着。
- 初始状态：`WWW_BBB`（`_` 代表空格）
- 目标状态：`BBB_WWW`

在这个游戏里有两种移动方法是允许的：
- 你可以把一个棋子移到与它相邻的空格；
- 你可以把一个棋子跳过一个(仅一个)与它不同色的棋子到达空格。

大小为 $N$ 的棋盘游戏包括 $N$ 个白棋子，$N$ 个黑棋子，还有有 $2N+1$ 个格子的木盒子。

这里是大小为 $3$ 的棋盘游戏的解，包括初始状态，中间状态和目标状态：

`WWW_BBB` $\rightarrow$ `WW_WBBB` $\rightarrow$ `WWBW_BB` $\rightarrow$ `WWBWB_B` $\rightarrow$ `WWB_BWB` $\rightarrow$ `W_BWBWB` $\rightarrow$ `_WBWBWB` $\rightarrow$ `BW_WBWB` $\rightarrow$ `BWBW_WB` $\rightarrow$ `BWBWBW_` $\rightarrow$ `BWBWB_W` $\rightarrow$ `BWB_BWW` $\rightarrow$ `B_BWBWW` $\rightarrow$ `BB_WBWW` $\rightarrow$ `BBBW_WW` $\rightarrow$ `BBB_WWW`

请编一个程序求解大小为 $N$ 的棋盘游戏（$1 \le N \le 12$）。要求用最少的移动步数实现。

## 输入格式

一个正整数 $N$，表示棋盘游戏的大小。

## 输出格式

输出用每一步移动的棋子移动前在棋盘的位置（位置从左到右依次为 $1,2,\dots,2N+1$）表示的序列，每个数字之间以空格分隔，每行 $20$ 个数（最后一行可以少于 $20$ 个数）。

输出的解还应当有最小的字典顺序，即如果有多组移动步数最小的解，输出第一个数最小的解；如果还有多组，输出第二个数最小的解，以此类推。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
3
```

#### 样例输出 #1

```
3 5 6 4 2 1 3 5 7 6 4 2 3 5 4
```

## 说明/提示

题目翻译来自 NOCOW。

USACO Training Section 4.3
