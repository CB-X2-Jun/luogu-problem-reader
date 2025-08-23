# P3148 P3148 [USACO16OPEN] Bull in a China Shop P

## 题目描述

Farmer John has decided his home needs more decoration. Visiting the local china shop, he finds a delicate glass cow figurine that he decides to purchase, knowing that it will fit perfectly on the mantel above his fireplace.

The shape of the cow figurine is described by an $N \times M$ grid of haracters like the one below ($3 \leq N, M \leq 500$), where lowercase letter characters are each part of the figurine (indicating different colors) and '.' characters are not.

```
...............
...............
x..x...........
xxxx...........
xxxxaaaaaaa...
.xx.aaaaaaaaa..
....aaaaaaa.aa.
....ll...ll....
....vv...vv....
...............
```

Unfortunately, right before FJ can make his purchase, a bull runs through the shop  and breaks not only FJ's figurine, but many of the other glass objects on the shelves as well!  FJ's figurine breaks into 3 pieces, which quickly becomelost  among $K$ total pieces lying on the ground ($4 \leq K \leq 100$).  Each ofthe $K$ pieces is described by a grid of characters, just like the originalfigurine.

Please help FJ determine how many sets of 3 pieces (out of the $K$ on the floor)could be glued back together to mend his broken figurine.

The pieces on the ground might have been flipped vertically or horizontally, orrotated by some multiple of 90 degrees. Therefore, given the original grid aswell as $K$ grids describing pieces, you want to find sets of 3 pieces that canbe joined together to form the original picture, allowing the pieces to betranslated, flipped, or rotated multiples of 90 degrees.  When thensuperimposed, the 3 pieces should exactly form the original picture, with eachcolored square in the original picture represented in exactly one of the pieces.

## 输入格式

The first line contains a single integer $K$. Following that will be $K + 1$ piece descriptions.  The first description will describe the original glass cow,the following $K$ descriptions will be of the broken pieces.

Each description begins with a line containing two integers $R$ and $C$ ($1 \le R, C \le 500$).  The following $R$ lines contain $C$ lowercase alphabet characters describing the color of each cell.  Each piece will be horizontally/vertically connected and have at least one non-empty cell.


## 输出格式

Output the number of triples $i, j, k$ ($i < j < k$) such that pieces $i$, $j$, and $k$ can be arranged to form the original glass cow.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
5
5 5
aaaaa
..a..
bbabb
..a..
aaaaa
3 5
..abb
..a..
aaaaa
5 2
a.
a.
aa
a.
a.
1 2
bb
1 5
bbabb
2 5
aaaaa
..a..
```

#### 样例输出 #1

```
3
```

## 说明/提示

The three solutions use pieces $(0, 1, 2)$, $(0, 2, 4)$, $(1, 3, 4)$.

Note that this problem has a time limit of 6 seconds per test case (and twice that  for Java and Python submissions).
