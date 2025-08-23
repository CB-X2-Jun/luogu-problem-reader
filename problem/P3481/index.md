# P3481 P3481 [POI 2009] PRZ-Algorithm Speedup

## 题目描述

As a punishment for misbehaving, Byteasar is to calculate a certain mysterious and nasty Boolean-valued function $F(x,y)$, which is defined for a pair of positive integer sequences $x=(x_1,x_2,\cdots,x_n)$, $y=(y_1,y_2,\cdots,y_n)$ as follows:

- boolean $F(x, y)$
- if $W(x)\neq W(y)$ then return $0$ 
- else if $|W(x)|=|W(y)|=1$ then return $1$
- else return $F(p(x), p(y)) \wedge F(s(x), s(y))$.

Where:

- $W(x)$ denotes the set of members of the sequence $x$ (order and repetitions of elements are insignificant),
- $p(x)$ denotes the longest prefix (initial part of any length) of the sequence $x$, such that $W(x)\neq W(p(x))$,
- $s(x)$ denotes the longest suffix (final part of any length) of the sequence $x$, such that $W(x)\neq W(s(x))$,
- $\wedge$ denotes the logical conjunction, $1$ - true, $0$ - false,      and $|z|$ - cardinality of set $z$.

For example, for the sequence $x=(2,3,7,2,7,4,7,2,4)$ we have: $W(x)=\{2,3,4,7\}$, $p(x)=(2,3,7,2,7)$, $s(x)=(7,2,7,4,7,2,4)$. For very large data a programme calculating values of the function $F$ directly from definition is too slow by any standards. Therefore you are to make these calculations as fast as possible.

Write a programme that reads several pairs of sequences $(x,y)$ from the standard input and    prints out the values $F(x,y)$ on the standard output for every input pair.



## 输入格式

The first line of the standard input contains one integer $k$ ($1\le k\le 13$) denoting the number of sequence pairs to analyse.

Next $3k$ line hold descriptions of test cases.

The first line of each description contains two integers $n$ and $m$ ($1\le n,m\le 100{,}000$) separated by a single space and denoting the lengths of the first and second sequence, respectively.

The second line holds $n$ integers $x_i$ ($1\le x_i\le 100$) that form the sequence $x$, separated by single spaces.

The third line holds $m$ integers $y_i$ ($1\le y_i\le 100$),    that form the sequence $y$, separated by single spaces.


## 输出格式

The output should consist of exactly $k$ lines; the $i$-th line (for $1\le i\le k$) should contain a single integer - 0 or 1 - the value of $F(x, y)$ for $i$-th test case.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
2
4 5
3 1 2 1
1 3 1 2 1
7 7
1 1 2 1 2 1 3
1 1 2 1 3 1 3
```

#### 样例输出 #1

```
0
1
```
