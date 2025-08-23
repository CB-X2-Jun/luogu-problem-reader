# P2945 P2945 [USACO09MAR] Sand Castle S

## 题目描述

Farmer John has built a sand castle! Like all good castles, the walls have crennelations, that nifty pattern of embrasures (gaps) and merlons (filled spaces); see the diagram below. The N (1 <= N <= 25,000) merlons of his castle wall are conveniently numbered 1..N; merlon i has height M\_i (1 <= M\_i <= 100,000); his merlons often have varying heights, unlike so many.

He wishes to modify the castle design in the following fashion: he has a list of numbers B\_1 through B\_N (1 <= B\_i <= 100,000), and wants to change the merlon heights to those heights B\_1, ..., B\_N in some order (not necessarily the order given or any other order derived from the data).

To do this, he has hired some bovine craftsmen to raise and lower the merlons' heights. Craftsmen, of course, cost a lot of money. In particular, they charge FJ a total X (1 <= X <= 100) money per unit height added and Y (1 <= Y <= 100) money per unit height

reduced.

FJ would like to know the cheapest possible cost of modifying his sand castle if he picks the best permutation of heights. The answer is guaranteed to fit within a 32-bit signed integer.

Note: about 40% of the test data will have N <= 9, and about 60% will have N <= 18.

## 输入格式

\* Line 1: Three space-separated integers: N, X, and Y

\* Lines 2..N+1: Line i+1 contains the two space-separated integers: M\_i and B\_i


## 输出格式

\* Line 1: A single integer, the minimum cost needed to rebuild the castle


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
3 6 5 
3 1 
1 2 
1 2
```

#### 样例输出 #1

```
11
```

## 说明/提示

FJ's castle starts with heights of 3, 1, and 1. He would like to change them so that their heights are 1, 2, and 2, in some order. It costs 6 to add a unit of height and 5 to remove a unit of height.


FJ reduces the first merlon's height by 1, for a cost of 5 (yielding merlons of heights 2, 1, and 1). He then adds one unit of height to the second merlon for a cost of 6 (yielding merlons of heights 2, 2, and 1).

