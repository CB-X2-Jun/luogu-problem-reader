# P3558 P3558 [POI 2013] BAJ-Bytecomputer

## 题目描述

A sequence of $n$ integers $x_1,x_2,\cdots,x_n$ from the set $\{-1, 0, 1\}$ is given. The bytecomputer is a device that allows the following operation on the sequence: incrementing $x_{i + 1}$ by $x_i$ for any $1\leq i\leq n$. There is no limit on the range of integers the bytecomputer can store, i.e., each $x_i$ can (in principle) have arbitrarily small or large value.

Program the bytecomputer so that it transforms the input sequence into a non - decreasing sequence (i.e., such that $x_1\leq x_2\leq\cdots\leq x_n$) with the minimum number of operations.

## 输入格式

The first line of the standard input holds a single integer $n$ ($1\leq n\leq1000000$), the number of elements in the (bytecomputer's) input sequence.

The second line contains $n$ integers $x_1,x_2,\cdots,x_n$ ($x_i\in\{-1, 0, 1\}$) that are the successive elements of the (bytecomputer's) input sequence, separated by single spaces.

In tests worth 24% of the total points it holds that $n\leq500$, and in tests worth 48% of the total points it holds that $n\leq10000$.

## 输出格式

The first and only line of the standard output should give one integer, the minimum number of operations the bytecomputer has to perform to make its input sequence non - decreasing, or the single word BRAK (Polish for *none*) if obtaining such a sequence is impossible. 

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
6
-1 1 0 -1 0 1
```

#### 样例输出 #1

```
3
```
