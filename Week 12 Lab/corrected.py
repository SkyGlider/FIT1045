#write your code here

def is_clique(S, k, G):
	pass

def is_indset(S, k, G):
	pass

def complement(G):
	pass


example_graph =\
       [[0, 1, 0, 0, 0, 0, 0],
		[1, 0, 1, 1, 0, 0, 0],
		[0, 1, 0, 1, 1, 1, 0],
		[0, 1, 1, 0, 1, 1, 0],
		[0, 0, 1, 1, 0, 1, 1],
		[0, 0, 1, 1, 1, 0, 1],
		[0, 0, 0, 0, 1, 1, 0]]

example_graph_complement =\
	       [[0, 0, 1, 1, 1, 1, 1],
		[0, 0, 0, 0, 1, 1, 1],
		[1, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 0, 0],
		[1, 1, 0, 0, 0, 0, 0],
		[1, 1, 1, 1, 0, 0, 0]]


if __name__ == "__main__":
	#if you have not yet implemented one of the functions, comment out those tests
	assert is_clique([2,3,4,5], 4, example_graph) == True
	assert is_clique([1,2,3], 2, example_graph) == True
	assert is_clique([1,2,3,6], 1, example_graph) == False
	assert is_clique([0,1,5,6], 5, example_graph) == False
	assert is_clique([1,2,3,4], 3, example_graph) == False

	assert is_indset([1,3,5], 2, example_graph) == False
	assert is_indset([1,2,6],2,  example_graph) == False
	assert is_indset([3,6], 2, example_graph) == True
	assert is_indset([1,2,3,6], 1, example_graph) == False
	assert is_indset([0,2,6], 2, example_graph) == True

	assert complement(example_graph) == example_graph_complement

	print("All tests passed!")