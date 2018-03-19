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
					if n / k > i:
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


def naive_time(n):
	SETUP_CODE = """
from __main__ import Prime
	"""
	TEST_CODE = """
prime = Prime()
prime.naive(%s)
	""" % n
	times = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=1)
	print(times)


def naive_better_time(n):
	SETUP_CODE = """
from __main__ import Prime
	"""
	TEST_CODE = """
prime = Prime()
prime.naive_better(%s)
		""" % n
	times = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=1)
	print(times)


def euler_time(n):
	SETUP_CODE = """
from __main__ import Prime
	"""
	TEST_CODE = """
prime = Prime()
prime.euler(%s)
	""" % n
	times = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=1)
	print(times)


def euler_2_time(n):
	SETUP_CODE = """
from __main__ import Prime
	"""
	TEST_CODE = """
prime = Prime()
prime.euler_2(%s)
	""" % n
	times = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=1)
	print(times)


def eratosthenes_time(n):
	SETUP_CODE = """
from __main__ import Prime
	"""
	TEST_CODE = """
prime = Prime()
prime.eratosthenes(%s)
	""" % n
	times = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=1)
	print(times)


if __name__ == "__main__":
	size = 100
	naive_time(size)
	naive_better_time(size)
	eratosthenes_time(size)
	euler_time(size)
	euler_2_time(size)
