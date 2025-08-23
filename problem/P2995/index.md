# P2995 P2995 [USACO10NOV] Cow Photographs G

## 题目描述

Farmer John wants to take a picture of his entire herd of N (1 <= N <= 100,000) cows conveniently numbered 1..N so he can show off to his friends.

On picture day, the cows run to form a single line in some arbitrary order with position i containing cow c\_i (1 <= c\_i <= N). Farmer John has his own ideas about how the cows should line up.

FJ thinks cow i may stand only to the left of cow i+1 (for all i, 1 <= i <= N-1) and that cow N may only stand to the left of Cow 1. Of course, no cow will stand to the left of the first (leftmost) cow in the line.

The cows are hungry for the promised post-photo dinner, so Farmer John wants to take the picture as quickly as possible. Cows are not great at following directions, so he will only choose a pair of adjacent cows and have them switch places once per minute. How quickly is Farmer John able to get them into some acceptable order?

Consider a set of 5 cows whose initial lineup looks like this:

Left           Right

3  5  4  2  1

He can first swap the second pair of cows:

3  4  5  2 1

and then swap the rightmost pair: 

3  4  5  1  2

to yield an acceptable lineup that required but two minutes of cow swapping.


## 输入格式

\* Line 1: A single integer: N

\* Lines 2..N+1: Line i+1 contains the number of the i-th cow in line: c\_i


## 输出格式

\* Line 1: The minimum amount of time, in minutes, that it takes Farmer John to get the cows into some appropriate order.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
5 
3 
5 
4 
2 
1
```

#### 样例输出 #1

```
2
```
