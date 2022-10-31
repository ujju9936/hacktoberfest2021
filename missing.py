def find_missing(lst):
	return [x for x in range(lst[0], lst[-1]+1)
							if x not in lst]
