# P3507 P3507 [POI 2010] GRA-The Minima Game

## 题目描述

Alice and Bob learned the minima game, which they like very much, recently.

The rules of the game are as follows.

A certain number of cards lies on a table, each inscribed with a positive integer.

The players make alternate moves, Alice making the first one.

A move consists in picking an arbitrary positive number of cards from the table.

For such move the player receives a number of points equal to the minimum    of the numbers inscribed on the cards he collected.

The game ends when the last card is removed from the table.

The goal of each player is maximizing the difference between their and their opponent's score.

Alice and Bob have duly noted that there is an optimal strategy in the game.

Thus they are asking you to write a program that, for a given set of cards,    determines the outcome of the game when both players play optimally.

## 输入格式

In the first line of the standard input there is one integer ![](http://main.edu.pl/images/OI17/gra-en-tex.1.png) (![](http://main.edu.pl/images/OI17/gra-en-tex.2.png)) given,      denoting the number of cards.

The second line holds ![](http://main.edu.pl/images/OI17/gra-en-tex.3.png) positive integers ![](http://main.edu.pl/images/OI17/gra-en-tex.4.png) (![](http://main.edu.pl/images/OI17/gra-en-tex.5.png)),      separated by single spaces, that are inscribed on the cards.


## 输出格式

Your program should print out a single line with a single integer to the standard      output - the number of points by which Alice wins over Bob, assuming they both play optimally;      if it is Bob who has more points, the result should be negative.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
3
1 3 1
```

#### 样例输出 #1

```
2
```
