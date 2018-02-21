import random
from time import time
import sys

sys.setrecursionlimit(10000)

def mergesort(a):
	
	if len(a) <= 1:
		return a

	mid = len(a) // 2

	left = mergesort(a[:mid])
	right = mergesort(a[mid:])

	return merge(left, right)

def merge(l, r):
	res = []

	while len(l) and len(r):
		if l[0] < r[0]:
			res.append(l.pop(0))
		else:
			res.append(r.pop(0))

	if len(l):
		res += l
	else:
		res += r

	return res

def quicksort(a, start, end):
	if start < end:
		pi = partition(a, start, end)
		quicksort(a, start, pi - 1)
		quicksort(a, pi + 1, end)

	return a

def partition(a, start, end):
	pivot_el = a[end]
	j = start - 1

	for i in range(start, end):
		if a[i] <= pivot_el:
			j += 1
			a[j], a[i] = a[i], a[j]

	a[j + 1], a[end] = a[end], a[j + 1]
	return j + 1

def heapify(a, n, i):
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2

    if l < n and a[i] < a[l]:
        largest = l

    if r < n and a[largest] < a[r]:
        largest = r

    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        heapify(a, n, largest)

def heapsort(a):
    l = len(a)
    for i in range(l, -1, -1):
        heapify(a, l, i)
    for i in range(l-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)

algs = ['mergesort', 'quicksort', 'heapsort']
list_type = ['random', 'asc', 'desc']

def driver(i, a):
	if i == 0:
		return mergesort(a)
	elif i == 1:
		return quicksort(a, 0, len(a) - 1)
	else:
		return heapsort(a)

def random_list(n):
	l = []
	for i in range(0,n):
		l.append(random.randint(0,n))
	return l

for i in range(0, 1):
	for j in range(2,7):
		lists = [random_list(10**j)]
		lists.append(sorted(lists[0]))
		lists.append(lists[1][::-1])
		for x, l in enumerate(lists):
			t0 = time()
			try:
				res = driver(i, l)
				t1 = time()
				t = t1-t0
				print(algs[i] + ' ' + str(t) + ' ' + list_type[x] + ' n = ' + str(10**j))
			except RecursionError as re:
				t1 = time()
				t = t1-t0
				print('RE ' + algs[i] + ' ' + str(t) + ' ' + list_type[x] + ' n = ' + str(10**j))
		print('...........................................')