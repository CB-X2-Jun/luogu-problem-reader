# P2931 P2931 [USACO09HOL] Pearl Bracelet G【征集 SPJ】

## 题目描述

Bessie received a magic bracelet of a set of the rarest black pearls for her favorite holiday. Bessie loved the bracelet and marveled that each pearl contained a small number engraved on it. She noticed that if you align the the bracelet's pearls in all the possible ways by bending it around some point (see below), the 'progressive' sums of the pearls' numbers that have corresponding numbers on the top and bottom sides of the bracelet never, everatch when compared using mod M (2 <= M <= 100). 'Progressive' sums are exemplified below.

Suppose the mod M is 3. Consider a bracelet with N=6 pearls, etched sequentially with the numbers 0, 1, 0, 2, 1, 0. We'll illustrate this bracelet with its clasps like this:

>0-1-0-2-1-0< 
The six-pearl bracelet can be laid out on the ground in five different ways so that some pearls 'correspond' to each other (see below). We can 'progressively' sum-mod-M those pearls that correspond on the top and also sum-mod-M the corresponding pearls on the bottom, as shown with ONE-sums, TWO-sums, THREE-sums (and so on when N > 6).

```cpp
               |     THREE-sums         |     TWO-sums      | ONE-sums
 --------------+------------------------+-------------------+--------- 
    >0-1-0-2-1 |                        |                   | => 1 |
               |                        |                   | 
            >0 |                        |                   | => 0 
 --------------+------------------------+-------------------+--------- 
      >0-1-0-2 |                        | => 0+2 = 2        | => 2 | 
               |                        |                   | 
          >0-1 |                        | => 0+1 = 1        | => 1 
 --------------+------------------------+-------------------+--------- 
        >0-1-0 | => 0+1+0 = 1           | => 1+0 = 1        | => 0 | 
               |                        |                   | 
        >0-1-2 | => 0+1+2 = 3 mod 3 = 0 | => 1+2 mod 3 = 0  | => 2 
 --------------+------------------------+-------------------+--------- 
          >0-1 |                        | => 0+1 = 1        | => 1 | 
               |                        |                   | 
      >0-1-2-0 |                        | => 2+0 = 2        | => 0 
 --------------+------------------------+-------------------+--------- 
            >0 |                        |                   | => 0 | 
               |                        |                   | 
    >0-1-2-0-1 |                        |                   | => 1 
```



Bessie notes that all the pairs of sums contain different numbers and has heard this is true for all the magic bracelets. Bessie wondered what is longest possible bracelet that has this unique-sum property.

Given M, find a really long (but no longer than 20,000) set of numbers can be etched on the black pearls to maintain this unique sum property for a bracelet.

This is an output-only problem, the 15 input files can be downloaded at: http://ace.delos.com/perlbrac.zip

SCORING: Scoring for this problem will be relative; your integer score (out of 10) for each test case will be int (10 \* sqrt (YOURS / BEST)), where YOURS is the length of your solution, and BEST is the length of the best solution among all contestants.

FEEDBACK: When you submit a file for grading, it will be checked for both correct format and validity (i.e., whether it satisfies the required numerical properties), and you will be informed of the results.


## 输入格式

\* Line 1: Two space-separated integers: the case number and M


## 输出格式

\* Line 1: A single line containing the task name and case number: #FILE perlbrac CASENUM

\* Line 2: A single line with a single integer, N (which must be no larger than 20,000)

\* Lines 3..N+1: Line i+2 contains a single integer that is the integer etched onto the i-th pearl on the bracelet; this number should be between 0 and M - 1, inclusive


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
0 6
```

#### 样例输出 #1

```
#FILE perlbrac 0 
6 
0 
1 
0 
2 
1 
0
```
