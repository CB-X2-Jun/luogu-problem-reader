# P1703 P1703 那个什么密码 2

## 题目背景

_本题改编自 <https://www.luogu.com.cn/problem/P1079>。_

## 题目描述

16 世纪法国外交家 Blaise de Vigenère 设计了一种多表密码加密算法 Vigenère 密码。Vigenère 密码的加密解密算法简单易用，且破译难度比较高，曾在美国南北战争中为南军所广泛使用。

 
在密码学中，我们称需要加密的信息为明文，用 $M$ 表示；称加密后的信息为密文，用 $C$ 表示；而密钥是一种参数，是将明文转换为密文或将密文转换为明文的算法中输入的数据，记为 $k$。在 Vigenère 密码中，密钥 $k$ 是一个字母串，$k=k_1,k_2,…,k_n$。当明文 $M=m_1,m_2,…,m_n$ 时，得到的密文 $C=c_1,c_2,…,c_n$，其中 $c_i$=$m_i \operatorname{\circledR} k_i$，运算 $\circledR$ 的规则如下表所示：

$$
\gdef \a{\kern{-5pt}}
\begin{array}{c|cccccccccccccccccccccccccc}
\circledR &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a  \\\hline
\tt A &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a  \\
\tt B &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a  \\
\tt C &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a  \\
\tt D &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a  \\
\tt E &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a  \\
\tt F &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a  \\
\tt G &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a  \\
\tt H &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a  \\
\tt I &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a  \\
\tt J &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a  \\
\tt K &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a  \\
\tt L &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a  \\
\tt M &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a  \\
\tt N &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a  \\
\tt O &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a  \\
\tt P &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a  \\
\tt Q &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a  \\
\tt R &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a  \\
\tt S &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a  \\
\tt T &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a  \\
\tt U &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a  \\
\tt V &\tt V \a &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a  \\
\tt W &\tt W \a &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a  \\
\tt X &\tt X \a &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a  \\
\tt Y &\tt Y \a &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a  \\
\tt Z &\tt Z \a &\tt A \a &\tt B \a &\tt C \a &\tt D \a &\tt E \a &\tt F \a &\tt G \a &\tt H \a &\tt I \a &\tt J \a &\tt K \a &\tt L \a &\tt M \a &\tt N \a &\tt O \a &\tt P \a &\tt Q \a &\tt R \a &\tt S \a &\tt T \a &\tt U \a &\tt V \a &\tt W \a &\tt X \a &\tt Y \a  \\

\end{array}

$$

Vigenère 加密在操作时需要注意：

1. $\circledR$ 运算忽略参与运算的字母的大小写，并保持字母在明文 $M$ 中的大小写形式；
2. 当明文 $M$ 的长度大于密钥 $k$ 的长度时，将密钥 $k$ 重复使用。

**任务：**

给定一串明文和一串密钥，请对明文进行两次加密：

- 一次加密：依次输入 $n$ 条形如 $(l,r)$ 的指令，翻转明文中的第 $l$ 到 $r$ 个字符。
- 二次加密：按照上面的规则，对一次加密后的一级密文再施加一次 Vigenère 密码加密，得到最终的二级密文。

例如，明文 $M=\texttt{Helloworld}$，密钥 $k=\texttt{abc}$，$n=1$，指令为 $(4,9)$ 时，一级密文 $C_1=\texttt{Hellrowold}$，二级密文 $C_2=\texttt{Hfnlsqwpnd}$。

$$
\def\arraystretch{1.5}
\begin{array}{|c|c|c|c|c|c|c|c|c|c|c|} \hline
\textsf{明文} & \tt H & \tt e & \tt l & \tt l & \tt o & \tt w & \tt o & \tt r & \tt l & \tt d \\  \hline
\textsf{一级密文} & \tt H & \tt e & \tt l & \tt l & \tt r & \tt o & \tt w & \tt o & \tt l & \tt d \\  \hline
\textsf{密钥} & \tt a & \tt b & \tt c & \tt a & \tt b & \tt c & \tt a & \tt b & \tt c & \tt a \\  \hline
\textsf{二级密文} & \tt H & \tt f & \tt n & \tt l & \tt s & \tt q & \tt w & \tt p & \tt n & \tt d \\  \hline
\end{array}
$$

## 输入格式

第一行为一个字符串，表示密钥 $k$，长度不超过 $1000$，其中仅包含大小写字母。  

第二行为一个字符串，表示加密前的明文，长度不超过 $1000$，其中仅包含大小写字母。

第三行为一个非负整数 $n\ (0 \le n \le 10^5)$，表示一次加密中的指令个数。

下面 $n$ 行，每行两个正整数 $l,r\ (1 \le l \le r \le m)$，表示一个指令，其中 $m$ 是明文的长度。

## 输出格式

一个字符串，表示输入密钥和明文所对应的二级密文。

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
CompleteVictory
Wherethereisawillthereisaway
0
```

#### 样例输出 #1

```
Yvqgpxaimmklongnzfwpvxmniytm
```
