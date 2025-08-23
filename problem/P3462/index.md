# P3462 P3462 [POI 2007] ODW-Weights

## 题目描述

While moving to a new compound the Byteotian Institute of Experimental Physics has encountered a logisticalproblem - the transfer of its vast collection of precision weights turned out to be non-trivial.

The Institute has a certain number of containers of limited strength at its disposal. As many weightsas possible are to be put into the containers, the remaining ones will be discarded. There is no limit onthe number of weights to be put in a container apart from the requirement of not exceeding its strength. Acontainer may also be empty.

Any two weights in the Institute have a peculiar property: the mass of one of them is an integer multipleof the mass of the other. Particularly, they may have the same mass.

TaskWrite a programme which:

reads the durabilities of the containers and masses of the weights from the standard input,        determines the maximal number of weights that can be put in the containers,        writes the outcome to the standard output.


## 输入格式

The first line of the standard input contains two integers $n$ and $m$($1\le n,m\le 100\ 000$), separated by a singlespace, denoting respectively: the number of containers and the number of weights. The second line of thestandard input consists of $n$ integers $w_i$ ($1\le w_i\le 1\ 000\ 000\ 000$ for $1\le i\le n$), separated by single spaces,denoting the strengths of containers in milligrammes. In the third line there are $m$ integers $m_j$($1\le m_j\le 1\ 000\ 000\ 000$) for $1\le j\le m$), separated by single spaces, denoting masses of the weights in milligrammes.


## 输出格式

The first and only line of the standard output should contain a single integer -the maximal number ofweights that can be placed in the containers without exceeding their durability.


## 输入输出样例

### 样例 #1

#### 样例输入 #1

```
2 4
13 9
4 12 2 4
```

#### 样例输出 #1

```
3
```
