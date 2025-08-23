# P3498 P3498 [POI 2010] KOR-Beads

## 题目描述

Byteasar once decided to start manufacturing necklaces.

He subsequently bought a very long string of colourful coral beads for a bargain price.

Byteasar now also has a machine that, for a given ![](http://main.edu.pl/images/OI17/kor-en-tex.1.png) (![](http://main.edu.pl/images/OI17/kor-en-tex.2.png)), can cut the string    into pieces (or substrings) of ![](http://main.edu.pl/images/OI17/kor-en-tex.3.png) coral beads (i.e., the first piece consists of the beads no.

![](http://main.edu.pl/images/OI17/kor-en-tex.4.png), the second of ![](http://main.edu.pl/images/OI17/kor-en-tex.5.png), etc.).

If the length of the string (measured in coral beads) is not a multiple of ![](http://main.edu.pl/images/OI17/kor-en-tex.6.png),    then the last piece is not used, as it has length smaller than ![](http://main.edu.pl/images/OI17/kor-en-tex.7.png).

From now on we denote the colours of the beads with positive integers.

Byteasar, always praising diversity, wonders how he should choose the number ![](http://main.edu.pl/images/OI17/kor-en-tex.8.png)    in order to get as many different substrings as possible.

The ends of the long string that will be cut are different: there are specific    beginning and ending (rather than two interchangeable endpoints), and the machine    of course starts cutting at the beginning. On the other hand, in the substrings    obtained from cutting the endpoints are interchangeable, and so the substrings    can be reversed. In other words, the substrings ![](http://main.edu.pl/images/OI17/kor-en-tex.9.png) and ![](http://main.edu.pl/images/OI17/kor-en-tex.10.png) are    identical to us. Write a program that determines the optimum value of ![](http://main.edu.pl/images/OI17/kor-en-tex.11.png) for Byteasar.

## 输入格式

In the first line of the standard input there is an integer ![](http://main.edu.pl/images/OI17/kor-en-tex.37.png)      (![](http://main.edu.pl/images/OI17/kor-en-tex.38.png)) denoting the length of the string to cut.

In the second line there are ![](http://main.edu.pl/images/OI17/kor-en-tex.39.png) positive integers ![](http://main.edu.pl/images/OI17/kor-en-tex.40.png)      (![](http://main.edu.pl/images/OI17/kor-en-tex.41.png)), separated by single spaces, that denote      the colours of successive beads in Byteasar's string.


## 输出格式

Two integers, separated by a single space, should be printed out to the first line of the standard ouput:

the (maximum) number of different substrings that can be obtained with an optimal choice    of parameter ![](http://main.edu.pl/images/OI17/kor-en-tex.42.png), and the number ![](http://main.edu.pl/images/OI17/kor-en-tex.43.png) of such optimal values of ![](http://main.edu.pl/images/OI17/kor-en-tex.44.png).

The second line should contain ![](http://main.edu.pl/images/OI17/kor-en-tex.45.png) integers separated by single spaces:

the values of parameter ![](http://main.edu.pl/images/OI17/kor-en-tex.46.png) that yield an optimum solution;    these can be given in arbitrary order.

输出两行，第一行第一个数为最多可以得到的不同子串的个数，第二个数为取到最优解时的不同的k的个数。第二行包含若干个数，为取到最优解时的不同的k 。第二行中的不同的k可以按任意位置输出。


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
21
1 1 1 2 2 2 3 3 3 1 2 3 3 1 2 2 1 3 3 2 1
```

#### 样例输出 #1

```
6 1
2
```

## 说明/提示

$1≤n≤2\times 10^5$，且 $\forall 1\le i\le n$，有 $1\le a_i\le n$
