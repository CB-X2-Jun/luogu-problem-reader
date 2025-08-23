# P2960 P2960 [USACO09OCT] Invasion of the Milkweed G

## 题目描述

Farmer John has always done his best to keep the pastures full of luscious, delicious healthy grass for the cows. He has lost the battle, though, as the evil milkweed has attained a foothold in the northwest part of his farm.

The pasture, as usual, is partitioned into a rectilinear grid of height Y (1 <= Y <= 100) and width X (1 <= X <= 100) with (1,1) being in the lower left corner (i.e., arranged as a normal X,Y coordinate grid). The milkweed has initially begun growing at square (Mx,My). Each week the milkweed propagates to all non-rocky squares that surround any square it already occupies, as many as eight more squares (both the rectilinear squares and the diagonals). After only one week in those squares, it is ready to move on to more squares.

Bessie wants to enjoy all the grass she can before the pastures are taken over by milkweed. She wonders how long it can last. If the milkweed is in square (Mx,My) at time zero, at what time does it complete its invasion of the pasture (which, for the given input data, will always happen)?

The pasture is described by a picture with '.'s for grass and '\*'s for boulders, like this example with X=4 and Y=3:

```
....
..*.
.**.
```

If the milkweed started in the lower left corner (row=1, column=1), then the map would progress like this:

```
    ....  ....  MMM.  MMMM  MMMM
    ..*.  MM*.  MM*.  MM*M  MM*M
    M**.  M**.  M**.  M**.  M**M
week  0    1    2    3    4
```

The milkweed has taken over the entire field after 4 weeks.

## 输入格式

\* Line 1: Four space-separated integers: X, Y, Mx, and My

\* Lines 2..Y+1: Line y+1 describes row (Y+2-y) of the field with X characters ('.' for grass and '\*' for a boulder)


## 输出格式

\* Line 1: A single integer that is the week number when the milkweed takes over the last remaining non-boulder square of the pasture.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 3 1 1 
.... 
..*. 
.**.
```

#### 样例输出 #1

```
4
```
