# P1940 P1940 Reversible Number

## 题目背景

本题改编自 Project Euler Problem 145：

> Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
>
> There are 120 reversible numbers below one-thousand.
>
> How many reversible numbers are there below one-billion (10^x)?

## 题目描述

有些正整数 $n$ 可能满足 $n+\text{rev}(n)$（$\text{rev}(n)$ 是把 $n$ 倒过来写所得的数）得到的结果的各位都是奇数。

比方说：

- $n=36$ 时，$36+63=99$。
- $n=409$ 时，$409+904=1313$。

规定满足上述的 $n$ 称为 Reversible 数。所以 $36,63,409,904$ 都是 Reversible 数。

当然，以 $0$ 开头的数统统不算 Reversible 数。

那么，小于等于 $10^x$ 的 Reversible 数有多少个？

## 输入格式

一个正整数 $x$。

## 输出格式

一行一个整数，表示答案。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4
```

#### 样例输出 #1

```
720
```

## 说明/提示

对于 $30\%$ 的数据，保证答案不大于 $2^{32}-1$。

对于 $100\%$ 的数据，$3 \le x \le 400$。
