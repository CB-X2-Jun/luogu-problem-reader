# P2910 P2910 [USACO08OPEN] Clear And Present Danger S

## 题目描述

Farmer John is on a boat seeking fabled treasure on one of the $N (1 \le N \le 100)$ islands conveniently labeled $1 \sim N$ in the Cowribbean Sea.

The treasure map tells him that he must travel through a certain sequence $A_1, A_2, \dots, A_M$ of $M (2 \le M \le 10^4)$ islands, starting on island $1$ and ending on island $N$ before the treasure will appear to him. He can visit these and other islands out of order and even more than once, but his trip must include the $A_i$ sequence in the order specified by the map.

FJ wants to avoid pirates and knows the pirate-danger rating $(0 \le danger \le 10^5)$ between each pair of islands. The total danger rating of his mission is the sum of the danger ratings of all the paths he traverses.

Help Farmer John find the least dangerous route to the treasure that satisfies the treasure map's requirement.

## 输入格式

Line $1$: Two space-separated integers: $N$ and $M$.

Lines $2 \sim M+1$: Line $i+1$ describes the $i$-th island FJ must visit with a single integer: $A_i$.

Lines $M+2\sim N+M+1$: Line $i+M+1$ contains $N$ space-separated integers that are the respective danger rating of the path between island i and islands $1, 2, \dots$, and $N$, respectively. The ith integer is always zero.

## 输出格式

Line $1$: The minimum danger that Farmer John can encounter while obtaining the treasure.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
3 4 
1 
2 
1 
3 
0 5 1 
5 0 2 
1 2 0
```

#### 样例输出 #1

```
7
```

## 说明/提示

There are $3$ islands and the treasure map requires Farmer John to visit a sequence of $4$ islands in order: island $1$, island $2$, island $1$ again, and finally island $3$. The danger ratings of the paths are given: the paths $(1, 2); (2, 3); (3, 1)$ and the reverse paths have danger ratings of $5, 2$, and $1$, respectively.


He can get the treasure with a total danger of $7$ by traveling in the sequence of islands $1, 3, 2, 3, 1$, and $3$. The cow map's requirement ($1, 2, 1$, and $3$) is satisfied by this route. We avoid the path between islands $1$ and $2$ because it has a large danger rating.
