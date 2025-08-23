# P2903 P2903 [USACO08MAR] The Loathesome Hay Baler S

## 题目描述

Farmer John has purchased the world's most loathesome hay baler. Instead of having a drive-roller that drives maybe an idler roller that drives the power take-off for the baler, it has N rollers (2 <= N <= 1050) which drive and are driven by various rollers.

FJ has meticulously cataloged data for each roller i: X\_i,Y\_i are the center of the roller (-5000 <= X\_i <= 5000; -5000 <= Y\_i <= 5000); R\_i is the roller's radius (3 <= R\_i <= 800). The drive-roller is located at 0,0; the baler power take-off is located at X\_t,Y\_t (numbers supplied in the input).

The drive-roller turns clockwise at 10,000 revolutions per hour. Your job is to determine the speeds of all the rollers that are in the power-train: from the drive-roller through the power take-off roller. Rollers that do not transfer power to the take-off roller are to be ignored. A roller of radius Rd that is turning at S rph and driving another roller of radius Rx will cause the second roller to turn at the speed -S\*Rd/Rx (where the sign denotes whether the roller is turning clockwise or counterclockwise (anticlockwise for our British friends)).

Determine the power-train path and report the sum of the absolute values of all those rollers' speeds. All the rollers in the input set except the driver-roller are driven by some other roller; power is never transferred to a roller from more than one other roller.

Report your answer as an integer that is the truncated value after summing all the speeds.

## 输入格式

\* Line 1: Three space-separated integers: N, X\_t, and Y\_t

\* Lines 2..N+1: Line i+1 describes roller i's properties: X\_i, Y\_i, and R\_i

## 输出格式

\* Line 1: A single integer that is the truncated version of the sum of the absolute value of the speeds of the rollers in the power-train including the drive-roller, all the driven rollers, and the power take-off roller.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 32 54 
0 0 10 
0 30 20 
32 54 20 
-40 30 20
```

#### 样例输出 #1

```
20000
```

## 说明/提示

$2 \leq N \leq 1050$，$-5000 \leq x,y \leq 5000$，$3 \leq r \leq 800$。




Four rollers: the drive-roller at 0,0 with radius 10. It drives the roller above it at 0,30 with radius 20. That roller drives both the power take-off roller at 32,54 (r=20) and a random roller (not in the power train) at -40,30 (r=20).


Roller   Radius   Speed

1 (0,0)     10     10,000 

2 (0,30)    20     -5,000 

3 (32,54)   20      5,000 

------
Sum of abs values: 20,000

