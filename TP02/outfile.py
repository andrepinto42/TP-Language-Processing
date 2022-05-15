#-------------------
# Lexer Code
#-------------------

import ply.lex as lex

literals = ['=', '+', '-', '*', '/', '(', ')']
tokens = []
ignore = " \t\n"
def t_VAR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	print("Found a ID")
	return t

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t

def t_error(t):
	print(f"Illegal character {t.value[0]}") 
	t.lexer.skip(1) # Inside Here
	

lexer = lex.lex()

#-------------------
# Yacc Code
#-------------------

import ply.yacc as yacc

ts = { }
def p_grammar0(t):
	r'prog : comandos'
	

def p_grammar1(t):
	r'comandos : comando comandos'
	

def p_grammar2(t):
	r' comandos :'
	print("End of file")

def p_grammar3(t):
	r' comando : stat '
	

def p_grammar4(t):
	r'stat : VAR "=" exp'
	ts[t[1]] = t[3]

def p_grammar5(t):
	r'stat : exp'
	print(t[1])

def p_grammar6(t):
	r"exp : exp '+' exp "
	t[0] = t[1] + t[3]
	print("found a +")

def p_grammar7(t):
	r"exp : exp '-' exp "
	t[0] = t[1] - t[3]

def p_grammar8(t):
	r"exp : exp '*' exp "
	t[0] = t[1] * t[3]

def p_grammar9(t):
	r"exp : exp '/' exp "
	t[0] = t[1] / t[3]

def p_grammar10(t):
	r"exp : '(' exp ')' "
	t[0] = t[2]

def p_grammar11(t):
	r'exp : NUMBER '
	t[0] = t[1]

def p_grammar12(t):
	r'exp : VAR '
	t[0] = getval(t[1])

def p_error(p):
    print("Error in",p)


parser = yacc.yacc()


def getval(n):
    pass

str_Input = '''4*5+4'''

parser.parse(str_Input)

