# This is a repo for algorithm study notes and implementations.

## Table of contents

1.  [Introduction](#intro)
2.  [求 N 以内质数](#p1)
    1.  [朴素算法](#p11)
    2.  [埃式筛法](#p12)
    3.  [欧拉筛](#p13)
    4.  [简易欧拉筛](#p14)
    5.  [小结](#p15)

## <a name="intro" /> Introduction

此仓库用于算法的学习笔记和 Python3 实现

## <a name="p1" /> 求 N 以内质数

给定 N，求 N 以内所有的质数并打印，主要分为朴素算法，埃式筛法，欧拉筛和简易欧拉筛。

算法笔记和实现来自 [求质数表的 N 种境界][1]

### 朴素算法 <a name="p11" />

即暴力枚举，试除法。对于 2 到 N 的每一个数，都用小于它的所有数试除，来判断其是否为质数，时间复杂度 ![equation][2]。

改进：判断一个数是否为质数时，用 2 到 ![equation][3]的所有质数试除。

* 只需使用质数试除的原因是若 a 能被 b 整除，则 a 一定能被 b 的任何质因数  整除，反之若 a 不能被任何质数整除，则其  一定也不能被任何数整除。
* 试除到![equation][3]的原因是若 N 若能被大于![equation][3]的某数 a 整除，其一定也能被小于![equation][3]的![equation][4]的整除。

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

### 埃式筛法 <a name="p12" />

Sieve of Eratosthenes

每次取剩下的最小数为质数，并划去其倍数。

[gif](Eratosthenes.gif)

维护一个 is_prime 数组，从 下标 2 开始遍历，依次将下标为 2 的倍数直到 N 置为 false，再从 3 开始，依次将下标为 3 的倍数直到 N 置为 false，以此类推，已经被置为 false 的数则不作处理。

改进: 处理 i 时，从 i\*i 开始筛而不是 i\*2, 因为小于 i 的倍数之前已经被筛去了，避免重复劳动，遍历到![equation][3]时结束。

[1]: https://www.bittiger.io/classpage/dEyzSBuZBsfiQPGyc "Bittiger"
[2]: https://latex.codecogs.com/svg.latex?\Large&space;N^{2}
[3]: https://latex.codecogs.com/svg.latex?\Large&space;\sqrt{N}
[4]: https://latex.codecogs.com/svg.latex?\Large&space;\frac{N}{a}
