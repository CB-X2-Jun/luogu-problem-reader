# P3084 P3084 [USACO13OPEN] Photo G

## 题目描述

Farmer John has decided to assemble a panoramic photo of a lineup of his $N$ cows ($1 \le N \le 2 \times 10^5$), which, as always, are conveniently numbered from $1...N$. Accordingly, he snapped $M$ ($1 \le M \le 1 \times 10^5$) photos, each covering a contiguous range of cows: photo $i$ contains cows $a_i$ through $b_i$ inclusive. The photos collectively may not necessarily cover every single cow.

After taking his photos, FJ notices a very interesting phenomenon: each photo he took contains exactly one cow with spots! FJ was aware that he had some number of spotted cows in his herd, but he had never actually counted them. Based on his photos, please determine the maximum possible number of spotted cows that could exist in his herd. Output $-1$ if there is no possible assignment of spots to cows consistent with FJ's photographic results.

## 输入格式

Line $1$: Two integers $N$ and $M$.

Lines $2...M+1$: Line $i+1$ contains $a_i$ and $b_i$.

## 输出格式

Line $1$: The maximum possible number of spotted cows on FJ's farm, or $-1$ if there is no possible solution.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
5 3 
1 4 
2 5 
3 4
```

#### 样例输出 #1

```
1
```

## 说明/提示

There are $5$ cows and $3$ photos. The first photo contains cows $1$ through $4$, etc.

From the last photo, we know that either cow $3$ or cow $4$ must be spotted. By choosing either of these, we satisfy the first two photos as well.
