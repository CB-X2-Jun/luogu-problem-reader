# P3139 P3139 [USACO16FEB] Milk Pails S

## 题目描述

Farmer John has received an order for exactly $M$ units of milk ($1 \leq M \leq 200$) that he needs to fill right away.  Unfortunately, his fancy milking machine has just become broken, and all he has are two milk pails of integer sizes $X$ and $Y$ ($1 \leq X, Y \leq 100$) with which he can measure milk.  Both pails are initially empty.  Using these two pails, he can perform up to $K$ of the following types of operations ($1 \leq K \leq 100$):

- He can fill either pail completely to the top.

- He can empty either pail.

- He can pour the contents of one pail into the other, stopping when the former becomes empty or the latter becomes full (whichever of these happens first).

Although FJ realizes he may not be able to end up with exactly $M$ total units of milk in the two pails, please help him compute the minimum amount of error between $M$ and the total amount of milk in the two pails.  That is, please compute the minimum value of $|M-M'|$ such that FJ can construct $M'$ units of milk collectively between the two pails.

## 输入格式

The first, and only line of input, contains $X$, $Y$, $K$, and $M$.


## 输出格式

Output the smallest distance from $M$ to an amount of milk FJ can produce.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
14 50 2 32
```

#### 样例输出 #1

```
18
```

## 说明/提示

In two steps FJ can be left with the following quanities in his pails


```cpp
(0, 0) = 0 units
(14, 0) = 14 units
(0, 50) = 50 units
(0, 14) = 14 units
(14, 36) = 50 units
(14, 50) = 64 units
```

The closest we can come to 32 units is 14 for a difference of 18.  Note that it would require an extra step to pour out the first pail to end up with (0, 36).

