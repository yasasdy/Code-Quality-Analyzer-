import pycparser
ast = pycparser.parse_file("testp.c", use_cpp=True)

dictionary = {}
def findComplexity(ast):
	children = ast.children()
	print(children)
	total_nn, total_ne = 0, 0
	for child in children:
		if str(type(child[1])) == "<class 'pycparser.c_ast.FuncDef'>":
			dictionary[str(child[1].decl.name)] = child[1].body

	for child in children:
		if str(type(child[1])) == "<class 'pycparser.c_ast.FuncDef'>":
			nn, ne = funcComplexity(child[1].body)
			if(ne == 0):
				ne = ne
			else:
				ne = ne - 1
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

	if(str(type(child)) == "<class 'pycparser.c_ast.If'>"):
		nn9, ne9 = funcComplexity(child.iftrue)
		print('9', nn9, ne9)
		nn10, ne10 = funcComplexity(child.iffalse)
		print('10', nn10, ne10)
		nn, ne = (1 + nn + nn9 + nn10), (2 + ne + ne9 + ne10)

	elif(str(type(child)) == "<class 'pycparser.c_ast.Compound'>"):
		if (child.block_items is None):
			nn, ne = nn, ne
		else:
			for item in child.block_items:
				#print(type(item))
				if (item is None):	
					nn, ne = nn, ne

				elif ((str(type(item)) == "<class 'pycparser.c_ast.Assignment'>") or
					(str(type(item)) == "<class 'pycparser.c_ast.UnaryOp'>") or
					(str(type(item)) == "<class 'pycparser.c_ast.BinaryOp'>")):
					nn, ne = nn+1, ne+1

				elif (str(type(item)) == "<class 'pycparser.c_ast.Decl'>"):
					if(item.init is not None):
						nn, ne = nn+1, ne+1	
						print('D', nn, ne)						

				elif str(type(item)) == "<class 'pycparser.c_ast.If'>":
					# if(item.iffalse is not None):	
					# if(str(type(item.iftrue)) == "<class 'pycparser.c_ast.Compound'>"):
					nn1, ne1 = funcComplexity(item.iftrue)
					print('1', nn1, ne1)
					# if(str(type(item.iffalse)) == "<class 'pycparser.c_ast.Compound'>"):
					nn2, ne2 = funcComplexity(item.iffalse)
					print('2', nn2, ne2)
					nn, ne = (1 + nn1 + nn2 + nn), (2 + ne1 + ne2 + ne)
					# if((str(type(item.iftrue)) == "<class 'pycparser.c_ast.Return'>")):	
					# 	nn1, ne1 = 1, 2
					# 	nn, ne = (nn1 + nn), (ne1 + ne)
					# if((str(type(item.iffalse)) == "<class 'pycparser.c_ast.Return'>")):	
					# 	nn1, ne1 = 1, 2
					# 	nn, ne = (nn1 + nn), (ne1 + ne)

				elif str(type(item)) == "<class 'pycparser.c_ast.For'>":
					nn3, ne3 = funcComplexity(item.stmt)
					nn, ne = (3 + nn3 + nn), (4 + ne3 + ne)
				
				elif str(type(item)) == "<class 'pycparser.c_ast.While'>":
					nn4, ne4 = funcComplexity(item.stmt)
					nn, ne = (1 + nn4 + nn), (2 + ne4 + ne)

				elif str(type(item)) == "<class 'pycparser.c_ast.Break'>":
					nn8, ne8 = 1, 1
					nn, ne = (nn8 + nn), (ne8 + ne)

				elif str(type(item)) == "<class 'pycparser.c_ast.Return'>":
					nn, ne = (nn + 1), (ne + 1)
				
				elif str(type(item)) == "<class 'pycparser.c_ast.FuncCall'>":
					if(str(item.name.name) == 'printf' or
						str(item.name.name) == 'scanf'):
						nn5, ne5 = 1, 1
						nn, ne = (nn5 + nn), (ne5 + ne)	
					else:
						nn6, ne6 = funcComplexity(dictionary[str(item.name.name)])
						nn, ne = (1 + nn6 + nn), (2 + ne6 + ne)

	return (nn, ne) 	

if __name__ == "__main__":
	no_of_vertices, no_of_edges = findComplexity(ast)		
	print(no_of_vertices, no_of_edges)
	print("Cyclomatic Complexity:", no_of_edges - no_of_vertices + 2)

