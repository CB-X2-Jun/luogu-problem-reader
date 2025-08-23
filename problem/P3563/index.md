# P3563 P3563 [POI 2013] POL-Polarization

## 题目描述

Everyone knew it would only be a matter of time. So what? Faced for years on, a peril becomes the every-day reality. It loses its meaning...

Today the letter of the Bitotian char Bittard to the Byteotian king Byteasar was released to the public. Bitotia requested annexation of the whole Byteotia on pain of using the Bit Polarizing Magnet (BPM). If used, the BPM would make each and every road in Byteotia unidirectional. The enemy knows only too well that this could be a fatal blow to the minimalist Byteotian infrastructure - there is a unique way between each pair of towns.

How badly can the BPM damage the Byteotian infrastructure? Determine the minimum and the maximum number of such pairs of towns that it will still be possible to travel from one of them to the other while observing the new roads orientation.

## 输入格式

The first line of the standard input gives a single integer n (1 ≤ n ≤ 250,000), the number of towns in Byteotia. The n-1 lines that follow describe these roads. Each such line holds two integers, u and v (1 ≤ u ≤ v ≤ n), which indicate that there is a direct road (still bidirectional at the moment) linking the towns no. u and v.

## 输出格式

Two integers should be printed to the first and only line of the standard output. 

The first number should be the minimum and the second - the maximum number of pairs of towns which could remain connected (though in one direction only) after the roads are polarized.

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
4
1 2
1 3
1 4
```

#### 样例输出 #1

```
3 5
```
