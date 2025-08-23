# P2875 P2875 [USACO07FEB] The Cow Lexicon S

## 题目描述

Few know that the cows have their own dictionary with W (1 ≤ W ≤ 600) words, each containing no more 25 of the characters 'a'..'z'. Their cowmunication system, based on mooing, is not very accurate; sometimes they hear words that do not make any sense. For instance, Bessie once received a message that said "browndcodw". As it turns out, the intended message was "browncow" and the two letter "d"s were noise from other parts of the barnyard.

The cows want you to help them decipher a received message (also containing only characters in the range 'a'..'z') of length L (2 ≤ L ≤ 300) characters that is a bit garbled. In particular, they know that the message has some extra letters, and they want you to determine the smallest number of letters that must be removed to make the message a sequence of words from the dictionary.

## 输入格式

Line 1: Two space-separated integers, respectively: W and L


Line 2: L characters (followed by a newline, of course): the received message


Lines 3..W+2: The cows' dictionary, one word per line

• 第1行:两个用空格隔开的整数,W和L.


• 第2行:一个长度为L的字符串,表示收到的信息.


• 第3行至第W+2行:奶牛的字典,每行一个词.


## 输出格式

Line 1: a single integer that is the smallest number of characters that need to be removed to make the message a sequence of dictionary words.

一个整数,表示最少去掉几个字母就可以使之变成准确的"牛语".


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
6 10
browndcodw
cow
milk
white
black
brown
farmer
```

#### 样例输出 #1

```
2
```

## 说明/提示

感谢@ws\_fuweidong 提供完整题面

