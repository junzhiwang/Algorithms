# This is a repo for algorithm study notes and implementations.

## Table of contents

1.  [Introduction](#intro)
2.  [求 N 以内质数](#p1)
    1.  [朴素算法](#p11)
    2.  [埃式筛法](#p12)
    3.  [欧拉筛](#p13)
    4.  [简易欧拉筛](#p14)
    5.  [小结](#p15)

## Introduction <a name="intro" />
 
此仓库用于算法的学习笔记和 Python3 实现

## 求 N 以内质数 <a name="p1" />

给定 N，求 N 以内所有的质数并打印，主要分为朴素算法，埃式筛法，欧拉筛和简易欧拉筛。算法笔记和实现来自 [求质数表的 N 种境界][1]

### 朴素算法 <a name="p11" />

即暴力枚举，试除法。对于 2 到 N 的每一个数，都用小于它的所有数试除，来判断其是否为质数。时间复杂度 O(N^2)

改进：判断一个数是否为质数时，用 2 到 ![equation](https://latex.codecogs.com/svg.latex?\Medium&space;\sqrt{N})的所有质数试除。代码如下：

```
def naive_better(n):
	primes = []
	i = 2
	while i <= n:
		is_prime = True
		for j in primes:
			if j * j > n:
				break
			if i % j == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(i)
		i += 1
	return primes
```

[1]: https://www.bittiger.io/classpage/dEyzSBuZBsfiQPGyc "Bittiger"
