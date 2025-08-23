# P3005 P3005 [USACO10DEC] The Trough Game S

## 题目描述

Farmer John and Bessie are playing games again. This one has to do with troughs of water.

Farmer John has hidden N (1 <= N <= 20) troughs behind the barn, and has filled some of them with food. Bessie has asked M (1 <= M <= 100) questions of the form, 'How many troughs from this list (which she recites) are filled?'.

Bessie needs your help to deduce which troughs are actually filled.

Consider an example with four troughs where Bessie has asked these questions (and received the indicated answers):

1) 'How many of these troughs are filled: trough 1' -->  1 trough is filled

2) 'How many of these troughs are filled: troughs 2 and 3' -->  1 trough is filled

3) 'How many of these troughs are filled: troughs 1 and 4' -->  1 trough is filled

4) 'How many of these troughs are filled: troughs 3 and 4' -->  1 trough is filled

From question 1, we know trough 1 is filled.

From question 3, we then know trough 4 is empty. 

From question 4, we then know that trough 3 is filled. 

From question 2, we then know that trough 2 is empty. 

Farmer John 和 Bessie 在玩一个游戏。

Farmer John 准备了 $n$ 个槽（$1\le n\le20$），其中一些槽中藏有食物。Bessie 为了知道哪些槽中有食物，会询问 $m$ 个形如“第 $x_1\cdots x_k$ 号槽中是否有食物？”的问题（$1\le m\le100,1\le k\le n$）。

请你帮忙求出哪几个槽中有食物。




## 输入格式

\* Line 1: Two space-separated integers: N and M

\* Lines 2..M+1: A subset of troughs, specified as a sequence of contiguous N 0's and 1's, followed by a single integer that is the number of troughs in the specified subset that are filled.

第一行包含两个整数 $n,m$，分别表示槽的个数和 Bessie 询问的问题数。

接下来 $m$ 行每行包含一个长度为 $n$ 的 $01$ 序列和一个整数 $t$，其中 $01$ 序列中的 $1$ 表示询问中提到了这个位置的槽，$t$ 表示这些槽中有 $t$ 份食物。


## 输出格式

\* Line 1: A single line with:

\* The string 'IMPOSSIBLE' if there is no possible set of filled troughs compatible with Farmer John's answers.

\* The string 'NOT UNIQUE' if Bessie cannot determine from the given data exactly what troughs are filled.

\* Otherwise, a sequence of contiguous N 0's and 1's specifying which troughs are filled.



输出共一行。

若无解，则输出 `IMPOSSIBLE`。

若不止一个解，则输出 `NOT UNIQUE`。

若有唯一解，则输出一个 $01$ 序列，其中 $1$ 表示这个位置的槽中有食物。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 4 
1000 1 
0110 1 
1001 1 
0011 1
```

#### 样例输出 #1

```
1010
```

## 说明/提示

### 样例解释
四个序列分别表示如下对话：

1. 问：在第一个槽中有多少个槽里有食物？——答：$1$ 个。
2. 问：在第二个和第三个槽中有多少个槽里有食物？——答：$1$ 个。
3. 问：在第一个和第四个槽中有多少个槽里有食物？——答：$1$ 个。
4. 问：在第三个和第四个槽中有多少个槽里有食物？——答：$1$ 个。

从第一个问题可以知道，第一个槽是有食物的。

从第三个问题可以知道，第四个槽是没有食物的。

从第四个问题可以知道，第三个槽是有食物的。

从第二个问题可以知道，第二个槽是没有食物的。
