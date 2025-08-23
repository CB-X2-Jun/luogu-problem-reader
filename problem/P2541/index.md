# P2541 P2541 [USACO16DEC] Robotic Cow Herd P

## 题目描述

Bessie is hoping to fool Farmer John by building a herd of $K$ realistic robotic cows ($1 \leq K \leq 100,000$).

It turns out that building a robotic cow is somewhat complicated. There are $N$ ($1 \leq n \leq 100,000$) individual locations on the robot into which microcontrollers must be connected (so a single microcontroller must be connected at each location). For each of these locations, Bessie can select from a number of different models of microcontroller, each varying in cost.

For the herd of robotic cows to look convincing to Farmer John, no two robots should behave identically. Therefore, no two robots should have exactly the same set of microcontrollers. For any pair of robots, there should be at least one location at which the two robots use a different microcontroller model. It is guaranteed that there will always be enough different microcontroller models to satisfy this constraint.

Bessie wants to make her robotic herd as cheaply as possible. Help her determine the minimum possible cost to do this!

## 输入格式

The first line of input contains $N$ and $K$ separated by a space.

The following $N$ lines contain a description of the different microcontroller models available for each location. The $i$th such line starts with $M_i$ ($1 \leq M_i \leq 10$), giving the number of models available for location $i$. This is followed by $M_i$ space separated integers $P_{i,j}$ giving the costs of these different models ($1 \le P_{i,j} \le 100,000,000$).

## 输出格式

Output a single line, giving the minimum cost to construct $K$ robots.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
3 10
4 1 5 3 10
3 2 3 3
5 1 3 4 6 6
```

#### 样例输出 #1

```
61
```
