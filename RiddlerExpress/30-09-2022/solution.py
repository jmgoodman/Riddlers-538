"""
I encoded each digit (0-9) as a binary vector with length 7, the number of segments in the display.

I then checked all pairs of digits, excluding inverses of ones I had already seen, as simultaneous presses would have covered those. For instance, no checking 74 since, by then, I had already checked 47.

From here, I took the sum of their binary encoding vectors and checked a memory store.

If that memory store already contained this sum, I populated my results with the two digit pairs producing the equivalent vector sums.

Otherwise, I simply committed the new vector sum to the memory store.

At the end, I spit out all unique digit pairs included in my results. And included their mirror images unless they were palindromes (e.g., 99).
"""

data = [ [1,1,1,0,1,1,1],[0,0,1,0,0,1,0],[1,0,1,1,1,0,1],[1,0,1,1,0,1,1],[0,1,1,1,0,1,0],[1,1,0,1,0,1,1],[1,1,0,1,1,1,1],[1,0,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1] ]

pair_patterns = dict()
duplicated_patterns = set()

segmentcount = 7
numeralcount = 10

for idx0 in range(numeralcount):
	for idx1 in range(idx0,numeralcount): # don't do duplicates, since any order will do
		pattern = tuple([data[idx0][i]+data[idx1][i] for i in range(segmentcount)])

		if pattern not in pair_patterns:
			pair_patterns[pattern] = (idx0,idx1)
		else:
			duplicated_patterns.add( pair_patterns[pattern] )
			duplicated_patterns.add((idx0,idx1))

reversed_duplicates = set()
for pattern in duplicated_patterns:
	reversed_duplicates.add(pattern[::-1])

all_duplicates = duplicated_patterns.union(reversed_duplicates)

int_duplicates = list()

for duplicate in all_duplicates:
	int_duplicates += [ 10*duplicate[0] + duplicate[1] ]

print( int_duplicates )