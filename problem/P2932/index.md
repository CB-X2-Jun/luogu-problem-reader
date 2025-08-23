# P2932 P2932 [USACO09JAN] Earthquake Damage G

## 题目描述

Wisconsin has had an earthquake that has struck Farmer John's farm! The earthquake has damaged some of the pastures so that they are unpassable. Remarkably, none of the cowpaths was damaged.

As usual, the farm is modeled as a set of $P(1 \le P \le 30,000)$ pastures conveniently numbered $1\ldots P$ which are connected by a set of $C (1 \le C \le 100,000)$ non-directional cowpaths conveniently numbered $1\ldots C$. Cowpath $i$ connects pastures $a_i$ and $b_i (1 \le a_i \le P; 1 \le b_i \le P)$. Cowpaths might connect $a_i$ to itself or perhaps might connect two pastures more than once.  The barn is located in pasture $1$.

A total of $N (1 \le N \le P)$ cows (in different pastures) sequentially contact Farmer John via moobile phone with an integer message $report_j (2 \le report_j \le P)$ that indicates that pasture $report_j$ is undamaged but that the calling cow is unable to return to the barn from pasture $report_j$ because she could not find a path that does not go through damaged pastures.

After all the cows report in, determine the minimum number of pastures (including ones that are uncrossable) from which it is not possible to return to the barn.

Note: Feedback on some of the test data will be provided on the first $50$ submissions.

## 输入格式

Line $1$: Three space-separated integers: $P$,$C$,and $N$.

Lines $2\ldots C+1$: Line $i+1$ describes cowpath $i$ with two integers: $a_i$ and $b_i$.

Lines $C+2\ldots C+N+1$: Line $C+1+j$ contains a single integer: $report_j$.


## 输出格式

Line $1$: A single integer that is the minimum count of pastures from which a cow can not return to the barn (including the damaged pastures themselves)


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 3 1 
1 2 
2 3 
3 4 
3
```

#### 样例输出 #1

```
3
```

## 说明/提示

Pasture $2$ is damaged, resulting in cows in pastures $2, 3, 4$ not being able to return to the barn.
