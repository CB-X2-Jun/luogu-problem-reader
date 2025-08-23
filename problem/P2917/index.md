# P2917 P2917 [USACO08NOV] Toys G

## 题目描述

Bessie's birthday is coming up, and she wishes to celebrate for the next D (1 <= D <= 100,000; 70% of testdata has 1 <= D <= 500) days. Cows have short attention spans so Bessie wants to provide toys to entertain them. She has calculated that she will require T\_i (1 <= T\_i <= 50) toys on day i.

Bessie's kindergarten provides many services to its aspiring bovine programmers, including a toy shop which sells toys for Tc (1 <= Tc <= 60) dollars. Bessie wishes to save money by reusing toys, but Farmer John is worried about transmitting diseases and requires toys to be disinfected before use. (The toy shop disinfects the toys when it sells them.)

The two disinfectant services near the farm provide handy complete services. The first one charges C1 dollars and requires N1 nights to complete; the second charges C2 dollars and requires N2 nights to complete (1 <= N1 <= D; 1 <= N2 <= D; 1 <= C1 <= 60; 1 <= C2 <= 60). Bessie takes the toys to the disinfecters after the party and can pay and pick them back up the next morning if one night service is rendered, or on later mornings if more nights are required for disinfecting.

Being an educated cow, Bessie has already learned the value of saving her money. Help her find the cheapest way she can provide toys for her party.

POINTS: 400


## 输入格式

\* Line 1: Six space-separated integers: D, N1, N2, C1, C2, Tc

\* Lines 2..D+1: Line i+1 contains a single integer: T\_i


## 输出格式

\* Line 1: The minimum cost to provide safe and sanitary toys for Bessie's birthday parties.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 1 2 2 1 3 
8 
2 
1 
6
```

#### 样例输出 #1

```
35
```

## 说明/提示

Bessie wishes to party for 4 days, and requires 8 toys the first day, 2 toys the second, 1 toy the third, and 6 toys on the fourth day. The first disinfectant service takes 1 day and charges \$2, and the second takes 2 days and charges \$1. Buying a new toy costs \$3.


Day 1   Purchase 8 toys in the morning for $24; party in the

afternoon. Take 2 toys to the fast cleaner (overnight) and 

the other 6 toys to the slow cleaner (two nights). 

Day 2   Pick up the two toys at the fast cleaner; pay $4. Party in the afternoon. Take 1 toy to the slow cleaner. 

Day 3   Pick up 6 toys from the slow cleaner and pay $6. Party in the afternoon.

Day 4   Pick up the final remaining toy from the slow cleaner

(bringing the number of toys onsite back to 6); pay $1. Party hearty with the realization that a minimum amount of money was spent.

