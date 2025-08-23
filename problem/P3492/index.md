# P3492 P3492 [POI 2009] TAB-Arrays

## 题目描述

Consider an $n \times m$ table filled with **distinct** integers. The following operations can be performed on the table:  

1. Swapping two rows.  
2. Swapping two columns.  

We say that two tables are **similar** if, by applying some sequence of the above operations to the first table, we can obtain the second table.  

Write a program that determines for a given set of table pairs which pairs contain similar tables.  

## 输入格式

The first line of standard input contains a single integer $t$ ($1 \leq t \leq 10$), representing the number of table pairs. The subsequent lines describe the table pairs.  

Each table pair description starts with a line containing two integers $n$ and $m$ ($1 \leq n, m \leq 1000$), separated by a single space, representing the number of rows and columns of both tables.  

The next $n$ lines contain the description of the first table. The $i$-th of these lines contains $m$ integers $a_{ij}$ ($-10^6 \leq a_{ij} \leq 10^6$), separated by single spaces, representing the numbers in the $i$-th row of the first table.  

The next $n$ lines contain the description of the second table. The $i$-th of these lines contains $m$ integers $b_{ij}$ ($-10^6 \leq b_{ij} \leq 10^6$), separated by single spaces, representing the numbers in the $i$-th row of the second table.  

All numbers in a single table are distinct.  

## 输出格式

Your program should print $t$ lines to standard output. The $k$-th of these lines should contain the word **"TAK"** if the tables in the $k$-th input pair are similar, and **"NIE"** otherwise.  

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
2
4 3
1 2 3
4 5 6
7 8 9
10 11 12
11 10 12
8 7 9
5 4 6
2 1 3
2 2
1 2
3 4
5 6
7 8
```

#### 样例输出 #1

```
TAK
NIE
```
