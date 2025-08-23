# P2873 P2873 [USACO07DEC] Mud Puddles S

## 题目描述

Farmer John is leaving his house promptly at 6 AM for his daily milking of Bessie. However, the previous evening saw a heavy rain, and the fields are quite muddy. FJ starts at the point (0, 0) in the coordinate plane and heads toward Bessie who is located at (X, Y) (-500 ≤ X ≤ 500; -500 ≤ Y ≤ 500). He can see all N (1 ≤ N ≤ 10,000) puddles of mud, located at points (Ai, Bi) (-500 ≤ Ai ≤ 500; -500 ≤ Bi ≤ 500) on the field. Each puddle occupies only the point it is on.

Having just bought new boots, Farmer John absolutely does not want to dirty them by stepping in a puddle, but he also wants to get to Bessie as quickly as possible. He's already late because he had to count all the puddles. If Farmer John can only travel parallel to the axes and turn at points with integer coordinates, what is the shortest distance he must travel to reach Bessie and keep his boots clean? There will always be a path without mud that Farmer John can take to reach Bessie.

## 输入格式

\* Line 1: Three space-separate integers: X, Y, and N.

\* Lines 2..N+1: Line i+1 contains two space-separated integers: Ai and Bi


## 输出格式

\* Line 1: The minimum distance that Farmer John has to travel to reach Bessie without stepping in mud.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
1 2 7
0 2
-1 3
3 1
1 1
4 2
-1 1
2 2
```

#### 样例输出 #1

```
11
```
