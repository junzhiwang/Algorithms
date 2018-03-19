import timeit


class Prime:
	def __init__(self):
		pass

	@staticmethod
	def euler(n):
		prev = [0] * (n + 2)
		next = [0] * (n + 2)
		primes = []
		for i in range(1, n+1):
			prev[i] = i-1
			next[i] = i+1
		i = 2
		while i * i <= n:
			j = i
			while j * i <= n:
				k = j * i
				while k <= n:
					next[prev[k]] = next[k]
					prev[next[k]] = prev[k]
					if n / i < k:
						break
					k *= i
				j = next[j]
			i = next[i]
		i = 2
		while i <= n:
			primes.append(i)
			i = next[i]
		return primes

	@staticmethod
	def euler_2(n):
		prev = [0] * (n + 2)
		next = [0] * (n + 2)
		primes = []
		for i in range(1, n + 1):
			prev[i] = i - 1
			next[i] = i + 1

		i = 2
		while i * i <= n:
			fs = []
			k = i
			while k * i <= n:
				fs.append(k)
				k = next[k]
			for f in fs:
				m = i * f
				next[prev[m]] = next[m]
				prev[next[m]] = prev[m]
			i = next[i]

		i = 2
		while i <= n:
			primes.append(i)
			i = next[i]
		return primes

	@staticmethod
	def euler_simple(n):
		primes = []
		is_prime = [True] * (n + 1)
		for i in range(2, n // 2 + 1):
			if is_prime[i]:
				primes.append(i)
			for p in primes:
				if n / i < p:
					break
				is_prime[i * p] = False
				if i % p == 0:
					break
		for i in range(n // 2 + 1, n + 1):
			if is_prime[i]:
				primes.append(i)
		return primes

	@staticmethod
	def naive(n):
		primes = []
		i = 2
		while i <= n:
			is_prime = True
			j = 2
			while j * j <= i:
				if i % j == 0:
					is_prime = False
					break
				j += 1
			if is_prime:
				primes.append(i)
			i += 1
		return primes

	@staticmethod
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

	@staticmethod
	def eratosthenes(n):
		is_prime = [True] * (n + 1)
		primes = []
		for i in range(2, n + 1):
			if is_prime[i]:
				j = i * i
				while j <= n:
					is_prime[j] = False
					j += i
		for i in range(2, n + 1):
			if is_prime[i]:
				primes.append(i)
		return primes


def prime_time_test(fn, n):
	SETUP_CODE = """
from __main__ import Prime
	"""
	TEST_CODE = """
prime = Prime()
%s(%s)
	""" % (fn, n)
	times = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=1)
	print("%s: %f" % (fn, times))


if __name__ == "__main__":
	size = 2000000
	# naive_time(size)
	prime_time_test('Prime.naive_better', size)
	prime_time_test('Prime.eratosthenes', size)
	prime_time_test('Prime.euler', size)
	prime_time_test('Prime.euler_2', size)
	prime_time_test('Prime.euler_simple', size)
