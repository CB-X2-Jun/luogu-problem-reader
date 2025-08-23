# P3025 P3025 [USACO11OPEN] Forgotten Password S

## 题目描述

就像在我们身上经常发生的那样，Bessie 又一次忘记了她的牛场管理员密码，她只能记得密码的一部分。

首先，她记得密码 $P$ 是长度为 $L$（$1 \le L \le 1000$）的字符串，并且她的密码中出现过的所有单词都记录在她的共有 $NW$ 个单词的字典中，每个字典中的单词 $W_i$ 都是由 $1$ 至 $20$ 个小写拉丁字母组成的。

她只记得密码中的一部分字母和它的位置。例如，Bessie 记得她的密码为 `a??l?ban???????`，其中，`?` 是她忘记的字母。她的字典中有这些单词：`apple cow farmer banana bananas pies`。所以，Bessie 的密码的两种可能是`applebananapies` 和 `applebananascow`.

现在，给你 Bessie 还记得的字母和她的字典，求可能的密码。如果有多个答案，则输出字典序最小的那一个。

## 输入格式

第一行输入她密码的长度 $L$ 和字典中的单词数量 $NW$，用一个空格隔开。

第二行输入长为 $L$ 的字符串 $P$。

此后 $NW$ 行，每行输入一个字符串 $W_i$。

## 输出格式

只输出一行：Bessie 的密码。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
15 6 
a??l?ban??????? 
apple 
cow 
farmer 
banana 
bananas 
pies
```

#### 样例输出 #1

```
applebananapies
```
