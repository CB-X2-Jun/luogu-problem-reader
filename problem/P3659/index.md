# P3659 P3659 [USACO17FEB] Why Did the Cow Cross the Road I G

## 题目描述

Why did the cow cross the road? Well, one reason is that Farmer John's farm simply has a lot of roads, making it impossible for his cows to travel around without crossing many of them.

FJ's farm is arranged as an $N \times N$ square grid of fields ($3 \leq N \leq 100$), with a set of $N-1$ north-south roads and $N-1$ east-west roads running through the interior of the farm serving as dividers between the fields. A tall fence runs around the external perimeter, preventing cows from leaving the farm. Bessie the cow can move freely from any field to any other adjacent field (north, east, south, or west), as long as she carefully looks both ways before crossing the road separating the two fields. It takes her $T$ units of time to cross a road ($0 \leq T \leq 1,000,000$).

One day, FJ invites Bessie to visit his house for a friendly game of chess. Bessie starts out in the north-west corner field and FJ's house is in the south-east corner field, so Bessie has quite a walk ahead of her. Since she gets hungry along the way, she stops at every third field she visits to eat grass (not including her starting field, but including possibly the final field in which FJ's house resides). Some fields are grassier than others, so the amount of time required for stopping to eat depends on the field in which she stops.

Please help Bessie determine the minimum amount of time it will take to reach FJ's house.

## 输入格式

The first line of input contains $N$ and $T$. The next $N$ lines each contain $N$ positive integers (each at most 100,000) describing the amount of time required to eat grass in each field. The first number of the first line is the north-west corner.


## 输出格式

Print the minimum amount of time required for Bessie to travel to FJ's house.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4 2
30 92 36 10
38 85 60 16
41 13 5 68
20 97 13 80
```

#### 样例输出 #1

```
31
```

## 说明/提示

The optimal solution for this example involves moving east 3 squares (eating the "10"), then moving south twice and west once (eating the "5"), and finally moving south and east to the goal.
