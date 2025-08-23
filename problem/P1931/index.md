# P1931 P1931 套利

## 题目描述

套利是利用汇率差异实现货币增值。例如，$1$ 美元可以兑换 $0.5$ 英镑、$1$ 英镑可以兑换 $10$ 法郎、$1$ 法郎可以兑换 $0.21$ 美元。接下来，一个聪明的交易商就可以从1美元开始，$0.5 \times 10.0 \times 0.21 =1.05$ 美元，获得了 $5\%$ 的利润。

你的任务是写一个程序，从输入文件读入汇率清单，然后决定套利是有可能的或没有可能的。

## 输入格式

输入文件包含多组数据，每组数据的第一行是一个整数 $n$（$1\le n\le30$）。代表有多少种货币。

接下来 $n$ 行字符串，每行表示一种货币的名称（名称中不会出现空格）。下一行是一个整数 $m$ ，约定了汇率表的长度。随后的 $m$ 行中，每行为 $c_i,r_{i,j},c_j$。其中：$c_i$ 表示源货币的名称，实数 $r_{i,j}$ 表示货币 $c_i$ 到 $c_j$ 的汇率，以及 $c_j$ 表示目标货币的名称。没有出现在其中的换汇是不可能的。

每组数据之间空一行。当 $n=0$ 时表示输入数据结束。

## 输出格式

第 $i$ 组数据，输出 Case i: 后，如果可以套利，输出 `Yes`，否则输出 `No`。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
3
USDollar
BritishPound
FrenchFranc
3
USDollar 0.5 BritishPound
BritishPound 10.0 FrenchFranc
FrenchFranc 0.21 USDollar

3
USDollar
BritishPound
FrenchFranc
6
USDollar 0.5 BritishPound
USDollar 4.9 FrenchFranc
BritishPound 10.0 FrenchFranc
BritishPound 1.99 USDollar
FrenchFranc 0.09 BritishPound
FrenchFranc 0.19 USDollar

0
```

#### 样例输出 #1

```
Case 1: Yes
Case 2: No
```
