# P2925 P2925 [USACO08DEC] Hay For Sale S

## 题目描述

Farmer John suffered a terrible loss when giant Australian cockroaches ate the entirety of his hay inventory, leaving him with nothing to feed the cows. He hitched up his wagon with capacity $C$ ($1\le C\le 50000$) cubic units and sauntered over to Farmer Don's to get some hay before the cows miss a meal.

Farmer Don had a wide variety of $H$ ($1\le H\le 5000$) hay bales for sale, each with its own volume ($1\le V_i\le C$). Bales of hay, you know, are somewhat flexible and can be jammed into the oddest of spaces in a wagon.

FJ carefully evaluates the volumes so that he can figure out the largest amount of hay he can purchase for his cows.

Given the volume constraint and a list of bales to buy, what is the greatest volume of hay FJ can purchase?  He can't purchase partial bales, of course. Each input line (after the first) lists a single bale FJ can buy.

## 输入格式

\* Line $1$: Two space-separated integers: $C$ and $H$;

\* Lines $2\dots H+1$: Each line describes the volume of a single bale: $V_i$.

## 输出格式

\* Line $1$: A single integer which is the greatest volume of hay FJ can purchase given the list of bales for sale and constraints.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
7 3 
2 
6 
5
```

#### 样例输出 #1

```
7
```

## 说明/提示

The wagon holds $7$ volumetric units; three bales are offered for sale with volumes of $2$, $6$, and $5$ units, respectively.


Buying the two smaller bales fills the wagon.
