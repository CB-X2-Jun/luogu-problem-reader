# P3033 P3033 [USACO11NOV] Cow Steeplechase G

## 题目描述

Farmer John has a brilliant idea for the next great spectator sport: Cow Steeplechase! As everyone knows, regular steeplechase involves a group of horses that race around a course filled with obstacles they must jump over. FJ figures the same contest should work with highly-trained cows, as long as the obstacles are made short enough.

In order to design his course, FJ makes a diagram of all the $N$ possible obstacles he could potentially build. Each one is represented by a line segment in the 2D plane that is parallel to the horizontal or vertical axis. Obstacle i has distinct endpoints $(X1_i, Y1_i)$ and $(X2_i, Y2_i)$. An example is as follows:
```none
   --+-------   
-----+-----
  ---+---     |
     |     |  |
   --+-----+--+-   |
     |     |  |  | |
     |   --+--+--+-+-
           |  |  | |
              |
```
FJ would like to build as many of these obstacles as possible, subject to the constraint that no two of them intersect. Starting with the diagram above, FJ can build $7$ obstacles:
```none
   ----------   
-----------
  -------     |
           |  |
           |  |    |
           |  |  | |
           |  |  | |
           |  |  | |
              |
```

Two segments are said to intersect if they share any point in common, even an endpoint of one or both of the segments. FJ is certain that no two horizontal segments in the original input diagram will intersect, and that similarly no two vertical segments in the input diagram will intersect.

Please help FJ determine the maximum number of obstacles he can build.

## 输入格式

The first line contains $N$.

The following $N$ lines contain four space-separated integers representing an obstacle: $X1_i$, $Y1_i$, $X2_i$, and $Y2_i$.

## 输出格式

Output the maximum number of non-crossing segments FJ can choose.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
3 
4 5 10 5 
6 2 6 12 
8 3 8 5
```

#### 样例输出 #1

```
2
```

## 说明/提示

**[Sample Explanation]**

There are three potential obstacles. The first is a horizontal segment connecting $(4, 5)$ to $(10, 5)$; the second and third are vertical segments connecting $(6, 2)$ to $(6, 12)$ and $(8, 3)$ to $(8, 5)$.

The optimal solution is to choose both vertical segments.

**[Data Range]**

For $100\%$ of the data, $1\le N\le250,1\le X1_i,Y1_i,X2_i,Y2_i\le10^9$.
