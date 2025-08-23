# P2983 P2983 [USACO10FEB] Chocolate Buying S

## 题目描述

Bessie and the herd love chocolate so Farmer John is buying them some.

The Bovine Chocolate Store features $N (1 \le N \le 100,000)$ kinds of chocolate in essentially unlimited quantities.  Each type i of chocolate has price $P_i (1 \le P_i \le 10^{18})$ per piece and there are $C_i (1 \le C_i \le 10^{18})$ cows that want that type of chocolate.

Farmer John has a budget of $B (1 \le B \le 10^{18})$ that he can spend on chocolates for the cows. What is the maximum number of cows that he can satisfy?  All cows only want one type of chocolate, and will be satisfied only by that type.

Consider an example where FJ has $50$ to spend on $5$ different types of chocolate. A total of eleven cows have various chocolate preferences:

|Chocolate\_Type|Per\_Chocolate\_Cost|Cows\_preferring\_this\_type| 
|:-----------:|:-----------:|:-----------:|
|$1$|$5$|$3$|
|$2$|$1$|$1$|
|$3$|$10$|$4$|
|$4$|$7$|$2$|
|$5$|$60$|$1$|

Obviously, FJ can't purchase chocolate type $5$, since he doesn't have enough money. Even if it cost only $50$, it's a counterproductive purchase since only one cow would be satisfied.

Looking at the chocolates start at the less expensive ones, he can purchase $1$ chocolate of type $2$ for $1 \times 1$ leaving $50-1=49$, then purchase $3$ chocolate of type $1$ for $3 \times 5$ leaving $49-15=34$, then  purchase $2$ chocolate of type $4$ for $2 \times 7$ leaving $34-14=20$, then  purchase $2$ chocolate of type $3$ for $2 \times 10$ leaving $20-20=0$.

He would thus satisfy $1 + 3 + 2 + 2 = 8$ cows. 

## 输入格式


Line $1$: Two space separated integers: $N$ and $B$.

Lines $2\ldots N+1$: Line $i$ contains two space separated integers defining chocolate type $i$: $P_i$ and $C_i$.

## 输出格式

Line $1$: A single integer that is the maximum number of cows that Farmer John can satisfy.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
5 50 
5 3 
1 1 
10 4 
7 2 
60 1
```

#### 样例输出 #1

```
8
```
