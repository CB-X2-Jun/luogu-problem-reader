# P1825 P1825 [USACO11OPEN] Corn Maze S

## 题目描述

This past fall, Farmer John took the cows to visit a corn maze. But this wasn't just any corn maze: it featured several gravity-powered teleporter slides, which cause cows to teleport instantly from one point in the maze to another. The slides work in both directions: a cow can slide from the slide's start to the end instantly, or from the end to the start. If a cow steps on a space that hosts either end of a slide, she must use the slide.

The outside of the corn maze is entirely corn except for a single exit.

The maze can be represented by an N x M (2 <= N <= 300; 2 <= M <= 300) grid. Each grid element contains one of these items:

\* Corn (corn grid elements are impassable) 

\* Grass (easy to pass through!) 

\* A slide endpoint (which will transport a cow to the other endpoint) 

\* The exit

A cow can only move from one space to the next if they are adjacent and neither contains corn. Each grassy space has four potential neighbors to which a cow can travel. It takes 1 unit of time to move from a grassy space to an adjacent space; it takes 0 units of time to move from one slide endpoint to the other.

Corn-filled spaces are denoted with an octothorpe (#). Grassy spaces are denoted with a period (.). Pairs of slide endpoints are denoted with the same uppercase letter (A-Z), and no two different slides have endpoints denoted with the same letter. The exit is denoted with the equals sign (=).

Bessie got lost. She knows where she is on the grid, and marked her current grassy space with the 'at' symbol (@). What is the minimum time she needs to move to the exit space?

## 输入格式

Line 1: Two space separated integers: N and M

Lines 2..N+1: Line i+1 describes row i of the maze: M characters (no spaces)

## 输出格式

Line 1: An integer, corresponding to the shortest time that Bessie needs to exit the maze.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
5 6
###=##
#.W.##
#.####
#.@W##
######
```

#### 样例输出 #1

```
3
```

## 说明/提示

Sample Explanation:

```plain
###=##
#.W.##
#.####
#.@W##
######
```

The endpoints of the only slide are marked with capital letters W.

The optimal strategy (which takes 3 units of time) is to: Move right to the slide endpoint using 1 unit of time, transport to the other endpoint using 0 units of time, move right using 1 unit of time, and move up to the exit using 1 unit of time.
