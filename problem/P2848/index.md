# P2848 P2848 [USACO16DEC] Cow Checklist G

## 题目描述

Every day, Farmer John walks through his pasture to check on the well-being ofeach of his cows. On his farm he has two breeds of cows, Holsteins and Guernseys. His $H$ Holsteins are conveniently numbered $1 \ldots H$, and his $G$ Guernseys are conveniently numbered $1 \ldots G$($1 \leq H \leq 1000, 1 \leq G \leq 1000$). Each cow is located at a point inthe 2D plane (not necessarily distinct).

Farmer John starts his tour at Holstein 1, and ends at Holstein $H$.  He wantsto visit each cow along the way, and for convenience in maintaining hischecklist of cows visited so far, he wants to visit the Holsteins and Guernseysin the order in which they are numbered. In the sequence of all $H+G$ cows hevisits, the Holsteins numbered $1 \ldots H$ should appear as a (not necessarilycontiguous) subsequence, and likewise for the Guernseys. Otherwise stated, thesequence of all $H+G$ cows should be formed by  interleaving the list ofHolsteins numbered $1 \ldots H$ with the list of Guernseys numbered $1 \ldots G$.

When FJ moves from one cow to another cow traveling a distance of $D$, heexpends $D^2$ energy.  Please help him determine the minimum amount of energyrequired to visit all his cows according to a tour as described above.

## 输入格式

The first line of input contains $H$ and $G$, separated by a space.

The next $H$ lines contain the $x$ and $y$ coordinates of the $H$ Holsteins, and the next $G$ lines after that contain coordinates of the Guernseys. Each coordinate is an integer in the range $0 \ldots 1000$.


## 输出格式

Write a single line of output, giving the minimum energy required for FJ's tour of all the cows.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
3 2
0 0
1 0
2 0
0 3
1 3
```

#### 样例输出 #1

```
20
```
