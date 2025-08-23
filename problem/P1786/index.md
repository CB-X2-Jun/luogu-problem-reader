# P1786 P1786 帮贡排序

## 题目背景

> 帮派名号：星月家园
> 
> 帮主尊号：Dragonfly Kang
> 
> 帮派 ID：2685023
> 
> 帮派等级：4
> 
> 帮派人数：101/110
> 
> 帮派技能：（？）

“星月家园”资料，欢迎各位豆友加入 ^\_^

---

在 absi2011 的帮派里，死号偏多。现在 absi2011 和帮主等人联合决定，要清除一些死号，加进一些新号，同时还要鼓励帮贡多的人，对帮派进行一番休整。

## 题目描述

目前帮派内共最多有：

- $1$ 位帮主（$\texttt{BangZhu}$）
- $2$ 位副帮主（$\texttt{FuBangZhu}$）
- $2$ 位护法（$\texttt{HuFa}$）
- $4$ 位长老（$\texttt{ZhangLao}$）
- $7$ 位堂主（$\texttt{TangZhu}$）
- $25$ 名精英（$\texttt{JingYing}$）
- 若干（数量不限）帮众（$\texttt{BangZhong}$）

保证以上职位是从高到低排列的。

现在 absi2011 要对帮派内几乎所有人的职位全部调整一番。他发现这是个很难的事情。于是要求你帮他调整。

他给你每个人的以下数据：

- 名字
- 原来职位
- 帮贡
- 等级

他要按照以下关键字给帮派内的人（帮主、副帮主除外）按以下关键字排序：

- 帮贡（从高到低）第一关键字
- 在输入中出现的顺序（从前到后）第二关键字

然后更新这些人的职位：

- 第 $1 \sim 2$ 名：护法
- 第 $3 \sim 6$ 名：长老
- 第 $7 \sim 13$ 名：堂主
- 第 $14 \sim 38$ 名：精英
- 第 $39 \sim (n-3)$ 名：帮众

可是，乐斗的显示并不按帮贡排序而按职位和等级排序。

他要你按照以下关键字排序并求出最后乐斗显示的列表（在他调整过职位后）：

- 职位（从高到低）第一关键字
- 等级（从高到低）第二关键字
- 在输入中出现的顺序（从前到后）第三关键字

注意：absi2011 无权调整帮主、副帮主的职位，包括他自己的。

## 输入格式

第一行一个正整数 $n$，表示星月家园内帮友的人数。

下面 $n$ 行每行两个字符串两个整数，表示每个人的名字、职位、帮贡、等级。

## 输出格式

一共输出 $n$ 行，每行包括排序后乐斗显示的名字、职位、等级。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
9
DrangonflyKang BangZhu 100000 66
RenZaiJiangHu FuBangZhu 80000 60
absi2011 FuBangZhu 90000 60
BingQiLingDeYanLei HuFa 89000 58
Lcey HuFa 30000 49
BangYou3 ZhangLao 1000 1
BangYou1 TangZhu 100 40
BangYou2 JingYing 40000 10
BangYou4 BangZhong 400 1
```

#### 样例输出 #1

```
DrangonflyKang BangZhu 66
RenZaiJiangHu FuBangZhu 60
absi2011 FuBangZhu 60
BingQiLingDeYanLei HuFa 58
BangYou2 HuFa 10
Lcey ZhangLao 49
BangYou1 ZhangLao 40
BangYou3 ZhangLao 1
BangYou4 ZhangLao 1
```

## 说明/提示

对于 $10\%$ 的数据，保证 $n=3$。

对于 $40\%$ 的数据，保证各个人的帮贡均为 $0$。

对于 $100\%$ 的数据，保证：

- $3\leq n\leq 110$
- $1\leq$ 名字长度 $\leq30$
- 所有名字两两不同
- 名字只包含 ASCII 可见字符
- $0\leq$ 各个人的帮贡 $\leq10^9$
- $1\leq$ 各个人等级 $\leq 150$
- 职位必定为以下七个中的一个：
  - $\texttt{BangZhu}$
  - $\texttt{FuBangZhu}$
  - $\texttt{HuFa}$
  - $\texttt{ZhangLao}$
  - $\texttt{TangZhu}$
  - $\texttt{JingYing}$
  - $\texttt{BangZhong}$
- 初始时帮派内最多有：
  - $1$ 位帮主
  - $2$ 位副帮主
  - $2$ 位护法
  - $4$ 位长老
  - $7$ 位堂主
  - $25$ 名精英
- 恰好有一名帮主
- 恰好有两名副帮主
- 恰好有一名副帮主叫 absi2011

【题目来源】

fight.pet.qq.com

absi2011 授权题目
