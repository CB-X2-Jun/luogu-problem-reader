# P3145 P3145 [USACO16OPEN] Splitting the Field G

## 题目描述

Farmer John's $N$ cows ($3 \leq N \leq 50,000$) are all located at distinct positions in his two-dimensional field.  FJ wants to enclose all of the cows with a rectangular fence whose sides are parallel to the x and y axes, and hewants this fence to be as small as possible so that it contains every cow (cowson the boundary are allowed).

FJ is unfortunately on a tight budget due to low milk production last quarter.He would therefore like to enclose a smaller area to reduce maintenance costs,and the only way he can see to do this is by building two enclosures instead of one.  Please help him compute how much less area he needs to enclose, in total,by using two enclosures instead of one. Like the original enclosure, the two enclosures must collectively contain all the cows (with cows on boundaries allowed), and they must have sides parallel to the x and y axes.  The two enclosures are not allowed to overlap -- not even on their boundaries. Note that enclosures of zero area are legal, for example if an enclosure has zero width and/or zero height.

## 输入格式

The first line of input contains $N$.  The next $N$ lines each contain two integers specifying the location of a cow. Cow locations are positive integers in the range $1 \ldots 1,000,000,000$.

## 输出格式

Write a single integer specifying amount of total area FJ can save by using two enclosures instead of one.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
6
4 2
8 10
1 1
9 12
14 7
2 3
```

#### 样例输出 #1

```
107
```
