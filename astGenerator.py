from pycparser import parse_file

ast = parse_file("test-1p.c", use_cpp = True)
ast.show()