# P2017 P2017 [USACO09DEC] Dizzy Cows G

## 题目描述

The cows have taken to racing each other around the farm but they get very dizzy when running in circles, and everyone knows that dizzy cows don't produce any milk. Farmer John wants to convert all of the two-way cow paths in the farm to one-way paths in order to eliminate any 'cycles' and prevent the cows from getting dizzy.  A 'cycle' enables a cow to traverse one or more cow paths and arrive back at her starting point, thus completing a loop or circle.

The farm comprises N pastures (1 <= N <= 100,000) conveniently numbered 1..N. M1 (1 <= M1 <= 100,000) one-way cow paths and M2 two-way cow paths (1 <= M2 <= 100,000) connect the pastures. No path directly connects a pasture to itself, although multiple paths might connect two different pastures. A cow may or may not be able to travel between any two given pastures by following a sequence of cow paths.

Your job is to assign a direction to the two-way cow paths such that the entire farm (ultimately with only one-way paths) has no cycles. That is, there should be no sequence of one-way cow paths which leads back to its starting position. The existing one-way cow paths do not form a cycle and should be left as they are.

One-way cow paths run from pasture A\_i (1 <= A\_i <= N) to pasture B\_i (1 <= B\_i <= N). Two-way cow paths connect pastures X\_i (1 <= X\_i <= N) and Y\_i (1 <= Y\_i <= N).

Consider this example:

```cpp
1-->2 
|  /| 
| / | 
|/  | 
3<--4 
```
The cow paths between pastures 1 and 3, 2 and 3, and 2 and 4 are two-way paths. One-way paths connect 1 to 2 and also 4 to 3. One valid way to convert the two-way paths into one-way paths in such a way that there are no cycles would be to direct them from 1 to 3, from 2 to 3, and from 3 to 4:

```cpp
1-->2 
|  /| 
| / | 
vL  v 
3<--4 
```


## 输入格式

Line 1: Three space separated integers: N, M1, and M2

Lines 2..1+M1: Line i+1 describes a one-way cow path using two space separated integers: A_i and B_i

Lines 2+M1..1+M1+M2: Line i+M1+1 describes a two-way cow path using two space separated integers: X_i and Y_i

## 输出格式

Lines 1..M2: Line i should contain two space-separated integers: either X_i and Y_i or Y_i and X_i, depending on the direction assigned to the i-th two-way path. The two-way paths must appear in the same order in the output as they do in the input. If there is no solution, output "-1" on a single line.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 2 3
1 2
4 3
1 3
4 2
3 2
```

#### 样例输出 #1

```
1 3
4 2
2 3
```
