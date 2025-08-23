# P3538 P3538 [POI 2012] OKR-A Horrible Poem

## 题目描述

Byteie boy has to learn a fragment of a certain poem by heart. The poem, following the best lines of modern art, is a long string consisting of lowercase English alphabet letters only. Obviously, it sounds horrible, but that is the least of Byteie's worries. First and foremost, he completely forgot which fragment is he supposed to learn. And they all look quite difficult to memorize...

There is hope, however: some parts of the poem exhibit certain regularity. In particular, every now and then a fragment, say $A$, is but a multiple repetition of another fragment, say $B$ (in other words, $A = BB\cdots B$, i.e., $A = B^k$, where $k\geq1$ is an integer). In such case we say that $B$ is a full period of $A$ (in particular, every string is its own full period). If a given fragment has a short full period, Byteie's task will be easy. The question remains... which fragment was that?

Make a gift for Byteie - write a program that will read the whole poem as well as a list of fragments that Byteie suspects might be the one he is supposed to memorize, and for each of them determines its shortest full period.

## 输入格式

In the first line of the standard input there is a single integer $n$ ($1\leq n\leq500,000$). In the second line there is a string of length $n$ consisting of lowercase English alphabet letters - the poem. We number the positions of its successive characters from $1$ to $n$.

The next line holds a single integer $q$ ($1\leq q\leq2,000,000$) denoting the number of fragments. Then the following $q$ lines give queries, one per line. Each query is a pair of integers $a_i$ and $b_i$ ($1\leq a_i\leq b_i\leq n$), separated by a single space, such that the answer to the query should be the length of the shortest full period of the poem's fragment that begins at position $a_i$ and ends at position $b_i$.

In tests worth in total 42% of the points $n\leq10,000$ holds in addition. In some of those, worth 30% of points in total, $q\leq10,000$ holds as well.

## 输出格式

Your program should print $q$ lines on the standard output. The $i$ - th of these lines should hold a single integer - the answer to the $i$ - th query. 

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
8
aaabcabc
3
1 3
3 8
4 8
```

#### 样例输出 #1

```
1
3
5
```
