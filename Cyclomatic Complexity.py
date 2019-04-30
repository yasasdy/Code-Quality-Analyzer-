import pycparser
ast = pycparser.parse_file("testp.c", use_cpp=True)

dictionary = {}
def findComplexity(ast):
	children = ast.children()
	#print(children)
	for child in children:
		if str(type(child[1])) == "<class 'pycparser.c_ast.FuncDef'>":
			dictionary[str(child[1].decl.name)] = child[1].body

	for child in children:
		if str(type(child[1])) == "<class 'pycparser.c_ast.FuncDef'>":
			nn, ne = funcComplexity(child[1].body)
			print (str(child[1].decl.name), "- no of vertices and edges", ":", nn, ne)
			if(str(child[1].decl.name) == 'main'):		
				total_nn = nn
				total_ne = ne

	return total_nn, total_ne

def funcComplexity(child):
	
	if (child is None):	
		return (0, 0)		

	nn = 0
	ne = 0
	for item in child.block_items:
		#print(type(item))
		if ((str(type(item)) == "<class 'pycparser.c_ast.Assignment'>") or
			(str(type(item)) == "<class 'pycparser.c_ast.UnaryOp'>") or
			(str(type(item)) == "<class 'pycparser.c_ast.BinaryOp'>")):
			nn, ne = nn+1, ne+1

		elif str(type(item)) == "<class 'pycparser.c_ast.If'>":
			nn1, ne1 = funcComplexity(item.iftrue)
			nn2, ne2 = funcComplexity(item.iffalse)
			nn, ne = (1 + nn1 + nn2 + nn), (2 + ne1 + ne2 + ne)

		elif str(type(item)) == "<class 'pycparser.c_ast.For'>":
			nn3, ne3 = funcComplexity(item.stmt)
			nn, ne = (3 + nn3 + nn), (4 + ne3 + ne)
		
		elif str(type(item)) == "<class 'pycparser.c_ast.While'>":
			nn4, ne4 = funcComplexity(item.stmt)
			nn, ne = (1 + nn4 + nn), (2 + ne4 + ne)

		elif str(type(item)) == "<class 'pycparser.c_ast.Break'>":
			nn8, ne8 = 1, 1
			nn, ne = (nn8 + nn), (ne8 + ne)
		
		elif str(type(item)) == "<class 'pycparser.c_ast.FuncCall'>":
			if(str(item.name.name) == 'printf' or
				str(item.name.name) == 'scanf'):
				nn5, ne5 = 1, 1
				nn, ne = (nn5 + nn), (ne5 + ne)	
			else:
				nn6, ne6 = funcComplexity(dictionary[str(item.name.name)])
				nn, ne = (1 + nn6 + nn), (2 + ne6 + ne)
		
		elif str(type(item)) == "<class 'pycparser.c_ast.Return'>":
			nn7, ne7 = 1, 0
			nn, ne = (nn7 + nn), (ne7 + ne)

	return (nn, ne) 	

if __name__ == "__main__":
	no_of_vertices, no_of_edges = findComplexity(ast)		
	print("Cyclomatic Complexity:", no_of_edges - no_of_vertices + 2)

