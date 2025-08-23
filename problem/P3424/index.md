# P3424 P3424 [POI 2005] SUM-Fibonacci Sums

## 题目描述

Fibonacci numbers are an integer sequence defined in the following way: $Fib_0=1$, $Fib_1=1$, $Fib_i=Fib_{i-1}+Fib_{i-2}$ (for $i\ge 2$). The first few numbers in this sequence are: ($1,1,2,3,5,8,\cdots$).

The great computer scientist Byteazar is constructing an unusual computer, in which numbers are represented in Fibonacci system i.e. a bit string $(b_1,b_2,\cdots,b_n)$ denotes the number $b_1\cdot Fib_1+b_2\cdot Fib_2+\cdots+b_n\cdot Fib_n$. (Note that we do not use $Fib_0$.) Unfortunately, such a representation is ambiguous i.e. the same number can have different representations. The number $42$, for instance, can be written as: $(0,0,0,0,1,0,0,1)$, $(0,0,0,0,1,1,1,0)$ or $(1,1,0,1,0,1,1)$. For this very reason, Byteazar has limited himself to only using representations satisfying the following conditions:

if $n>1$, then $b_n=1$, i.e. the representation of a number does not contain leading zeros.

if $b_i=1$, then $b_{i+1}=0$ (for $i=1,\cdots,n-1$), i.e. the representation of a number does not contain two (or more) consecutive ones.

The construction of the computer has proved more demanding than Byteazar supposed. He has difficulties implementing addition. Help him!

TaskWrite a programme which:

reads from the standard input the representations of two positive integers,calculates and writes to the standard output the representation of their sum.

## 输入格式

The input contains the Fibonacci representations (satisfying the aforementioned conditions) of two positive integers $x$ and $y$ - one in the first, the other in the second line. Each of these representations is in the form of a sequence of non-negative integers, separated by single spaces. The first number in the line denotes the length of the representation $n$, $1\le n\le 1\ 000\ 000$. It is followed by $n$ zeros and/or ones.


## 输出格式

In the first and only line of the output your programme should write the Fibonacci representation (satisfying the aforementioned conditions) of the sum $x+y$. The representation should be in the form of a sequence of non-negative integers, separated by single spaces, as it has been described in the Input section. The first number in the line denotes the length of the representation $n$, $1\le n\le 1\ 000\ 000$. It is followed by $n$ zeros and/or ones.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 0 1 0 1
5 0 1 0 0 1
```

#### 样例输出 #1

```
6 1 0 1 0 0 1
```
