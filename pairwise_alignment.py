#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import operator
import re
GAP = -5
MAX_NUM = 500

class array(object):
	def __init__(self, name):
		self.result = []
		self.name = name
	def set_seq(self, seq):
		self.seq = seq

class dp_table(object):
	global MAX_NUM
	global GAP

	def __init__(self, length):
		self.array = []
		for i in xrange(length):
			self.array.append([])
			self.array[i] = length*[0]
		for i in xrange(length):
			self.array[i][0] = i*GAP
			self.array[0][i] = i*GAP

def make_map(dp, trace, array1, array2):
	for i in xrange(1, len(array1.seq)):
		for j in xrange(1, len(array2.seq)):
			trace[i][j], dp[i][j] = match_score(dp, array1, array2, i, j)
	return trace

def match_score(dp, array1, array2, i, j):
	global GAP
	case = []
	case.append(dp[i-1][j-1]+get_score(array1.seq[i], array2.seq[j]))
	case.append(dp[i-1][j]+GAP)
	case.append(dp[i][j-1]+GAP)
	result = max(enumerate(case), key=operator.itemgetter(1))
	return result[0], result[1]

def traceback(trace, i, j, array1, array2):
	if i <= 0 and j <= 0: pass
	elif trace[i][j] == 0:
		array1.result.insert(0, array1.seq[i])
		array2.result.insert(0, array2.seq[j])
		traceback(trace, i-1, j-1, array1, array2)
	elif trace[i][j] == 1:
		array1.result.insert(0, array1.seq[i])
		array2.result.insert(0, '-')
		traceback(trace, i-1, j, array1, array2)
	else:
		array1.result.insert(0, '-')
		array2.result.insert(0, array2.seq[j])
		traceback(trace, i, j-1, array1, array2)

def convert(c):
	amino = ['A', 'R', 'N', 'D', 'C', 'Q',
		'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
	for i in xrange(20):
		if amino[i] == c:
			return i;
def get_score(x, y):
	score = [
		[ 5,-2,-1,-2,-1,-1,-1, 0,-2,-1,-2,-1,-1,-3,-1, 1, 0,-3,-2, 0], 
		[-2, 7,-1,-2,-4, 1, 0,-3, 0,-4,-3, 3,-2,-3,-3,-1,-1,-3,-1,-3],
		[-1,-1, 7, 2,-2, 0, 0, 0, 1,-3,-4, 0,-2,-4,-2, 1, 0,-4,-2,-3],
		[-2,-2, 2, 8,-4, 0, 2,-1,-1,-4,-4,-1,-4,-5,-1, 0,-1,-5,-3,-4],
		[-1,-4,-2,-4,13,-3,-3,-3,-3,-2,-2,-3,-2,-2,-4,-1,-1,-5,-3,-1],
		[-1, 1, 0, 0,-3, 7, 2,-2, 1,-3,-2, 2, 0,-4,-1, 0,-1,-1,-1,-3],
		[-1, 0, 0, 2,-3, 2, 6,-3, 0,-4,-3, 1,-2,-3,-1,-1,-1,-3,-2,-3],
		[ 0,-3, 0,-1,-3,-2,-3, 8,-2,-4,-4,-2,-3,-4,-2, 0,-2,-3,-3,-4],
		[-2, 0, 1,-1,-3, 1, 0,-2,10,-4,-3, 0,-1,-1,-2,-1,-2,-3, 2,-4],
		[-1,-4,-3,-4,-2,-3,-4,-4,-4, 5, 2,-3, 2, 0,-3,-3,-1,-3,-1, 4],
		[-2,-3,-4,-4,-2,-2,-3,-4,-3, 2, 5,-3, 3, 1,-4,-3,-1,-2,-1, 1],
		[-1, 3, 0,-1,-3, 2, 1,-2, 0,-3,-3, 6,-2,-4,-1, 0,-1,-3,-2,-3],
		[-1,-2,-2,-4,-2, 0,-2,-3,-1, 2, 3,-2, 7, 0,-3,-2,-1,-1, 0, 1],
		[-3,-3,-4,-5,-2,-4,-3,-4,-1, 0, 1,-4, 0, 8,-4,-3,-2, 1, 4,-1],
		[-1,-3,-2,-1,-4,-1,-1,-2,-2,-3,-4,-1,-3,-4,10,-1,-1,-4,-3,-3],
		[ 1,-1, 1, 0,-1, 0,-1, 0,-1,-3,-3, 0,-2,-3,-1, 5, 2,-4,-2,-2],
		[ 0,-1, 0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1, 2, 5,-3,-2, 0],
		[-3,-3,-4,-5,-5,-1,-3,-3,-3,-3,-2,-3,-1, 1,-4,-4,-3,15, 2,-3],
		[-2,-1,-2,-3,-3,-1,-2,-3, 2,-1,-1,-2, 0, 4,-3,-2,-2, 2, 8,-1],
		[ 0,-3,-3,-4,-1,-3,-3,-4,-4, 4, 1,-3, 1,-1,-3,-2, 0,-3,-1, 5]
	]
	return score[convert(x)][convert(y)]

if __name__ == '__main__':
	array_lst = []
	FILE = open(sys.argv[1], 'r')
	data = FILE.read()
	data = re.split("\n|''", data)
	for i in data:
		if i == '': pass
		elif i[0] == '>':
			array_lst.append(array(i))
		else:
			array_lst[-1].set_seq(i)

	length = len(array_lst[0].seq)
	length += 1
	DP = dp_table(length)
	trace = []
	for i in xrange(length):
		trace.append([])
		trace[i] = length*[0]
	for i in xrange(length):
		trace[i][0] = 1
		trace[0][i] = 2
	trace = make_map(DP.array, trace, array_lst[0], array_lst[1])
	traceback(trace, length-2, length-2, array_lst[0], array_lst[1])
	for i in xrange(len(array_lst)):
		print array_lst[i].name
		print ''.join(array_lst[i].result)
