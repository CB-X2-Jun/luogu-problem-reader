# P3012 P3012 [USACO11FEB] Cowlphabet G

## 题目描述

Like all bovines, Farmer John's cows speak the peculiar 'Cow'

language. Like so many languages, each word in this language comprises a sequence of upper and lowercase letters (A-Z and a-z).  A word is valid if and only if each ordered pair of adjacent letters in the word is a valid pair.

Farmer John, ever worried that his cows are plotting against him, recently tried to eavesdrop on their conversation. He overheard one word before the cows noticed his presence. The Cow language is spoken so quickly, and its sounds are so strange, that all that Farmer John was able to perceive was the total number of uppercase letters, $U$ ($1 \leq U \leq 250$) and the total number of lowercase letters, $L$ ($1 \leq L \leq 250$) in the word. 

Farmer John knows all $P$ ($1 \leq P \leq 200$) valid ordered pairs of adjacent letters.  He wishes to know how many different valid words are consistent with his limited data.  However, since this number may be very large, he only needs the value modulo $97654321$.

约翰家的奶牛用别人听不懂的“牛语”联络。牛语采用英文字母，而且区分大小写。牛语中的语法中，前后字母的衔接非常重要，存在 $P$ 个基本组合，每个字母之后只能接固定的几个字母。约翰担心奶牛正在密谋反对他，于是最近一直在偷听她们的对话。可是牛语太复杂了，他只模模糊糊地听到了一个单词，并确定了这个单词中有 $U$（$1 \leq U \leq 250$）个大写字母，$L$（$1 \leq L \leq 250$）个小写字母。约翰对这个单词很在意，他想知道，有多少牛语词汇拥有 $U$ 个大写字母，$L$ 个小写字母。由于这个数字太大了，你只要输出答案取 $97654321$ 的余数就可以了。

## 输入格式

- Line 1: Three space-separated integers: U, L and P.

 - 第一行：三个用空格分开的整数 $U$，$L$ 和 $P$。

 - Lines 2..P+1: Two letters (each of which may be uppercase or lowercase), representing one valid ordered pair of adjacent letters in Cow.

 - 第二至 $P+1$ 行：两个字母 $A_i$ 和 $B_i$，表示字母 $A_i$ 后面可以接 $B_i$，没有一对 $A_i$ 和 $B_i$ 是完全相同的。

## 输出格式

- Line 1: A single integer, the number of valid words consistent with Farmer John's data mod $97654321$.

 - 第一行：单独一个整数，与 FJ 的数据吻合的单词数模 $97654321$ 的值。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
2 2 7 
AB 
ab 
BA 
ba 
Aa 
Bb 
bB
```

#### 样例输出 #1

```
7
```

## 说明/提示

The word Farmer John overheard had 2 uppercase and 2 lowercase letters.  The valid pairs of adjacent letters are AB, ab, BA, ba, Aa, Bb and bB.


The possible words are:

AabB
ABba
abBA
BAab
BbBb
bBAa
bBbB
