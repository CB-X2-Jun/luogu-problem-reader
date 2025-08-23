# P1906 P1906 凯撒密码

## 题目描述

在元老院的支持下，Caesar 率领罗马军团进攻高卢地区。但是他的军事行动并不顺利，他急需你的支持。

一天，你突然受到 Caesar 从前线写来的信。为了防止敌军偷窃情报，Caesar 决定用自创的密码来写这封信。但是面对满纸的乱码，你也无从下手。于是你前往元老院询问这种密码的玄机。

元老们告诉你，这是凯撒移位密码（世界上最早的加密术——编者注），解读它非常的简单：

对于明文中的每个字母，Caesar 会用它后面的第 $t$ 个字母代替。例如，当 $t=2$ 时，字母 `A` 将变成 `C`，字母 `B` 将变成 `D`，……，字母 `Y` 将变成 `A`，字母 `Z` 将变成 `B`（假设字母表是循环的）。

这样一来：

```plain
(t = 2)

[Plain Text]   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
[Cipher]       C D E F G H I J K L M N O P Q R S T U V W X Y Z A B

[Plain Text]   I Need Soldiers
[Cipher]       K Pggf Uqnfkgtu
```

如此一来，需要传达的信息在外人看来就如同天书了。加上 Caesar 会不时更换 $t$ 的值，使得密码变得更加难以捉摸。

你的任务是将 Caesar 的密码翻译为明文。

## 输入格式

你将得到若干段 Caesar 的密码，我们保证这是一句成文的英文句子。输入文件将保证小于 50 KB。

每个句子以一行 `START` 开始，下一行描述这个句子，再下一行以 `END` 结束。整个输入文件以 `ENDOFINPUT` 结束。

## 输出格式

对于每个句子，输出翻译后的明文。

**输出请全部转为大写！**

## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
START
NS BFW, JAJSYX TK NRUTWYFSHJ FWJ YMJ WJXZQY TK YWNANFQ HFZXJX
END
START
N BTZQI WFYMJW GJ KNWXY NS F QNYYQJ NGJWNFS ANQQFLJ YMFS XJHTSI NS WTRJ
END
START
IFSLJW PSTBX KZQQ BJQQ YMFY HFJXFW NX RTWJ IFSLJWTZX YMFS MJ
END
ENDOFINPUT
```

#### 样例输出 #1

```
IN WAR, EVENTS OF IMPORTANCE ARE THE RESULT OF TRIVIAL CAUSES
I WOULD RATHER BE FIRST IN A LITTLE IBERIAN VILLAGE THAN SECOND IN ROME
DANGER KNOWS FULL WELL THAT CAESAR IS MORE DANGEROUS THAN HE
```

## 说明/提示

1. 如果你有看过《福尔摩斯探案集》的话，请回忆“跳舞娃娃”密码破译第一步；
2. 我想这些可能会对你有帮助：

```plain
e 0.1268
t 0.0978
a 0.0788
o 0.0766
i 0.0707
n 0.0706
s 0.0634
r 0.0594
```

---

**提示：**

根据大量统计，在成文的英文句子中，字母 E 的出现频率最高。

你需要根据这一特性确定 $t$ 的值。

数据保证这一特性可以唯一确定 $t$ 的值。
