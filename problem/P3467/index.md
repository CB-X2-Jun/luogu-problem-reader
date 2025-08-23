# P3467 P3467 [POI 2008] PLA-Postering

## 题目描述

All the buildings in the east district of Byteburg were built in accordance with the old arbitecture: they stand next to each other with no spacing inbetween. Together they form a very long chain of buildings of diverse    height, extending from east to west.

The mayor of Byteburg, Byteasar, has decided to have the north face of the chain covered with posters. Byteasar ponders over the minimum number of posters sufficient to    cover the whole north face. The posters have rectangular shape with vertical and horizontal sides. They cannot overlap, but may touch each other, i.e. have common points on the sides. Every poster has to entirely adjoin the walls of certain buildings and the whole surface of the north face has to be covered.

Task Write a programme that:

- reads the description of buildings from the standard input, 
- determines the minimum number of posters needed to entirely cover their north faces, 
- writes out the outcome to the standard output.


## 输入格式

The first line of the standard input contains one integer $n$ ($1\le n\le 250\ 000$), denoting the number of buildings the chain      comprises of.

Each of the following $n$ lines contains two integers $d_i$ and $w_i$ ($1\le d_i,w_i\le 1\ 000\ 000\ 000$),      separated by a single space, denoting respectively the length and height      of the $i^{th}$ building in the row.

## 输出格式

The first and only line of the standard output should contain one integer,      the minimum number of rectangular posters that suffice to cover the north faces      of the buildings.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
5
1 2
1 3
2 2
2 5
1 4
```

#### 样例输出 #1

```
4
```
