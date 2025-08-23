# P3052 P3052 [USACO12MAR] Cows in a Skyscraper G

## 题目描述

A little known fact about Bessie and friends is that they love stair climbing races.  A better known fact is that cows really don't like going down stairs.  So after the cows finish racing to the top of their favorite skyscraper, they had a problem.  Refusing to climb back down using the stairs, the cows are forced to use the elevator in order to get back to the ground floor.

The elevator has a maximum weight capacity of $W$ ($1 <= W <= 100,000,000$) pounds and cow $i$ weighs $C_i$ ($1 <= C_i <= W$) pounds.  Please help Bessie figure out how to get all the N ($1 <= N <= 18$) of the cows to the ground floor using the least number of elevator rides.  The sum of the weights of the cows on each elevator ride must be no larger than W.

## 输入格式

\* Line $1$: $N$ and $W$ separated by a space.

\* Lines $2$ ~ $N+1$: Line $i+1$ contains the integer $C_i$, giving the weight of one of the cows.

## 输出格式

\* A single integer, $R$, indicating the minimum number of elevator rides needed.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 10 
5 
6 
3 
7
```

#### 样例输出 #1

```
3
```

## 说明/提示

There are four cows weighing 5, 6, 3, and 7 pounds.  The elevator has a maximum weight capacity of 10 pounds.


We can put the cow weighing 3 on the same elevator as any other cow but the other three cows are too heavy to be combined.  For the solution above, elevator ride 1 involves cow #1 and #3, elevator ride 2 involves cow #2, and elevator ride 3 involves cow #4.  Several other solutions are possible for this input.
